from pyrogram import filters
from pyrogram import __version__ as pyro_vr
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from config import *
from pyrogram import Client
from config import ALIVE_LOGO
from PunyaAlby.modules.help import *
 

@Client.on_message(filters.command(["alive", "awake"], [".", "!"]) & filters.me)
async def alive(client: Client, e: Message):
        Alive_msg = f"𝐀𝐋𝐁𝐘 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐈𝐬 𝐎𝐧 𝐅𝐢𝐫𝐞 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► Vᴇʀsɪᴏɴ : `Beta.0.1` \n"
        Alive_msg += f"► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `{pyro_vr}` \n"
        Alive_msg += f"► SUPPORT : [Jᴏɪɴ](https://t.me/ruangdiskusikami) \n"
        Alive_msg += f"► UPDATES : [Jᴏɪɴ](https://t.me/ruangprojects) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🎥 Watch ", url=f"https://t.me/ruangdiskusikami"
                        ),
                        InlineKeyboardButton(
                            text="🔄 Updates", url=f"https://t.me/ruangdiskusikami"
                        ),
                    ],
                ]
            )
        await e.reply_photo(
        photo=ALIVE_LOGO,
        caption=Alive_msg,
        parse_mode="markdown",
        reply_markup=key,
        )


add_command_help(
    "alive",
    [
        [
            ".alive",
            "This Command for check your bot working or nt",
        ]
    ],
)
