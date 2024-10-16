from ..request import Requests

class ResourcesAPI:
    """Returns information about Hypixel."""

    BASE_URL = "https://api.hypixel.net/v2/resources"
    requests = Requests

    def __init__(self):
        pass

    def get_games(self) -> dict:
        """Returns information about Hypixel Games."""
        url = f"{self.BASE_URL}/games"
        return Requests.get(url)['games']

    def get_achievements(self) -> dict:
        """Returns information about Hypixel Achievements."""
        url = f"{self.BASE_URL}/achievements"
        return Requests.get(url)['achievements']

    def get_challenges(self) -> dict:
        """Returns information about Hypixel Challenges"""
        url = f"{self.BASE_URL}/challenges"
        return Requests.get(url)['challenges']

    def get_quests(self) -> dict:
        """Returns information about Hypixel Quests"""
        url = f"{self.BASE_URL}/quests"
        return Requests.get(url)['quests']

    def get_guild_achievement(self) -> dict:
        """Returns information about Hypixel Guild Achievemnts"""
        url = f"{self.BASE_URL}/guilds/achievements"
        data = Requests.get(url)
        return {
            "one_time": data['one_time'],
            "tiered": data['tiered']
            }