"""
This file is for closed page inline help menu.
"""

from pyrogram import filters

from pyrogram.types import (
    InputMediaPhoto,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery
)

from PunyaAlby import app





@app.bot.on_callback_query(filters.regex("close-tab"))
@app.alert_user
async def _close(_, cb: CallbackQuery):
    await cb.edit_message_media(
        media=InputMediaPhoto(
            media=app.ALIVE_LOGO(), 
            caption=app.close_tab_string()
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="OPEN",
                        callback_data="home-tab"
                    )
                ]
            ]
        )
    )
