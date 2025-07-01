import random

class RuleBasedBot:
    def __init__(self, name="RuleBot"):
        self.name = name

    def act(self, state):
        """
        Simple logic:
        - Fold if hand is weak
        - Call with medium strength
        - Raise if hand is strong
        """
        hand_strength = state.get("hand_strength", random.random())
        if hand_strength < 0.3:
            return "fold"
        elif hand_strength < 0.7:
            return "call"
        else:
            return "raise"
