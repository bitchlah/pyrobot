# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram import idle

from config import *
from PunyaAlby import BOTLOG_CHATID, LOGGER, LOOP, bots
from PunyaAlby.helpers.misc import git, heroku
from PunyaAlby.client import app

MSG_ON = """
🔥 **ALBY-PYROBOT Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}alby` **untuk Mengecheck Bot**
━━
"""

async def start_assistant():
    """ this function starts the pyrogram bot client. """
    if app and app.bot:
        print("Activating assistant.\n")
        response = await app.bot.start()
        if response:
            print("Assistant activated.\n")
            botcmd = [
                ["start", "check whether bot is on or not."],
                ["help", "Get your helpdex."],
                ["ping", "Get server response speed & uptime."],
                ["id", "Get ids of users / groups."],
                ["quote", "get inline anime quotes."],
                ["broadcast", "send messages to users who have started your bot."],
            ]
            cmds = [x.command for x in await app.bot.get_bot_commands()]
            botcmdkeys = [y[0] for y in botcmd]

            if cmds != botcmdkeys:
                print("Setting bot commands.\n")
                await app.bot.set_bot_commands([BotCommand(y[0], y[1]) for y in botcmd])
                print("Added bot commands.\n")
        else:
            print("Assistant is not activated.\n")
    else:
        print("Assistant start unsuccessful, please check that you have given the bot token.\n")
        print("skipping assistant start !")


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("ruangdiskusikami")
            await bot.join_chat("ruangprojects")
            await bot.join_chat("ruang_gabutku")
            await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
        except Exception as a:
            LOGGER("main").warning(a)
    await idle()


if __name__ == "__main__":
    LOGGER("PunyaAlby").info("Starting ALBY-PYROBOT")
    git()
    heroku()
    LOGGER("PunyaAlby").info(f"ALBY-PYROBOT v{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")
    LOOP.run_until_complete(main())
