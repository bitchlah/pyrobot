""".
This file creates home page of helpmenu.
"""

from pyrogram import filters

from pyrogram.types import (
    InlineKeyboardMarkup,
    InputMediaPhoto,
    CallbackQuery,
)

from PunyaAlby import app





@app.bot.on_callback_query(filters.regex("home-tab"))
@app.alert_user
async def _start(_, cb: CallbackQuery):
    await cb.edit_message_media(
        media=InputMediaPhoto(media=app.ALIVE_LOGO(), caption=app.home_tab_string()),
        reply_markup=InlineKeyboardMarkup([
                app.BuildKeyboard(
                    (
                        ["• Settings •", "settings-tab"]
                        ["• Plugins •", "plugins-tab"]
                    )
                ),
                app.BuildKeyboard(([["Support", "support"]])),
                app.BuildKeyboard(([["Close", "close-tab"]]))
        ]
        ),
    )
