from ..request import Requests
from .housingApi import HousingAPI

class Housing:
    """### Retrieve the housing data of specified player or house."""
    requests = Requests

    def __init__(self, house: str = None, player_name: str = None) -> None:
        self.house: str = house
        self.player_name: str = player_name
        self.housing_api = HousingAPI()

    @property
    def active(self) -> list[dict]:
        """The current active public houses."""
        return self.housing_api.get_active()

    @property
    def house(self) -> dict:
        """The data of specified house."""
        return self.housing_api.get_house(self.house)
    
    @property
    def house(self) -> list[dict]:
        """The data of specified player's houses."""
        return self.housing_api.get_houses(self.player_name)