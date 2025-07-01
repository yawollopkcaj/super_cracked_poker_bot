import random
import json
import os
from datetime import datetime

class ToyPokerEnv:
    def __init__(self, agents, log_dir="data/logs"):
        self.agents = agents  # list of two agent objects
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)
        self.reset()

    def reset(self):
        self.hand_strengths = {agent.name: random.random() for agent in self.agents}
        self.actions = {}
        self.pot = 2  # 1 blind each to start

    def run_hand(self, log=True):
        self.reset()
        print(f"Dealing hand...\n")

        for agent in self.agents:
            state = {"hand_strength": self.hand_strengths[agent.name]}
            action = agent.act(state)
            self.actions[agent.name] = action
            print(f"{agent.name} ({round(state['hand_strength'], 2)}) -> {action}")

        winner = self.resolve_showdown()

        if log:
            self.log_hand(winner)

        self.resolve_showdown()

    def resolve_showdown(self):
        a1, a2 = self.agents
        act1, act2 = self.actions[a1.name], self.actions[a2.name]

        # Fold logic
        if act1 == "fold":
            winner = a2.name
        elif act2 == "fold":
            winner = a1.name
        else:
            # Compare hand strength
            winner = a1.name if self.hand_strengths[a1.name] > self.hand_strengths[a2.name] else a2.name

        print(f"\nWinner: {winner} 🏆\n{'-'*40}")
        return winner
    
    def log_hand(self, winner):
        log_data = {
            "timestamp": datetime.now().isoformat(),
            "players": [agent.name for agent in self.agents],
            "hand_strengths": self.hand_strengths,
            "actions": self.actions,
            "winner": winner,
        }

        filename = os.path.join(self.log_dir, f"hand_{datetime.now().strftime('%Y%m%d_%H%M%S%f')}.json")
        with open(filename, "w") as f:
            json.dump(log_data, f, indent=2)
