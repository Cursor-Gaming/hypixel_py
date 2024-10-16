from ..request import Requests

class PlayerAPI:
    """### Information about a specified player or players."""

    BASE_URL = "https://api.hypixel.net/v2"
    requests = Requests

    def __init__(self):
        pass

    def get_player(self, player_name: str) -> dict:
        """### Gets a Player's information by name.

        **parameters**:
                player_name: str ; Name of a player.
        **output**:
                Dictionary"""

        url = f"{self.BASE_URL}/player"
        params = {
            "uuid": player_name
        }
        return self.requests.get_data(url, params)['player']
    
    def get_recentgames(self, player_name: str) -> list[dict]:
        """### Gets the recently played games of a specific player.

        **parameters**:
                player_name: str ; Name of a player.
        **output**:
                Dictionary"""

        url = f"{self.BASE_URL}/recentgames"
        params = {
            "uuid": player_name
        }
        return self.requests.get_data(url, params)['games']
    
    def get_status(self, player_name: str) -> dict:
        """The current online status of a specific player.
        
        parameters:
                player_name: str ; Name of a player.
        output:
                Dictionary"""
        
        url = f"{self.BASE_URL}/status"
        params = {
            "uuid":player_name
        }
        return self.requests.get_data(url, params)