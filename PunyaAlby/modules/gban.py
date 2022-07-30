import asyncio
from pyrogram import filters
from requests import get
from pyrogram.errors import PeerIdInvalid


DEVS = get(
    "https://raw.githubusercontent.com/BukanDev/Prime-Json/master/dev.json"
).json()


@Client.on_message(filters.command("gban", ".") & filters.me)
async def gban(client, message):
    kontol = await message.edit_text("Menjalankan perintah gban user")
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        get_user = message.from_user.id
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except ValueError:
            pass
    try:
        user = await client.get_users(get_user)
    except PeerIdInvalid:
        await message.edit_text("Tidak menemukan user tersebut.")
        return

    iso = 0
    gagal = 0
    prik = user.id
    async for dialog in app.iter_dialogs():
        chat_type = dialog.chat.type
        if chat_type in ["group", "supergroup", "channel"]:
            chat = dialog.chat.id
            if prik not in DEVS:
                try:
                    await app.ban_chat_member(chat, prik)
                    iso = iso + 1
                    await asyncio.sleep(0.1)
                    await kontol.delete()
                except:
                    gagal = gagal + 1
                    await asyncio.sleep(0.1)

    return await app.send_message(
        message.chat.id,
        f"Global Banned \n\nTerbanned: {iso} Chats \nGagal Banned: {gagal} Chats\nKorban: [{user.first_name}](tg://user?id={prik})",
    )
    await kontol.delete()


@Client.on_message(filters.command("ungban", ".") & filters.me)
async def ungban(client, message):
    kontol = await message.edit_text("Menjalankan proses ungban user")
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        get_user = message.from_user.id
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except ValueError:
            pass
    try:
        user = await client.get_users(get_user)
    except PeerIdInvalid:
        await message.edit_text("Tidak menemukan user tersebut.")
        return

    iso = 0
    gagal = 0
    prik = user.id
    async for dialog in app.iter_dialogs():
        chat_type = dialog.chat.type
        if chat_type in ["group", "supergroup", "channel"]:
            chat = dialog.chat.id
            if prik not in DEVS:
                try:
                    await app.unban_chat_member(chat, prik)
                    iso = iso + 1
                    await asyncio.sleep(0.1)
                    await kontol.delete()
                except:
                    gagal = gagal + 1
                    await asyncio.sleep(0.1)

    return await app.send_message(
        message.chat.id,
        f"Unglobal Banned \n\nUngbanned: {iso} Chats \nGagal Unbanned: {gagal} Chats\nKorban: [{user.first_name}](tg://user?id={prik})",
    )
