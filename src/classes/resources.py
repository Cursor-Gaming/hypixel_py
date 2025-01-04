from ..request import Requests
from ..api.resourcesApi import ResourcesAPI

class Resources:
    """Returns information about Hypixel."""

    BASE_URL = "https://api.hypixel.net/v2/resources"
    requests = Requests

    def __init__(self):
        self.resources_api = ResourcesAPI()

    @property
    def games(self) -> dict:
        """Returns information about Hypixel Games."""
        return self.resources_api.get_games()

    @property
    def achievements(self) -> dict:
        """Returns information about Hypixel Achievements."""
        return self.resources_api.get_achievements()

    @property
    def challenges(self) -> dict:
        """Returns information about Hypixel Challenges"""
        return self.resources_api.get_challenges()

    @property
    def quests(self) -> dict:
        """Returns information about Hypixel Quests"""
        return self.resources_api.get_quests()

    @property
    def guild_achievement(self) -> dict:
        """Returns information about Hypixel Guild Achievemnts"""
        return self.resources_api.get_guild_achievement()
