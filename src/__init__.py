"""
# Hypixel API for Python.

Unofficial module written in Python for Python is intended to be used to interact with [Hypixel's public API](https://api.hypixel.net")
in an easier way.

When using the module, you will still recieve the information directly from the Hypixel's API, and the data
will be formated in the way Hypixel formated their responses.

note: the API key used in the documentation is only an example, and it should be specified in your project
also, do not share your API key with anyone for obvious privacy reasons.
Make sure your project complies with [Hypixel's API policy](https://developers.hypixel.net/policies) and [TOS](https://hypixel.net/tos).


## Usage:


Start with:
        ```python
        import hypixel_py
        hypixel_py.set_api_key(YOUR_API_KEY_GOES_HERE_012345678900)
        ```
Fetch player information:
        ```python
        player_data = hypixel_py.Player("...")
        general = player_data.player
        recentgames = player_data.recentgames
        status = player_data.status
        ```
        or:
        ```python
        player_api = hypixel_py.PlayerAPI()
        general = player_api.get_player(player_name = "...")
        recentgames = player_api.get_recentgames(player_name = "...")
        status = player_api.get_status(player_name = "...")
        ```

The module works similarly with all other categories of information.
It always follows the ``hypixel_py.Category(Information = "Your information").WhatYouWant`` or ``hypixel_py.Category().get_WhatYouWant(information = "Your information")``.
For every category, you can use either methods. The categories are from the [Hypixel API documentation](https://api.hypixel.net) like [Player Data](https://api.hypixel.net/#tag/Player-Data), [Guild Information](https://api.hypixel.net/#tag/Player-Data/paths/~1v2~1guild/get),
[Resources](https://api.hypixel.net/#tag/Resources), [Skyblock](https://api.hypixel.net/#tag/SkyBlock), [Housing](https://api.hypixel.net/#tag/Housing) and [Other](https://api.hypixel.net/#tag/Other). Every endpoint in the [documentation](https://api.hypixel.net) is included
in this module.
For every class and function in the module, I've written descriptions about what they do, what parameters they take,
and what they give as an output.
"""

from . import api, errors
from .request import Requests
from .api.guild import Guild
from .api.guildApi import GuildAPI
from .api.housing import Housing
from .api.housingApi import HousingAPI
from .api.player import Player
from .api.playerApi import PlayerAPI
from .api.resources import Resources
from .api.resourcesApi import ResourcesAPI
from .api.skyblock import Skyblock
from .api.skyblockApi import SkyblockAPI

__name__ = "hypixel_py"
__version__ = "1.0"

def set_api_key(api_key: str) -> None:
    """### Function used to set your API key for your application.

    **parameters**:
        api_key: str ; your specified API key."""

    api.set_api_key(api_key)
    Requests.api_key = api_key
