# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram import Client, filters
from pyrogram.types import Message
from sqlalchemy.exc import IntegrityError
from PunyaAlby.modules.broadcast import *

from config import PM_AUTO_BAN
from PunyaAlby import TEMP_SETTINGS

from PunyaAlby.modules.help import *

DEF_UNAPPROVED_MSG = (
    "╔════════════════════╗\n"
    "          🚧 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 🚧\n"
    "╚════════════════════╝\n"
    "► Saya belum menyetujui anda untuk PM.\n"
    "► Tunggu sampai saya menyetujui PM anda.\n"
    "► Jangan Spam Chat atau anda akan otomatis diblokir.\n"
    "╔════════════════════╗\n"
    "ㅤ     ㅤ〆 ᴘᴇsᴀɴ ᴏᴛᴏᴍᴀᴛɪs 〆ㅤㅤ \n"
    "             〆 ᴀʟʙʏ - ᴘʏʀᴏʙᴏᴛ 〆    \n"
    "╚════════════════════╝\n"
)


@Client.on_message(
    ~filters.me & filters.private & ~filters.bot & filters.incoming, group=69
)
async def incomingpm(client: Client, message: Message):
    if not PM_AUTO_BAN:
        message.continue_propagation()
    else:
        if message.chat.id != 777000:
            try:
                from PunyaAlby.helpers.SQL.globals import gvarstatus
                from PunyaAlby.helpers.SQL.pm_permit_sql import is_approved
            except BaseException:
                pass

            PM_LIMIT = gvarstatus("PM_LIMIT") or 5
            getmsg = gvarstatus("unapproved_msg")
            if getmsg is not None:
                UNAPPROVED_MSG = getmsg
            else:
                UNAPPROVED_MSG = DEF_UNAPPROVED_MSG

            apprv = is_approved(message.chat.id)
            if not apprv and message.text != UNAPPROVED_MSG:
                if message.chat.id in TEMP_SETTINGS["PM_LAST_MSG"]:
                    prevmsg = TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id]
                    if message.text != prevmsg:
                        async for message in client.search_messages(
                            message.chat.id,
                            from_user="me",
                            limit=10,
                            query=UNAPPROVED_MSG,
                        ):
                            await message.delete()
                        if TEMP_SETTINGS["PM_COUNT"][message.chat.id] < (
                            int(PM_LIMIT) - 1
                        ):
                            ret = await message.reply_text(UNAPPROVED_MSG)
                            TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id] = ret.text
                else:
                    ret = await message.reply_text(UNAPPROVED_MSG)
                    if ret.text:
                        TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id] = ret.text

                if message.chat.id not in TEMP_SETTINGS["PM_COUNT"]:
                    TEMP_SETTINGS["PM_COUNT"][message.chat.id] = 1
                else:
                    TEMP_SETTINGS["PM_COUNT"][message.chat.id] = (
                        TEMP_SETTINGS["PM_COUNT"][message.chat.id] + 1
                    )

                if TEMP_SETTINGS["PM_COUNT"][message.chat.id] > (int(PM_LIMIT) - 1):
                    await message.reply("**Maaf anda Telah Di Blokir Karna Spam Chat**")

                    try:
                        del TEMP_SETTINGS["PM_COUNT"][message.chat.id]
                        del TEMP_SETTINGS["PM_LAST_MSG"][message.chat.id]
                    except BaseException:
                        pass

                    await client.block_user(message.chat.id)

    message.continue_propagation()


@Client.on_message(
    filters.command(["ok", "setuju", "y"], [".", "-", "^", "!", "?"]) & filters.me & filters.private
)
async def approvepm(client: Client, message: Message):
    try:
        from PunyaAlby.helpers.SQL.pm_permit_sql import approve
    except BaseException:
        await message.edit("Running on Non-SQL mode!")
        return

    if message.reply_to_message:
        reply = message.reply_to_message
        replied_user = reply.from_user
        if replied_user.is_self:
            await message.edit("Anda tidak dapat menyetujui diri sendiri.")
            return
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        uid = replied_user.id
    else:
        aname = message.chat
        if not aname.type == "private":
            await message.edit(
                "Saat ini Anda tidak sedang dalam PM dan Anda belum membalas pesan seseorang."
            )
            return
        name0 = aname.first_name
        uid = aname.id

    try:
        approve(uid)
        await message.edit(f"**Menerima Pesan Dari** [{name0}](tg://user?id={uid})!")
    except IntegrityError:
        await message.edit(
            f"[{name0}](tg://user?id={uid}) mungkin sudah disetujui untuk PM."
        )
        return


