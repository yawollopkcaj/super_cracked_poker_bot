import os
import json
import pandas as pd
import matplotlib.pyplot as plt

LOG_DIR = "data/logs"

def load_logs(log_dir):
    data = []
    for filename in os.listdir(log_dir):
        if filename.endswith(".json"):
            with open(os.path.join(log_dir, filename)) as f:
                hand = json.load(f)
                for player in hand["players"]:
                    data.append({
                        "timestamp": hand["timestamp"],
                        "player": player,
                        "opponent": [p for p in hand["players"] if p != player][0],
                        "hand_strength": hand["hand_strengths"][player],
                        "action": hand["actions"][player],
                        "won": 1 if hand["winner"] == player else 0
                    })
    return pd.DataFrame(data)

def plot_action_distribution(df):
    action_counts = df.groupby("player")["action"].value_counts(normalize=True).unstack()
    action_counts.plot(kind="bar", stacked=True)
    plt.title("Action Distribution per Player")
    plt.ylabel("Proportion")
    plt.tight_layout()
    plt.show()

def plot_win_rates(df):
    win_rates = df.groupby("player")["won"].mean()
    win_rates.plot(kind="bar", color="green")
    plt.title("Win Rate per Player")
    plt.ylabel("Win %")
    plt.tight_layout()
    plt.show()

def plot_bluff_rate(df, threshold=0.4):
    df["is_bluff"] = (df["action"] == "raise") & (df["hand_strength"] < threshold)
    bluff_rate = df.groupby("player")["is_bluff"].mean()
    bluff_rate.plot(kind="bar", color="red")
    plt.title(f"Bluff Rate (Raise with hand_strength < {threshold})")
    plt.ylabel("Bluff %")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = load_logs(LOG_DIR)

    print(f"Loaded {len(df)//2} hands from {LOG_DIR}")
    print(df.head())

    plot_win_rates(df)
    plot_action_distribution(df)
    plot_bluff_rate(df)