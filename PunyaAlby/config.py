import os
import aiohttp
from distutils.util import strtobool
from os import getenv
from dotenv import load_dotenv
    
if os.path.exists("Internal"):
    load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
admins = {}
que = {}

ALIVE_EMOJI = getenv("ALIVE_EMOJI", "⚡️")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph/file/7b2a3fa167686dfaa3da8.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey, I am ALBY-PYROBOT 🔥")
API_ID = int(getenv("API_ID", "1020199"))
API_HASH = getenv("API_HASH", "3672885f650c19ef18d53548bb641d5f")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001638078842, -1001675396283, -1001473548283, -1001433238829, -1001576424326]
CHANNEL = getenv("CHANNEL", "ruangprojects")
GROUP = getenv("GROUP", "ruangdiskusikami")
STRING_SESSION = getenv("STRING_SESSION", "session")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! /").split())
CMD_HANDLER = getenv("CMD_HANDLER", ".")
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
MONGO_DB_URL = getenv("MONGO_DB_URL", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5336023580").split()))
BOT_VER = "0.1.0@main"
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID", ""))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5356564375").split()))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/arsyabot/pyrobot")
BRANCH = getenv("BRANCH", "main")
