from ..request import Requests
from typing import overload

class Guild:
    """### Retrieve a Guild by a player, ID, or name."""
    requests = Requests
    BASE_URL = "https://api.hypixel.net/v2"

    @overload
    def __init__(self, guild_id: str):
        self.params = {
            "id": guild_id
        }

    @overload
    def __init__(self, player_name: str):
        self.params = {
            "player": player_name
        }

    @overload
    def __init__(self, guild_name: str):
        self.params = {
            "name": guild_name
        }

    @property
    def guild(self):
        """### Gets the data of specified guild
        
        **parameters**:
                guild_id: str ; (optional) the ID of the Guild.
                player_name: str ; (optional) a Guild member's name.
                guild_name: str ; (optional) the name of the Guild."""
        url = f"{self.BASE_URL}/guild"
        return self.requests.get_data(url, self.params)['guild']