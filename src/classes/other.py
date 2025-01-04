from ..request import Requests
from ..api.otherApi import OtherAPI

class Other:
    """### All other endpoints of the Hypixel API"""
    requests = Requests
    other_api = OtherAPI()

    def __init__(self) -> None:
        pass

    @property
    def boosters(self) -> dict:
        """### Gets all of the currently active network boosters."""
        return self.other_api.get_boosters()

    @property
    def counts(self) -> dict:
        """### Gets the current player count on the server."""
        return self.other_api.get_counts()

    @property
    def leaderboards(self) -> dict:
        """### Gets the current leaderboards."""
        return self.other_api.get_leaderboards()

    @property
    def punishmentstatistics(self) -> dict:
        """### Gets the current punishment statistics."""
        return self.other_api.get_punishmentstatistics()