# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
import time
from platform import python_version

from pyrogram import Client
from pyrogram import __version__ as versipyro
from pyrogram import filters
from pyrogram.types import Message

from config import ALIVE_LOGO, ALIVE_TEKS_CUSTOM, BOT_VER
from PunyaAlby import CMD_HELP, StartTime
from PunyaAlby.helpers.basic import edit_or_reply
from PunyaAlby.helpers.PyroHelpers import ReplyCheck
from PunyaAlby.utils.tools import get_readable_time

from .help import add_command_help

modules = CMD_HELP
alive_text = ALIVE_TEKS_CUSTOM


@Client.on_message(filters.command(["alive", "alby"], [".", "-", "^", "!", "?"]) & filters.me)
async def alive(client: Client, message: Message):
    xx = await message.reply("💃")
    await asyncio.sleep(2)
    apa = client.send_video if ALIVE_LOGO.endswith(".mp4") else client.send_photo
    uptime = await get_readable_time((time.time() - StartTime))
    capt = (
        f"✘ <b> [ALBY-Pyrobot](https://github.com/PunyaAlby/ALBY-Pyrobot) is Up and Running. </b> ✘\n\n"
        f"<b>{alive_text}</b>\n"
        f"◈ ━━━━━━ ◆ ━━━━━━ ◈\n"
        f"✘ <b>Master: </b> {client.me.mention} \n"
        f"✘ <b>Modules: </b> <code>{len(modules)} Modules</code> \n"
        f"✘ <b>Bot Version: </b> <code>{BOT_VER}</code> \n"
        f"✘ <b>Python Version: </b> <code>{python_version()}</code> \n"
        f"✘ <b>Pyrogram Version: </b> <code>{versipyro}</code> \n"
        f"　  (\︵/) \n"
        f"　⫺( •ᆺ•)⫹ \n"
        f"┏━∪ ━━━━━━━━━━━\n"
        f"╏<b>[𝗦𝘂𝗽𝗽𝗼𝗿𝘁](https://t.me/ruangdiskusikami)</b> & <b>[𝗖𝗵𝗮𝗻𝗻𝗲𝗹](https://t.me/ruangprojects)</b>\n"
        f"┗━━━━━━━━━━━━━"
    )
    await asyncio.gather(
        xx.delete(),
        apa(
            message.chat.id,
            ALIVE_LOGO,
            caption=capt,
            reply_to_message_id=ReplyCheck(message),
        ),
    )

add_command_help(
    "alive",
    [
        [".alby or .alive", "Perintah ini untuk memeriksa userbot anda berfungsi atau tidak."],
    ],
)
