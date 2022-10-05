from .botconfig import BotConfig, BOTDV
from .pmpermitconfig import PmpermitConfig, PMPERMITDV



class Configs(
    BotConfig,
    PmpermitConfig
    ):
    DVLIST = BOTDV + PMPERMITDV
