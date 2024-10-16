from ..request import Requests

class GuildAPI:
    """### Retrieve a Guild by a player, ID, or name."""
    BASE_URL = "https://api.hypixel.net/v2"
    requests = Requests

    def __init__(self):
        pass
    
    def get_guild(self, guild_id: str = None, player_name: str = None, guild_name: str = None) -> dict:
        """### Gets the data of specified guild
        
        **parameters**:
                guild_id: str ; (optional) the ID of the Guild.
                player_name: str ; (optional) a Guild member's name.
                guild_name: str ; (optional) the name of the Guild."""
        url = f"{self.BASE_URL}/guild"
        params = {}
        if guild_id != None:
            params = {
                "id": guild_id
            }
        elif player_name != None:
            params = {
                "player": player_name
            }
        elif guild_name != None:
            params = {
                "name": guild_name
            }
        return self.requests.get_data(url, params)['guild']