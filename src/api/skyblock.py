from ..request import Requests
from .skyblockApi import SkyblockAPI

class Skyblock:
    """### Retrieve the Skyblock data of specified player or auction."""
    requests = Requests

    def __init__(self, player_name: str = None, auction: str = None, profile: str = None):
        self.player_name: str = player_name
        self.auction: str = auction
        self.profile: str = profile
        self.skyblock_api = SkyblockAPI()

    @property
    def collections(self) -> dict:
        """### Information regarding collections."""
        return self.skyblock_api.get_collections()
    
    @property
    def skills(self) -> dict:
        """### Information regarding skills."""
        return self.skyblock_api.get_skills()
    
    @property
    def items(self) -> list[dict]:
        """### Information regarding items."""
        return self.skyblock_api.get_items()
    
    @property
    def mayor(self) -> dict:
        """### Information regarding the current mayor."""
        return self.skyblock_api.get_mayor()

    @property
    def election(self) -> dict:
        """### Information regarding the ongoing election."""
        return self.skyblock_api.get_election()

    @property
    def news(self) -> list[dict]:
        """### Information regarding the news. (not sure what that means)"""
        return self.skyblock_api.get_news()
    
    @property
    def auction(self) -> list[dict]:
        """### Returns the auctions selected by the provided query."""
        if self.auction != None:
            return self.skyblock_api.get_auction(auction = self.auction)
        elif self.player_name != None:
            return self.skyblock_api.get_auction(player_name = self.player_name)
        elif self.profile != None:
            return self.skyblock_api.get_auction(profile = self.profile)
        
    @property
    def auctions(self) -> dict:
        """### Returns the ongoing auctions."""
        return self.skyblock_api.get_auctions()
    
    @property
    def auctions_ended(self) -> dict:
        """### Returns the ended auctions."""
        return self.skyblock_api.get_auctions_ended()
    
    @property
    def bazaar(self) -> dict:
        """### Information regarding the bazaar."""
        return self.skyblock_api.get_bazaar()
    
    @property
    def profile(self) -> dict:
        """Information regarding the profile."""
        return self.skyblock_api.get_profile(profile = self.profile)
    
    @property
    def profiles(self) -> list[dict]:
        """### Information regarding the player's profiles."""
        return self.skyblock_api.get_profiles(player_name = self.player_name)
    
    @property
    def museum(self) -> dict:
        """### Information regarding the player's museum."""
        return self.skyblock_api.get_museum(profile = self.profile)
    
    @property
    def garden(self) -> dict:
        """### Information regarding the player's garden."""
        return self.skyblock_api.get_garden(profile = self.profile)
    
    @property
    def bingo(self) -> list[dict]:
        """### Information regarding the player's bingo."""
        return self.skyblock_api.get_bingo(player_name = self.player_name)
    
    @property
    def firesales(self) -> list[dict]:
        """### Information regarding the ongoing firesales."""
        return self.skyblock_api.get_firesales()