# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
import logging
import sys
import time
from datetime import datetime
from logging.handlers import RotatingFileHandler
from typing import Any, Dict

from aiohttp import ClientSession
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from gpytranslate import Translator
from pyrogram import Client
from pyrogram.types import *
from pytgcalls import GroupCallFactory

from config import (
    API_HASH,
    API_ID,
    BOT_TOKEN,
    BOTLOG_CHATID,
    DB_URL,
    STRING_SESSION,
    SUDO_USERS,
)

LOOP = asyncio.get_event_loop_policy().get_event_loop()
trl = Translator()
aiosession = ClientSession()
CMD_HELP = {}
scheduler = AsyncIOScheduler()
StartTime = time.time()
START_TIME = datetime.now()
TEMP_SETTINGS: Dict[Any, Any] = {}
TEMP_SETTINGS["PM_COUNT"] = {}
TEMP_SETTINGS["PM_LAST_MSG"] = {}

LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("asyncio").setLevel(logging.CRITICAL)
logging.getLogger("pytgcalls").setLevel(logging.WARNING)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.client").setLevel(logging.WARNING)
logging.getLogger("pyrogram.syncer").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.session.auth").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.session.session").setLevel(logging.CRITICAL)
LOGS = logging.getLogger(__name__)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


API_ID = API_ID
API_HASH = API_HASH
BOT_TOKEN = BOT_TOKEN
SUDO_USERS = SUDO_USERS
DB_URL = DB_URL

if not STRING_SESSION1:
    LOGGER(__name__).error("No String Session Found! Exiting!")
    sys.exit()

if not API_ID:
    LOGGER(__name__).error("No API_ID Found! Exiting!")
    sys.exit()

if not API_HASH:
    LOGGER(__name__).error("No API_HASH Found! Exiting!")
    sys.exit()

if not BOT_TOKEN:
    LOGGER(__name__).error("No BOT_TOKEN Found! Exiting!")
    sys.exit()

if BOTLOG_CHATID:
    BOTLOG_CHATID = BOTLOG_CHATID
else:
    BOTLOG_CHATID = "me"


app = (
    Client(
        name="app",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION,
        plugins=dict(root="PunyaAlby/modules"),
    )
    if STRING_SESSION
    else None
)

gbot = Client(":memory:", API_ID, API_HASH, bot_token=BOT_TOKEN)


for app:
    if not hasattr(app, "group_call"):
        setattr(app, "group_call", GroupCallFactory(bot).get_group_call())