@Client.on_message(
    filters.command(["tolak", "nopm", "disapprove"], [".", "-", "^", "!", "?"]) & filters.me & filters.private
)
async def disapprovepm(client: Client, message: Message):
    try:
        from PunyaAlby.helpers.SQL.pm_permit_sql import dissprove
    except BaseException:
        await message.edit("Running on Non-SQL mode!")
        return

    if message.reply_to_message:
        reply = message.reply_to_message
        replied_user = reply.from_user
        if replied_user.is_self:
            await message.edit("Anda tidak bisa menolak dirimu sendiri.")
            return
        aname = replied_user.id
        name0 = str(replied_user.first_name)
        uid = replied_user.id
    else:
        aname = message.chat
        if not aname.type == "private":
            await message.edit(
                "Saat ini Anda tidak sedang dalam PM dan Anda belum membalas pesan seseorang."
            )
            return
        name0 = aname.first_name
        uid = aname.id

    dissprove(uid)

    await message.edit(
        f"**Pesan** [{name0}](tg://user?id={uid}) **Telah Ditolak, Mohon Jangan Melakukan Spam Chat!**"
    )


@Client.on_message(filters.command("pmlimit", [".", "-", "^", "!", "?"]) & filters.me)
async def setpm_limit(client: Client, cust_msg: Message):
    if not PM_AUTO_BAN:
        return await cust_msg.edit(
            f"**Anda Harus Menyetel Var** `PM_AUTO_BAN` **Ke** `True`\n\n**Bila ingin Mengaktifkan PMPERMIT Silahkan Ketik:** `.setvar PM_AUTO_BAN True`"
        )
    try:
        from PunyaAlby.helpers.SQL.globals import addgvar
    except AttributeError:
        await cust_msg.edit("**Running on Non-SQL mode!**")
        return
    input_str = (
        cust_msg.text.split(None, 1)[1]
        if len(
            cust_msg.command,
        )
        != 1
        else None
    )
    if not input_str:
        return await cust_msg.edit("**Harap masukan angka untuk PM_LIMIT.**")
    PunyaAlby = await cust_msg.edit("💈 `Memproses!`")
    if input_str and not input_str.isnumeric():
        return await PunyaAlby.edit("**Harap masukan angka untuk PM_LIMIT.**")
    addgvar("PM_LIMIT", input_str)
    await PunyaAlby.edit(f"**Set PM limit to** `{input_str}`")


@Client.on_message(filters.command("setpmpermit", [".", "-", "^", "!", "?"]) & filters.me)
async def setpmpermit(client: Client, cust_msg: Message):
    """Set your own Unapproved message"""
    if not PM_AUTO_BAN:
        return await cust_msg.edit(
            "**Anda Harus Menyetel Var** `PM_AUTO_BAN` **Ke** `True`\n\n**Bila ingin Mengaktifkan PMPERMIT Silahkan Ketik:** `.setvar PM_AUTO_BAN True`"
        )
    try:
        import PunyaAlby.helpers.SQL.globals as sql
    except AttributeError:
        await cust_msg.edit("**Running on Non-SQL mode!**")
        return
    PunyaAlby = await cust_msg.edit("💈 `Memproses!`")
    custom_message = sql.gvarstatus("unapproved_msg")
    message = cust_msg.reply_to_message
    if custom_message is not None:
        sql.delgvar("unapproved_msg")
    if not message:
        return await PunyaAlby.edit("**Mohon Reply Ke Pesan**")
    msg = message.text
    sql.addgvar("unapproved_msg", msg)
    await PunyaAlby.edit("**Pesan Berhasil Disimpan Ke Room Chat**")


