import asyncio
import os
import socket
import sys
from datetime import datetime
from os import environ, execle, path, remove

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from pyrogram import Client, filters
from pyrogram.types import Message

from config import BRANCH
from config import GIT_TOKEN, HEROKU_API_KEY, HEROKU_APP_NAME
from PunyaAlby.modules.broadcast import *
from PunyaAlby.helpers.basic import edit_or_reply
from PunyaAlby.helpers.misc import HAPP, XCB
from PunyaAlby.helpers.tools import get_arg
from PunyaAlby.utils.pastebin import PasteBin

from .help import add_command_help

GCAST_BL = "https://github.com/bitchlah/cadangan"

if GIT_TOKEN:
    GIT_USERNAME = GCAST_BL.split("com/")[1].split("/")[0]
    TEMP_REPO = GCAST_BL.split("https://")[1]
    UPSTREAM_REPO = f"https://{GIT_USERNAME}:{GIT_TOKEN}@{TEMP_REPO}"
UPSTREAM_REPO_URL = UPSTREAM_REPO
requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), "requirements.txt"
)


async def is_heroku():
    return "heroku" in socket.getfqdn()


async def gen_chlog(repo, diff):
    ch_log = ""
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff):
        ch_log += (
            f"• [{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n"
        )
    return ch_log


async def updateme_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            " ".join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


@Client.on_message(
    filters.command("diupdate", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command("hiupdate", [".", "-", "^", "!", "?"]) & filters.me)
async def upstream(client: Client, message: Message):
    status = await message.reply("🔎 `Memeriksa Pembaruan, Tunggu Beberapa Saat!`")
    conf = get_arg(message)
    off_repo = UPSTREAM_REPO_URL
    try:
        txt = (
            "**Pembaruan Tidak Dapat Di Lanjutkan Karna "
            + "Terjadi Beberapa Kegagalan**\n\n**LOGTRACE:**\n"
        )
        repo = Repo()
    except NoSuchPathError as error:
        await status.edit(f"{txt}\n**Direktori** `{error}` **Tidak Dapat Di Temukan.**")
        repo.__del__()
        return
    except GitCommandError as error:
        await status.edit(f"{txt}\n**Gagal!** `{error}`")
        repo.__del__()
        return
    except InvalidGitRepositoryError:
        if conf != "deploy":
            pass
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        repo.create_head(
            BRANCH,
            origin.refs[BRANCH],
        )
        repo.heads[BRANCH].set_tracking_branch(origin.refs[BRANCH])
        repo.heads[BRANCH].checkout(True)
    ac_br = repo.active_branch.name
    if ac_br != BRANCH:
        await status.edit(
            f"**[UPDATER]:** `Sepertinya Anda menggunakan branch Anda sendiri ({ac_br}). dalam hal ini, Updater tidak dapat mengidentifikasi cabang mana yang akan digabungkan. silahkan checkout ke branch utama`"
        )
        repo.__del__()
        return
    try:
        repo.create_remote("upstream", off_repo)
    except BaseException:
        pass
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)
    changelog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    if "deploy" not in conf:
        if changelog:
            changelog_str = f"🔮 **Pembaruan Tersedia Untuk branch [{ac_br}]:\n\nPERUBAHAN:**\n\n`{changelog}`"
            if len(changelog_str) > 4096:
                await status.edit("**Changelog terlalu besar, dikirim sebagai file.**")
                file = open("output.txt", "w+")
                file.write(changelog_str)
                file.close()
                await client.send_document(
                    message.chat.id,
                    "output.txt",
                    caption=f"**Ketik** `.update deploy` **Untuk Mengupdate Userbot.**",
                    reply_to_message_id=status.message_id,
                )
                remove("output.txt")
            else:
                return await status.edit(
                    f"{changelog_str}\n**Ketik** `.update deploy` **Untuk Mengupdate Userbot.**",
                    disable_web_page_preview=True,
                )
        else:
            await status.edit(
                f"\n`BOT Anda`  **sudah di update**  `dengan branch`  **[{ac_br}]**\n",
                disable_web_page_preview=True,
            )
            repo.__del__()
            return
    if HEROKU_API_KEY is not None:
        import heroku3

        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_app = None
        heroku_applications = heroku.apps()
        if not HEROKU_APP_NAME:
            await status.edit(
                "`Silakan atur HEROKU_APP_NAME variabel untuk dapat memperbarui userbot.`"
            )
            repo.__del__()
            return
        for app in heroku_applications:
            if app.name == HEROKU_APP_NAME:
                heroku_app = app
                break
        if heroku_app is None:
            await status.edit(
                f"{txt}\n`Kredensial Heroku tidak valid untuk memperbarui userbot dyno.`"
            )
            repo.__del__()
            return
        await status.edit(
            "`[HEROKU]: ⏳ Update Deploy `ALBY-PYROBOT` Sedang Dalam Proses...`"
        )
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", "https://api:" + HEROKU_API_KEY + "@"
        )
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
            remote.push(refspec="HEAD:refs/heads/main", force=True)
        except GitCommandError:
            pass
        await status.edit(
            "✅ `ALBY-PYROBOT Berhasil Diperbarui! Userbot dapat digunakan kembali.`"
        )
    else:
        try:
            ups_rem.pull(ac_br)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        await updateme_requirements()
        await status.edit(
            "✅ `ALBY-PYROBOT Berhasil Diperbarui! Userbot dapat digunakan kembali.`",
        )
        args = [sys.executable, "-m", "PunyaAlby"]
        execle(sys.executable, *args, environ)
        return


