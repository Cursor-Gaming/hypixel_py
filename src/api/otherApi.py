from ..request import Requests

class OtherAPI:
    """### Class of all other endpoints of the Hypixel API"""
    BASE_URL = "https://api.hypixel.net/v2"
    requests = Requests

    def __init__(self) -> None:
        pass

    def get_boosters(self) -> dict:
        """### Gets all of the currently active network boosters."""
        url = f"{self.BASE_URL}/boosters"
        data = self.requests.get_data(url)
        return {
            "boosters": data['boosters'],
            "boosterState": data['boosterState']
        }
    
    def get_counts(self) -> dict:
        """### Gets the current player count on the server."""
        url = f"{self.BASE_URL}/counts"
        data = self.requests.get_data(url)
        return {
            "playerCount": data['playerCount'],
            "games": data['games']
        }
    
    def get_leaderboards(self) -> dict:
        """### Gets the current leaderboards."""
        url = f"{self.BASE_URL}/counts"
        return self.requests.get_data(url)['leaderboards']
    
    def get_punishmentstatistics(self) -> dict:
        """### Gets the current punishment statistics."""
        url = f"{self.BASE_URL}/punishmentstatistics"
        data = self.requests.get_data(url)
        return {
            "watchdog_lastMinute": data['watchdog_lastMinute'],
            "staff_rollingDaily": data['staff_rollingDaily'],
            "watchdog_total": data['watchdog_total'],
            "watchdog_rollingDaily": data['watchdog_rollingDaily'],
            "staff_total": data['staff_total']
        }