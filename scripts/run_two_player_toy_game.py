from agents.rule_based import RuleBasedBot
from envs.two_player_toy_env import ToyPokerEnv

if __name__ == "__main__":
    bot1 = RuleBasedBot(name="Bot_A")
    bot2 = RuleBasedBot(name="Bot_B")

    env = ToyPokerEnv([bot1, bot2])

    num_hands = 10  # run multiple hands to collect logs
    for _ in range(num_hands):
        env.run_hand(log=True)
