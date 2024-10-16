from ..request import Requests

class SkyblockAPI:
    """### Returns information about Hypixel Skyblock"""

    BASE_URL = "https://api.hypixel.net/v2/skyblock"
    requests = Requests

    def __init__(self):
        pass

    def get_collections(self) -> dict:
        """### Information regarding collections."""
        url = f"{self.BASE_URL}/collections"
        return self.requests.get(url)['collections']
    
    def get_skills(self) -> dict:
        """### Information regarding skills."""
        url = f"{self.BASE_URL}/skills"
        return self.requests.get(url)['skills']
    
    def get_items(self) -> list[dict]:
        """### Information regarding items."""
        url = f"{self.BASE_URL}/items"
        return self.requests.get(url)['items']
    
    def get_mayor(self) -> dict:
        """### Information regarding the current mayor."""
        url = f"https://api.hypixel.net/v2/resouces/skyblock/election"
        return self.requests.get(url)['mayor']
    
    def get_election(self) -> dict:
        """Information regarding the ongoing election."""
        url = f"https://api.hypixel.net/v2/resouces/skyblock/election"
        return self.requests.get(url)['current']
    
    def get_news(self) -> list[dict]:
        """### Information regarding the news. (not sure what that means)"""
        url = f"{self.BASE_URL}/news"
        return Requests.get_data(url)['items']

    def get_auction(self, auction = None, player_name = None, profile = None) -> list[dict]:
        """### Returns the auctions selected by the provided query.
        
        **parameters**:
                auction: str (optional) ; the ID of the auction.
                player_name: str (optional) ; the name of the player.
                profile: str (optional) ; the ID of the profile."""
        url = f"{self.BASE_URL}/auction"
        params = {}
        if auction != None:
            params = {
                "uuid": auction
            }
        elif player_name != None:
            params = {
                "player": player_name
            }
        elif profile != None:
            params = {
                "profile": profile
            }
        return self.requests.get_data(url, params)['auction']

    def get_auctions(self) -> list[dict]:
        """### Returns the ongoing auctions."""
        url = f"{self.BASE_URL}/auctions"
        data = self.requests.get(url)
        return {
            "page": data['page'],
            "totalPages": data['totalPages'],
            "totalAuctions": data['totalAuctions'],
            "auctions": data['auctions']
        }

    def get_auctions_ended(self) -> dict:
        """### Returns the ended auctions."""
        url = f"{self.BASE_URL}/auctions_ended"
        return self.requests.get(url)
    
    def get_bazaar(self) -> dict:
        """### Information regarding the bazaar."""
        url = f"{self.BASE_URL}/bazaar"
        return self.requests.get(url)['products']
    
    def get_profile(self, profile: str) -> dict:
        """### Information regarding the profile.
        
        **parameters**:
                profile: str ; the ID of the profile."""
        url = f"{self.BASE_URL}/profile"
        params = {
            "profile": profile
        }
        return self.requests.get_data(url, params)['profile']
    
    def get_profiles(self, player_name: str) -> list[dict]:
        """### Information regarding the player's profiles.
        
        **parameters**:
                player_name: str ; the name of the player."""
        url = f"{self.BASE_URL}/profiles"
        params = {
            "uuid": player_name
        }
        return self.requests.get_data(url, params)['profiles']
    
    def get_museum(self, profile: str) -> dict:
        """### Information regarding the player's museum.
        
        **parameters**:
                profile: str ; the ID of the profile."""
        url = f"{self.BASE_URL}/museum"
        params = {
            "uuid": profile
        }
        return self.requests.get_data(url, params)['profile']
    
    def get_garden(self, profile: str) -> dict:
        """### Information regarding the player's garden.
        
        **parameters**:
                profile: str ; the ID of the profile."""
        url = f"{self.BASE_URL}/garden"
        params = {
            "uuid": profile
        }
        return self.requests.get_data(url, params)['garden']
    
    def get_bingo(self, player_name: str) -> list[dict]:
        """### Information regarding the player's bingo.
        
        **parameters**:
                player_name: str ; the name of the player."""
        url = f"{self.BASE_URL}/bingo"
        params = {
            "uuid": player_name
        }
        return self.requests.get_data(url, params)['events']
    
    def get_firesales(self) -> list[dict]:
        """### Information regarding the ongoing firesales."""
        url = f"{self.BASE_URL}/firesales"
        return self.requests.get(url)['sales']