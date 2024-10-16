from ..request import Requests
from .skyblockApi import SkyblockAPI

class Skyblock:

    requests = Requests

    def __init__(self, player_name: str = None, auction: str = None, profile: str = None):
        self.player_name: str = player_name
        self.auction: str = auction
        self.profile: str = profile
        self.skyblock_api = SkyblockAPI()

    @property
    def collections(self) -> dict:
        return self.skyblock_api.get_collections()
    
    @property
    def skills(self) -> dict:
        return self.skyblock_api.get_skills()
    
    @property
    def items(self) -> list[dict]:
        return self.skyblock_api.get_items()
    
    @property
    def mayor(self) -> dict:
        return self.skyblock_api.get_mayor()

    @property
    def election(self) -> dict:
        return self.skyblock_api.get_election()

    @property
    def news(self) -> list[dict]:
        return self.skyblock_api.get_news()
    
    @property
    def auction(self) -> list[dict]:
        if self.auction != None:
            return self.skyblock_api.get_auction(auction=self.auction)
        elif self.player_name != None:
            return self.skyblock_api.get_auction(player_name=self.player_name)
        elif self.profile != None:
            return self.skyblock_api.get_auction(profile=self.profile)
        
    @property
    def auctions(self) -> dict:
        return self.skyblock_api.get_auctions()
    
    @property
    def auctions_ended(self) -> dict:
        return self.skyblock_api.get_auctions_ended()
    
    @property
    def bazaar(self) -> dict:
        return self.skyblock_api.get_bazaar()
    
    @property
    def profile(self) -> dict:
        return self.skyblock_api.get_profile(profile = self.profile)
    
    @property
    def profiles(self) -> list[dict]:
        return self.skyblock_api.get_profiles(player_name = self.player_name)
    
    @property
    def museum(self) -> dict:
        return self.skyblock_api.get_museum(profile = self.profile)
    
    @property
    def garden(self) -> dict:
        return self.skyblock_api.get_garden(profile = self.profile)
    
    @property
    def bingo(self) -> list[dict]:
        return self.skyblock_api.get_bingo(player_name = self.player_name)
    
    @property
    def firesales(self) -> list[dict]:
        return self.skyblock_api.get_firesales()