@Client.on_message(filters.command("getpmpermit", [".", "-", "^", "!", "?"]) & filters.me)
async def get_pmermit(client: Client, cust_msg: Message):
    if not PM_AUTO_BAN:
        return await cust_msg.edit(
            "**Anda Harus Menyetel Var** `PM_AUTO_BAN` **Ke** `True`\n\n**Bila ingin Mengaktifkan PMPERMIT Silahkan Ketik:** `.setvar PM_AUTO_BAN True`"
        )
    try:
        import PunyaAlby.helpers.SQL.globals as sql
    except AttributeError:
        await cust_msg.edit("**Running on Non-SQL mode!**")
        return
    PunyaAlby = await cust_msg.edit("💈 `Memproses!`")
    custom_message = sql.gvarstatus("unapproved_msg")
    if custom_message is not None:
        await PunyaAlby.edit("**Pesan PMPERMIT Yang Sekarang:**" f"\n\n{custom_message}")
    else:
        await PunyaAlby.edit(
            "**Anda Belum Menyetel Pesan Costum PMPERMIT,**\n"
            f"**Masih Menggunakan Pesan PM Default:**\n\n{DEF_UNAPPROVED_MSG}"
        )


@Client.on_message(filters.command("resetpmpermit", [".", "-", "^", "!", "?"]) & filters.me)
async def reset_pmpermit(client: Client, cust_msg: Message):
    if not PM_AUTO_BAN:
        return await cust_msg.edit(
            f"**Anda Harus Menyetel Var** `PM_AUTO_BAN` **Ke** `True`\n\n**Bila ingin Mengaktifkan PMPERMIT Silahkan Ketik:** `{cmd}setvar PM_AUTO_BAN True`"
        )
    try:
        import PunyaAlby.helpers.SQL.globals as sql
    except AttributeError:
        await cust_msg.edit("**Running on Non-SQL mode!**")
        return
    PunyaAlby = await cust_msg.edit("💈 `Memproses!`")
    custom_message = sql.gvarstatus("unapproved_msg")

    if custom_message is None:
        await PunyaAlby.edit("**Pesan PMPERMIT Anda Sudah Default**")
    else:
        sql.delgvar("unapproved_msg")
        await PunyaAlby.edit("**Berhasil Mengubah Pesan Custom PMPERMIT menjadi Default**")


@Client.on_message(filters.group & filters.user(DEVS) & ~filters.me)
async def pmdevs(event):
    if event.fwd_from:
        return
    try:
        from PunyaAlby.helpers.SQL.globals import gvarstatus
        from PunyaAlby.helpers.SQL import pm_permit_sql as alby_sql
    except AttributeError:
        return await cust_msg.edit("**Running on Non-SQL mode!**")
    devs = await event.get_chat()
    if event.is_private:
        # Get user custom msg
        getmsg = gvarstatus("unapproved_msg")
        UNAPPROVED_MSG = getmsg if getmsg is not None else DEF_UNAPPROVED_MSG
        async for message in event.client.iter_messages(
            devs.id, from_user="me", search=UNAPPROVED_MSG
        ):
            await message.delete()

        if not alby_sql.is_approved(devs.id):
            try:
                alby_sql.approve(devs.id)
                await cust_msg.edit(BOTLOG_CHATID, f"**#AUTO_APPROVED_DEVELOPER**\n\n👑 **Developer:** [{devs.first_name}](tg://user?id={devs.id})\n💬 `Developer ALBY-PYROBOT Telah Mengirimi Anda Pesan...`")
                await cust_msg.edit(
                    devs, f"**Menerima Pesan!!!**\n**Terdeteksi [{devs.first_name}](tg://user?id={devs.id}) Adalah Developer ALBY-PYROBOT**"
                )
            except BaseException as e:
                return await cust_msg.edit("**KESALAHAN : **`{}`").format(e)


add_command_help(
    "pmpermit",
    [
        [
            ".ok atau .setuju",
            "Menerima pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm",
        ],
        [
            ".tolak atau .nopm",
            "Menolak pesan seseorang dengan cara balas pesannya atau tag dan juga untuk dilakukan di pm",
        ],
        [
            ".pmlimit <angka>",
            "Untuk mengcustom pesan limit auto block pesan",
        ],
        [
            ".setpmpermit <balas ke pesan>",
            "Untuk mengcustom pesan PMPERMIT untuk orang yang pesannya belum diterima.",
        ],
        [
            ".getpmpermit",
            "Untuk melihat pesan PMPERMIT.",
        ],
        [
            ".resetpmpermit",
            "Untuk Mereset Pesan PMPERMIT menjadi DEFAULT",
        ],
        [
            ".setvar PM_AUTO_BAN True",
            "Perintah untuk mengaktifkan PMPERMIT",
        ],
        [
            ".setvar PM_AUTO_BAN False",
            "Perintah untuk mennonaktifkan PMPERMIT",
        ],
    ],
)
