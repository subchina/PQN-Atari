import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_from_logged_returns(csv_path):
    df = pd.read_csv(csv_path)

    x = df["Step"]

    # Base
    base_mean = df["Group: Space Invaders Base - test/returned_episode_returns"]
    base_min = df["Group: Space Invaders Base - test/returned_episode_returns__MIN"]
    base_max = df["Group: Space Invaders Base - test/returned_episode_returns__MAX"]
    base_std = (base_max - base_min) / 2

    # Transfer
    transfer_mean = df["Group: Space Invaders Transfer from Demon Attack - test/returned_episode_returns"]
    transfer_min = df["Group: Space Invaders Transfer from Demon Attack - test/returned_episode_returns__MIN"]
    transfer_max = df["Group: Space Invaders Transfer from Demon Attack - test/returned_episode_returns__MAX"]
    transfer_std = (transfer_max - transfer_min) / 2

    # Plot
    plt.figure(figsize=(10, 6))
    
    plt.plot(x, base_mean, label="Baseline", color="blue")
    plt.fill_between(x, base_mean - base_std, base_mean + base_std, color="blue", alpha=0.3)

    plt.plot(x, transfer_mean, label="Transfer from Demon Attack", color="green")
    plt.fill_between(x, transfer_mean - transfer_std, transfer_mean + transfer_std, color="green", alpha=0.3)

    plt.xlabel("Environment Steps")
    plt.ylabel("Episode Return")
    plt.title("Space Invaders: Baseline vs Transfer from Demon Attack; Greedy Policy")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Example usage:
plot_from_logged_returns("wandb_export_2025-07-26T03_35_48.526+02_00 sit.csv")
