"""Contains the request function that gets data from the given website"""

import requests
from .errors import RequestError

class Requests:
    """### Contains the functions that get players' data.
    Your API key is given to this class, but it's only used by the get_data
    function."""

    api_key = ""

    @classmethod
    def get_uuid(cls, player_name: str) -> str:
        """### Gets the UUID of said player.
        
        **parameters**:
                player_name: str ; players' username.
        **output**:
                UUID of said player.
        This function is only used by the hypixel_py module and should not be used outside of it.
            except if you want to get literally only someone's Minecraft Account's UUID"""

        url = f"https://api.mojang.com/users/profiles/minecraft/{player_name}"
        response = requests.get(url)
        if response.status_code != 200:
            if response.status_code == 204:
                raise RequestError(f"No content. ({response.status_code})")
            if response.status_code == 400:
                raise RequestError(f"Invalid/bad request.({response.status_code})")
            if response.status_code == 404:
                raise RequestError(f"Player not found. ({response.status_code})")
            else:
                raise RequestError(response.status_code)
        return response.json()['id']

    @classmethod
    def get_data(cls, url: str, params: dict = None) -> dict | list[dict]:
        """### Makes a get HTTP request to the given URL with the given params.
        
        **parameters**:
                url: str ; Specified URL where the get requests gets information from.
                params: dict[str, Any] ; Parameters of that URL; ie: "key", "player_name". 
        **output**:
                Response of the get request as a dict or a list[dict].
        This function is only used by the hypixel_py module and should not be used outside of it."""

        params = params or {}
        params['key'] = cls.api_key
        player_name = params.get('uuid')
        if player_name != None:
            params['uuid'] = cls.get_uuid(player_name)
        response = requests.get(url, params=params)
        if response.status_code != 200:
            if response.status_code == 400:
                raise RequestError(f"Invalid API key, try again with a valid one. ({response.status_code})")
            if response.status_code == 403:
                raise RequestError(f"Invalid data. ({response.status_code})")
            if response.status_code == 422:
                raise RequestError(f"Not all required data is given. ({response.status_code})")
            if response.status_code == 429:
                raise RequestError(f"Requesting is on cooldown, try again later. ({response.status_code})")
            else:
                raise RequestError(f"({response.status_code})")
        return response.json()

    @staticmethod
    def get(*args, **kwargs):
        """### Makes a get HTTP request to the given URL with the given params, used if no API key is neccessary"""
        response = requests.get(*args, **kwargs)
        response.raise_for_status()
        return response.json()