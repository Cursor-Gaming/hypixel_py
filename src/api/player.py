from ..request import Requests
from .playerApi import PlayerAPI

class Player:
    """### Information about a specified player or players.
    
    **parameters**:
            player_name: str ; Name of a player."""

    requests = Requests

    def __init__(self, player_name: str):
        self.player_name = player_name
        self.player_api = PlayerAPI()

    @property
    def player(self) -> dict:
        """### Gets a Player's information by name."""
        return self.player_api.get_player(self.player_name)

    @property
    def recentgames(self) -> list[dict]:
        """### Gets the recently played games of a specific player."""
        return self.player_api.get_recentgames(self.player_name)

    @property
    def status(self) -> dict:
        """The current online status of a specific player."""
        return self.player_api.get_status(self.player_name)