from ..classes.guild import Guild
from .guildApi import GuildAPI
from ..classes.player import Player
from .playerApi import PlayerAPI
from ..classes.resources import Resources
from .resourcesApi import ResourcesAPI
from ..classes.skyblock import Skyblock
from .skyblockApi import SkyblockAPI

api_key = [""]

def set_api_key(api_key: str) -> None:
    """### **Function used to set your API key for your application.**

    **parameters**:
        api_key: str ; your specified API key
    This function is only supposed to be used by the Hypixel_py module"""
    Guild.requests.api_key = api_key
    GuildAPI.requests.api_key = api_key
    Player.requests.api_key = api_key
    PlayerAPI.requests.api_key = api_key
    Resources.requests.api_key = api_key
    ResourcesAPI.requests.api_key = api_key
    Skyblock.requests.api_key = api_key
    SkyblockAPI.requests.api_key = api_key