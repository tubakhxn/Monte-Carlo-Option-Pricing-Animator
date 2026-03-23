"""
visualization.py
Animated and static plots for Monte Carlo option pricing.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_convergence(mc_prices, bs_price, n_paths, option_type="call"):
    """
    Animate convergence of Monte Carlo price to Black-Scholes price.
    Args:
        mc_prices (np.ndarray): Array of MC prices as paths increase
        bs_price (float): Analytical Black-Scholes price
        n_paths (int): Total number of paths
        option_type (str): "call" or "put"
    """
    fig, ax = plt.subplots()
    x = np.arange(1, len(mc_prices) + 1)
    line, = ax.plot([], [], lw=2, label="Monte Carlo Price")
    ax.axhline(bs_price, color="red", linestyle="--", label="Black-Scholes Price")
    ax.set_xlim(1, n_paths)
    ax.set_ylim(min(mc_prices.min(), bs_price) * 0.95, max(mc_prices.max(), bs_price) * 1.05)
    ax.set_xlabel("Number of Paths")
    ax.set_ylabel(f"Option Price ({option_type.title()})")
    ax.set_title(f"Convergence of Monte Carlo {option_type.title()} Price")
    ax.legend()

    def update(frame):
        line.set_data(x[:frame+1], mc_prices[:frame+1])
        return line,

    ani = FuncAnimation(fig, update, frames=len(mc_prices), interval=30, blit=True)
    plt.show()


def plot_payoff_distribution(payoffs, option_type="call"):
    """
    Plot histogram of simulated payoffs.
    Args:
        payoffs (np.ndarray): Array of simulated payoffs
        option_type (str): "call" or "put"
    """
    plt.figure()
    plt.hist(payoffs, bins=40, color="skyblue", edgecolor="black")
    plt.xlabel("Payoff")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of Simulated Payoffs ({option_type.title()})")
    plt.show()
