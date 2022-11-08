import time
import logging 
import platform

import pyrogram
from config import Config
from telegraph import Telegraph
from pyrogram import __version__ as pyrogram_version
from PunyaAlby.core.database import Database
from PunyaAlby.core.helpers import Helpers
from PunyaAlby.core.newpyrogram import Methods






class ClassManager(Config, Helpers, Database, Methods):
    # versions /
    python_version = str(platform.python_version())
    pyrogram_version = str(pyrogram_version)

    # assistant /
    assistant_name = "ALBY"
    assistant_version = "v.0.0.4"

    # userbot /
    userbot_name = "ALBY-PYROBOT"
    userbot_version = "v.0.1.5"

    # containers /
    CMD_HELP = {}

    # owner details /
    owner_name = "ALBY"
    owner_id = 1441342342
    owner_username = "@Punya_Alby"

    # other /
    message_ids = {}
    PIC = "https://telegra.ph/file/508d316cca47fd20c0829.jpg"
    Repo = "https://github.com/bitchlah/pyrobot.git"
    StartTime = time.time()
    utube_object = object
    callback_user = None
    whisper_ids = {}

    # debugging /
    
   
    logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)
    logging.getLogger("pyrogram.session.session").setLevel(logging.WARNING) 
    logging.getLogger("pyrogram.session.internals.msg_id").setLevel(logging.WARNING)
    logging.getLogger("pyrogram.dispatcher").setLevel(logging.WARNING)
    logging.getLogger("pyrogram.connection.connection").setLevel(logging.WARNING)
    log = logging.getLogger()

    # telegraph /
    telegraph = Telegraph()
    telegraph.create_account(short_name=Config.TL_NAME or "ALBY-PYROBOT")
