import time

from main.userbot.client import app

from pyrogram import filters
from pyrogram.types import Message




@app.bot.on_message(filters.command("start"), group=-1)
async def send_response(_, m: Message):
    await m.reply("Ada yang bisa saya bantu ?\nsilahkan ketik /help untuk mengetahui fitur yang tersedia")



@app.bot.on_message(filters.new_chat_members & filters.group, group=1)
async def added_to_group_msg(_, m: Message):
    if m.new_chat_members[0].is_self:
        try:
            await app.bot.send_message(
                m.chat.id,
                "Terimakasih telah memasukkan saya ke dalam group ini !\nsilahkan ketik /help untuk mengetahui fitur yang tersedia."
            )
        except Exception as e:
            await app.error(m, e)
    else:
        return
