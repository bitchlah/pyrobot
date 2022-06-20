import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from requests import get
from PunyaAlby.modules.help import *

add_command_help(
    "gcast",
    [
        [".gcast", "Kirim pesan ke group."],
        [".gucast", "Kirim pesan khusus ke private chat."],
    ],
)


BL = get(
    "https://raw.githubusercontent.com/BukanDev/Prime-Json/master/blgcast.json"
).json()


@Client.on_message(filters.command("gcast", ".") & filters.me)
async def chat_broadcast(client: Client, message: Message):
    if message.reply_to_message:
        msg = message.reply_to_message.text.markdown
    else:
        await message.edit_text("Balas pesan untuk disiarkan")
        return

    await message.reply_text("Mengirim pesan ke seluruh group yang kamu ikuti!")
    sent = 0
    failed = 0
    async for dialog in client.iter_dialogs():
    if message.chat.type in ["group", "supergroup"]:
            chat = message.chat.id
            if chat not in BL:
                try:
                    await msg.copy(chat)
                    sent = sent + 1
                    await asyncio.sleep(0.1)
                except:
                    failed = failed + 1
                    await asyncio.sleep(0.1)

    return await message.edit_text(
        f"**Pesan global selesai \n\nTerkirim ke:** `{sent}` **Chats \nGagal terkirim ke:** `{failed}` **Chats**"
    )


@Client.on_message(filters.command("gucast", ".") & filters.me)
async def chat_broadcast(client: Client, message: Message):
    if message.reply_to_message:
        msg = message.reply_to_message.text.markdown
    else:
        await message.edit_text("Balas pesan untuk disiarkan")
        return

    await message.reply_text("Mengirim pesan ke seluruh private chat kamu!")
    sent = 0
    failed = 0
    async for dialog in client.iter_dialogs():
    if message.chat.type in ["private"]:
            chat = message.chat.id
            masih = message.from_user.id
            if chat != masih:
                try:
                    await msg.copy(chat)
                    sent = sent + 1
                    await asyncio.sleep(0.1)
                except:
                    failed = failed + 1
                    await asyncio.sleep(0.1)

    return await message.edit_text(
        f"**Pesan global selesai \n\nTerkirim ke:** `{sent}` **Chats \nGagal terkirim ke:** `{failed}` **Chats**"
    )
