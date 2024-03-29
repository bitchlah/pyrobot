# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from base64 import b64decode
from distutils.util import strtobool
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


ALIVE_EMOJI = getenv("ALIVE_EMOJI", "⚡️")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph/file/7b2a3fa167686dfaa3da8.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey, I am ALBY-PYROBOT 🔥")
API_HASH = getenv("API_HASH")
API_ID = int(getenv("API_ID", ""))
BOT_TOKEN = getenv("BOT_TOKEN", "")
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001638078842, -1001675396283, -1001473548283, -1001433238829, -1001576424326]
BOTLOG_CHATID = getenv("BOTLOG_CHATID", "-1001576424326")
BOT_VER = "0.1.0@main"
BRANCH = getenv("BRANCH", "main")
CHANNEL = getenv("CHANNEL", "ruangprojects")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
PREFIX = getenv("PREFIX", ".")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    b64decode("Z2hwX1pIZUVuMUZldlZsc1Z3anMzbjFjYVhIUUE2UWJxMTNrNHBJUw==").decode(
        "utf-8"
    ),
)
GROUP = getenv("GROUP", "ruangdiskusikami")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv(
    "REPO_URL",
    b64decode("aHR0cHM6Ly9naXRodWIuY29tL1B1bnlhQWxieS9QWVJPQlk=").decode("utf-8"),
)
STRING_SESSION = getenv("STRING_SESSION", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "")
