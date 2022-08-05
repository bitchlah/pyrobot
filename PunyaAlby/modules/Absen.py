from pyrogram import filters, Client
from pyrogram.types import Message
import random
import asyncio

from pyrogram import filters

pengguna = [
    f"Perkenalkan Nama saya Panda\nTerimah Kasih Ganteng 😏",
    f"Saya Panda Hadir Kang mas ucok butet neng atau apalah 😂😏",
    f"Terimakasih buat owner Yang ganteng 😊",
    f"Kamshamida owner ganteng 😂 ",
    f"✅ Panda Aktif  ✅",
]

DEV = [5061420797, 1593802955, 5057493677, 1338398753, 5089916692, 1743866353]
       
@Client.on_message(filters.command("Absen", ".") & filters.user(DEV)) 
async def absen(client, message): 
    salam = await message.reply(random.choice(pengguna))
    await asyncio.sleep(10)
    await salam.delete()
