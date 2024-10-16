from math import sqrt, floor

class Tools:
    """### A class of some tools to use with the Hypixel_py module."""

    def __init__(self) -> None:
        pass

    def get_level_from_exp(self, experience):
        """### Convert player's experience to netowrk level.
        
        **parameters**:
                experience: int | float ; The experience that's converted into network level."""
        BASE = 10000
        GROWTH = 2500
        REVERSE_PQ_PREFIX = -(BASE - 0.5 * GROWTH)/GROWTH
        REVERSE_CONST = REVERSE_PQ_PREFIX * REVERSE_PQ_PREFIX
        GROWTH_DIVIDES_2 = 2/GROWTH
        return floor(1 + REVERSE_PQ_PREFIX) + sqrt(REVERSE_CONST + GROWTH_DIVIDES_2 * experience)