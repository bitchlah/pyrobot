from pyrogram.types import CallbackQuery
from pyrogram.errors import MessageNotModified





class AlertUser(object):
    def alert_user(self, func):
        async def wrapper(_, cb: CallbackQuery):
            user = cb.from_user
            if user and not (user.id == self.id or user.id in self.SudoUsersList()):
                await cb.answer(
                    f"❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini !\nSilahkan buat ALBY-PYROBOT kamu disini @ruangprojects\nBisa juga hubungi @punya_alby", 
                    show_alert=True
                )
            else:
                try:
                    await func(_, cb)
                except MessageNotModified:
                    pass
        return wrapper
