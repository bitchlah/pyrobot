# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de


import sys
from os import environ, execle, remove

from pyrogram import Client, filters
from pyrogram.types import Message

from PunyaAlby import BOTLOG_CHATID, LOGGER
from PunyaAlby.helpers.basic import edit_or_reply
from PunyaAlby.helpers.misc import HAPP

from PunyaAlby.modules.help import *


@Client.on_message(filters.command("restart", [".", "-", "^", "!", "?"]) & filters.me)
async def restart_bot(_, message: Message):
    try:
        msg = await message.reply("⏳ `Memulai Ulang Bot!`")
        LOGGER(__name__).info("SERVER BOT DIMULAI KEMBALI !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("✅ **Bot dimulai ulang!**\n\n")
    if HAPP is not None:
        HAPP.restart()
    else:
        args = [sys.executable, "-m", "PunyaAlby"]
        execle(sys.executable, *args, environ)


@Client.on_message(filters.command(["shutdown", "off"], [".", "-", "^", "!", "?"]) & filters.me)
async def shutdown_bot(client: Client, message: Message):
    if BOTLOG_CHATID:
        await client.send_message(
            BOTLOG_CHATID,
            "**✅ SHUTDOWN** \n"
            "`ALBY-Pyrobot` telah di matikan!\nJika ingin menghidupkan kembali silahkan buka heroku",
        )
    await message.reply("🔌 `ALBY-Pyrobot` **Berhasil di matikan!**")
    if HAPP is not None:
        HAPP.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)


@Client.on_message(filters.command("logs", [".", "-", "^", "!", "?"]) & filters.me)
async def logs_ubot(client: Client, message: Message):
    if HAPP is None:
        return await edit_or_reply(
            message,
            "Pastikan `HEROKU_API_KEY` dan `HEROKU_APP_NAME` anda dikonfigurasi dengan benar di config vars heroku",
        )
    Man = await message.reply("🧾 `Mendapatkan Log Bot Anda.`")
    with open("Logs-Heroku.txt", "w") as log:
        log.write(HAPP.get_log())
    await client.send_document(
        message.chat.id,
        "Logs-Heroku.txt",
        thumb="https://telegra.ph/file/bc0cbf95ece5564dbcaa9.jpg",
        caption="**Ini adalah Log Heroku Anda**",
    )
    await Man.delete()
    remove("Logs-Heroku.txt")


add_command_help(
    "system",
    [
        [".restart", "Untuk merestart userbot."],
        [".shutdown or off", "Untuk mematikan userbot."],
        [".logs", "Untuk melihat logs userbot."],
    ],
)
