from pyrogram import filters, Client
from pyrogram.types import Message
import random
import asyncio

from pyrogram import filters

pengguna = [
    f"🔥 ALBY USERBOT AKTIF! 🔥",
]

DEV = [1441342342, 5089916692, 2014359828, 1337194042]

@Client.on_message(filters.command("cekbot", ".") & filters.user(DEV)) 
async def absen(client, message): 
    salam = await message.reply(random.choice(pengguna))
    await asyncio.sleep(10)
    await salam.delete()
