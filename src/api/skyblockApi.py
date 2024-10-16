from ..request import Requests

class SkyblockAPI:
    """Returns information about Hypixel Skyblock"""

    BASE_URL = "https://api.hypixel.net/v2/skyblock"
    requests = Requests

    def __init__(self):
        pass

    def get_collections(self) -> dict:
        """collections"""
        url = f"{self.BASE_URL}/collections"
        return self.requests.get(url)['collections']
    
    def get_skills(self) -> dict:
        """skills"""
        url = f"{self.BASE_URL}/skills"
        return self.requests.get(url)['skills']
    
    def get_items(self) -> list[dict]:
        """items"""
        url = f"{self.BASE_URL}/items"
        return self.requests.get(url)['items']
    
    def get_mayor(self) -> dict:
        """mayor"""
        url = f"https://api.hypixel.net/v2/resouces/skyblock/election"
        return self.requests.get(url)['mayor']
    
    def get_election(self) -> dict:
        """election"""
        url = f"https://api.hypixel.net/v2/resouces/skyblock/election"
        return self.requests.get(url)['current']
    
    def get_news(self) -> list[dict]:
        """news?"""
        url = f"{self.BASE_URL}/news"
        return Requests.get_data(url)['items']

    def get_auction(self, auction = None, player_name = None, profile = None) -> list[dict]:
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
        url = f"{self.BASE_URL}/auctions"
        data = self.requests.get(url)
        return {
            "page": data['page'],
            "totalPages": data['totalPages'],
            "totalAuctions": data['totalAuctions'],
            "auctions": data['auctions']
        }

    def get_auctions_ended(self) -> dict:
        url = f"{self.BASE_URL}/auctions_ended"
        return self.requests.get(url)
    
    def get_bazaar(self) -> dict:
        url = f"{self.BASE_URL}/bazaar"
        return self.requests.get(url)['products']
    
    def get_profile(self, profile: str) -> dict:
        url = f"{self.BASE_URL}/profile"
        params = {
            "profile": profile
        }
        return self.requests.get_data(url, params)['profile']
    
    def get_profiles(self, player_name: str) -> list[dict]:
        url = f"{self.BASE_URL}/profiles"
        params = {
            "uuid": player_name
        }
        return self.requests.get_data(url, params)['profiles']
    
    def get_museum(self, profile: str) -> dict:
        url = f"{self.BASE_URL}/museum"
        params = {
            "uuid": profile
        }
        return self.requests.get_data(url, params)['profile']
    
    def get_garden(self, profile: str) -> dict:
        url = f"{self.BASE_URL}/garden"
        params = {
            "uuid": profile
        }
        return self.requests.get_data(url, params)['garden']
    
    def get_bingo(self, player_name: str) -> list[dict]:
        url = f"{self.BASE_URL}/bingo"
        params = {
            "uuid": player_name
        }
        return self.requests.get_data(url, params)['events']
    
    def get_firesales(self) -> list[dict]:
        url = f"{self.BASE_URL}/firesales"
        return self.requests.get(url)['sales']