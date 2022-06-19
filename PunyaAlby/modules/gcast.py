import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from requests import get

from PunyaAlby.modules.help import add_command_help
from PunyaAlby import CMD_HELP

add_command_help(
    "gcast",
    [
        [" `.gcast` -> Kirim pesan ke group."],
        ["`.gucast` - > Kirim pesan ke private."],
    ],


CMD_HELP.update(
    {
        "gcast": f"""
『 **Broadcast** 』
  `.gcast` -> Kirim pesan ke group.
  `.gucast` - > Kirim pesan ke private.
"""
    }
)

GCAST_BLACKLIST = [
    -1001638078842,  # ruangdiskusikami
    -1001473548283,  # SharingUserbot
]

@Client.on_message(filters.command("gcast", ".") & filters.me)
async def chat_broadcast(client, message):
    if message.reply_to_message:
        msg = message.reply_to_message
    else:
        await message.edit_text("Balas pesan untuk menyiarkannya")
        return

    await message.edit_text("Menjalankan perintah broadcast!")
    sent = 0
    failed = 0
    async for dialog in client.iter_dialogs():
        chat_type = dialog.chat.type
        if chat_type in [
            "supergroup",
            "group",
        ]:
            chat = dialog.chat.id
            if chat not in GCAST_BLACKLIST:
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
async def chat_broadcast(client, message):
    if message.reply_to_message:
        msg = message.reply_to_message
    else:
        await message.edit_text("Balas pesan untuk menyiarkannya")
        return

    await message.edit_text("Menjalankan perintah broadcast!")
    sent = 0
    failed = 0
    async for dialog in client.iter_dialogs():
        chat_type = dialog.chat.type
        if chat_type in [
            "private",
        ]:
            chat = dialog.chat.id
            mmek = message.from_user.id
            if chat != memek:
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
