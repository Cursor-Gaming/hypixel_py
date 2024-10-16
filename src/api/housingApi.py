from ..request import Requests

class HousingAPI:
    """### Retrieve the housing data of specified player or house."""
    BASE_URL = "https://api.hypixel.net/v2/housing"
    requests = Requests

    def __init__(self) -> None:
        pass

    def get_active(self) -> list[dict]:
        """### The current active public houses."""
        url = f"{self.BASE_URL}/active"
        return self.requests.get_data(url)
    
    def get_house(self, house: str) -> dict:
        """### The data of specified house.
        
        **parameters**:
                house: str ; the ID of the house."""
        url = f"{self.BASE_URL}/house"
        params = {
            "house": house
        }
        return self.requests.get_data(url, params)
    
    def get_houses(self, player_name: str) -> list[dict]:
        """### The data of specified player's houses.
        
        **parameters**:
                player_name: str ; the name of the player."""
        url = f"{self.BASE_URL}/houses"
        params = {
            "uuid": player_name
        }
        return self.requests.get_data(url, params)