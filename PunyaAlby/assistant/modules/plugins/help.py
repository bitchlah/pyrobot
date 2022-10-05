from pyrogram import filters

from pyrogram.types import (
    InlineKeyboardMarkup, 
    Message,
)

from PunyaAlby.client import app





emoji = app.HelpEmoji() or "•"

settings = app.BuildKeyboard(([f"{emoji} Modules {emoji}", "plugins-tab"]))
extra = app.BuildKeyboard(([f"{emoji} Diskusi {emoji}", "https://t.me/ruangdiskusikami"], [f"{emoji} Updates {emoji}", "https://t.me/ruangprojects"]))
close = app.BuildKeyboard(([["Close", "close-tab"]]))




# /help command for bot
@app.bot.on_message(filters.command("help"), group=-1)
async def start(_, m: Message):
    if m.from_user:
        if m.from_user.id == app.id:
            # bot pic
            buttons=InlineKeyboardMarkup(
                [ settings, extra, close ]
            )
            botpic = app.BotPic().split(".")[-1] # extension of media
            if botpic in ("jpg", "png", "jpeg"):
                info = await app.bot.send_photo(
                    m.chat.id,
                    app.BotPic(),
                    app.BotBio(m),
                    reply_markup=buttons
                )
            elif botpic in ("mp4", "gif"):
                info = await app.bot.send_video(
                    m.chat.id,
                    app.BotPic(),
                    app.BotBio(m),
                    reply_markup=buttons
                )
            else:
                info = await app.bot.send_message(
                    m.chat.id,
                    app.BotBio(m),
                    reply_markup=buttons
                )
        app.message_ids.update({info.chat.id : info.id})