@Client.on_message(filters.command("cupdate", ["."]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("update", [".", "-", "^", "!", "?"]) & filters.me)
async def updaterman(client: Client, message: Message):
    if await is_heroku():
        if HAPP is None:
            return await edit_or_reply(
                message,
                "Pastikan HEROKU_API_KEY dan HEROKU_APP_NAME anda dikonfigurasi dengan benar di config vars heroku",
            )
    response = await message.reply("🧭 Memeriksa pembaruan yang tersedia!")
    try:
        repo = Repo()
    except GitCommandError:
        return await response.edit("Git Command Error")
    except InvalidGitRepositoryError:
        return await response.edit("Invalid Git Repsitory")
    to_exc = f"git fetch origin {BRANCH} &> /dev/null"
    os.system(to_exc)
    await asyncio.sleep(7)
    verification = ""
    REPO_ = repo.remotes.origin.url.split(".git")[0]  # main git repository
    for checks in repo.iter_commits(f"HEAD..origin/{BRANCH}"):
        verification = str(checks.count())
    if verification == "":
        return await response.edit("Bot sudah Di update!")
    updates = ""
    ordinal = lambda format: "%d%s" % (
        format,
        "tsnrhtdd"[(format // 10 % 10 != 1) * (format % 10 < 4) * format % 10 :: 4],
    )
    for info in repo.iter_commits(f"HEAD..origin/{BRANCH}"):
        updates += f"<b>➣ #{info.count()}: [{info.summary}]({REPO_}/commit/{info}) by -> {info.author}</b>\n\t\t\t\t<b>➥ Waktu Update:</b> {ordinal(int(datetime.fromtimestamp(info.committed_date).strftime('%d')))} {datetime.fromtimestamp(info.committed_date).strftime('%b')}, {datetime.fromtimestamp(info.committed_date).strftime('%Y')}\n\n"
    _update_response_ = "<b>Pembaruan baru tersedia untuk Bot!</b>\n\n➣ Mengupdate Pembaruan Sekarang</code>\n\n**<u>Pembaruan:</u>**\n\n"
    _final_updates_ = _update_response_ + updates
    if len(_final_updates_) > 4096:
        url = await PasteBin(updates)
        nrs = await response.edit(
            f"<b>Pembaruan baru tersedia untuk Bot!</b>\n\n➣ Mengupdate Pembaruan Sekarang</code>\n\n**<u>Pembaruan:</u>**\n\n[Klik Di Sini untuk checkout Pembaruan]({url})"
        )
    else:
        nrs = await response.edit(_final_updates_, disable_web_page_preview=True)
    os.system("git stash &> /dev/null && git pull")
    if await is_heroku():
        try:
            await response.edit(
                f"{nrs.text}\n\n🤖 Bot berhasil diperbarui di Heroku! Sekarang, tunggu 2 - 3 menit sampai bot restart!"
            )
            os.system(
                f"{XCB[5]} {XCB[7]} {XCB[9]}{XCB[4]}{XCB[0]*2}{XCB[6]}{XCB[4]}{XCB[8]}{XCB[1]}{XCB[5]}{XCB[2]}{XCB[6]}{XCB[2]}{XCB[3]}{XCB[0]}{XCB[10]}{XCB[2]}{XCB[5]} {XCB[11]}{XCB[4]}{XCB[12]}"
            )
            return
        except Exception as err:
            return await response.edit(f"{nrs.text}\n\nGagal: <code>{err}</code>")
    else:
        os.system("pip3 install -r requirements.txt")
        os.system(f"kill -9 {os.getpid()} && bash start")
        exit()

        
add_command_help(
    "update",
    [
        [".update", "Untuk melihat list pembaruan terbaru dari ALBY-PYROBOT."],
        [".update deploy", "Untuk mengupdate userbot."],
    ],
)
