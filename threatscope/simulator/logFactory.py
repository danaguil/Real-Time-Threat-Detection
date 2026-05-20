# logFactory.py
# This module defines a factory for generating log entries based on different strategies, including various attack patterns and normal traffic. The factory uses a weighted random selection to simulate realistic log generation, where normal traffic is more common than attacks.

import random

from logStrategy import (
    BruteForceStrategy, 
    SQLInjectionStrategy, 
    NormalTrafficStrategy
)

# We can use the Strategy Pattern to create different log generation strategies for various attack types and normal traffic. This allows us to easily extend our log generator with new attack patterns in the future without modifying existing code.
class LogStrategyFactory:
    """
    Picks a strategy based on weighted probability.
    Normal traffic is most common — just like the real world.
    """
    POOL = [
        BruteForceStrategy,    # 3x — most common attack
        BruteForceStrategy,
        BruteForceStrategy,
        SQLInjectionStrategy,  # 2x
        SQLInjectionStrategy,
        NormalTrafficStrategy, # 4x — normal traffic dominates
        NormalTrafficStrategy,
        NormalTrafficStrategy,
        NormalTrafficStrategy,
    ]


    @staticmethod
    def get_strategy():
        return random.choice(LogStrategyFactory.POOL)()