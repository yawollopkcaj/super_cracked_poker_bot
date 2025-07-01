import argparse
from agents.rule_based import RuleBasedBot
from envs.two_player_toy_env import ToyPokerEnv

def simulate_hands(num_hands, log_dir):
    bot1 = RuleBasedBot(name="Bot_A")
    bot2 = RuleBasedBot(name="Bot_B")

    env = ToyPokerEnv([bot1, bot2], log_dir=log_dir)

    for i in range(num_hands):
        env.run_hand(log=True)
        if (i + 1) % 100 == 0:
            print(f"Simulated {i + 1} hands")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=1000, help="Number of hands to simulate")
    parser.add_argument("--log_dir", type=str, default="data/logs", help="Directory to store logs")
    args = parser.parse_args()

    simulate_hands(args.n, args.log_dir)