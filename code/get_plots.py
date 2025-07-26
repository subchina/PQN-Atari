" Replace ??? with corresponding learning and target environment (e.g. Space Invaders and Breakout)"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_from_logged_returns(csv_path):
    df = pd.read_csv(csv_path)

    x = df["Step"]

    # Base
    base_mean = df["Group: ??? Base - test/returned_episode_returns"]
    base_min = df["Group: ??? Base - test/returned_episode_returns__MIN"]
    base_max = df["Group: ??? Base - test/returned_episode_returns__MAX"]
    base_std = (base_max - base_min) / 2

    # Transfer
    transfer_mean = df["Group: ??? Transfer from ??? - test/returned_episode_returns"]
    transfer_min = df["Group: ??? Transfer from ??? - test/returned_episode_returns__MIN"]
    transfer_max = df["Group: ??? Transfer from ??? - test/returned_episode_returns__MAX"]
    transfer_std = (transfer_max - transfer_min) / 2

    # Plot
    plt.figure(figsize=(10, 6))
    
    plt.plot(x, base_mean, label="Baseline", color="blue")
    plt.fill_between(x, base_mean - base_std, base_mean + base_std, color="blue", alpha=0.3)

    plt.plot(x, transfer_mean, label="Transfer from Demon Attack", color="green")
    plt.fill_between(x, transfer_mean - transfer_std, transfer_mean + transfer_std, color="green", alpha=0.3)

    plt.xlabel("Environment Steps")
    plt.ylabel("Episode Return")
    plt.title("???: Baseline vs Transfer from ???")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

plot_from_logged_returns(".csv") # CSV name
