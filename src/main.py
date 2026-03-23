"""
main.py
Entry point for Monte Carlo Option Pricing Animator.
"""
import numpy as np
from data_generator import generate_gbm_paths
from monte_carlo_pricing import monte_carlo_option_price
from black_scholes import black_scholes_price
from visualization import animate_convergence, plot_payoff_distribution

# --- User Inputs ---
S0 = 100         # Spot price
K = 100          # Strike price
r = 0.05         # Risk-free rate
sigma = 0.2      # Volatility
T = 1.0          # Time to maturity (years)
option_type = "call"  # "call" or "put"
steps = 100      # Time steps for GBM (not used in MC pricing, but for path simulation)
max_paths = 2000 # Max number of MC paths for animation
seed = 42        # Random seed for reproducibility

# --- Analytical Black-Scholes Price ---
bs_price = black_scholes_price(S0, K, r, sigma, T, option_type)
print(f"Black-Scholes {option_type.title()} Price: {bs_price:.4f}")

# --- Monte Carlo Convergence Animation ---
mc_prices = []
for n in range(1, max_paths + 1):
    price, _ = monte_carlo_option_price(S0, K, r, sigma, T, n, option_type, seed)
    mc_prices.append(price)
mc_prices = np.array(mc_prices)

animate_convergence(mc_prices, bs_price, max_paths, option_type)

# --- Final Monte Carlo Price and Payoff Distribution ---
final_price, payoffs = monte_carlo_option_price(S0, K, r, sigma, T, max_paths, option_type, seed)
print(f"Monte Carlo {option_type.title()} Price (N={max_paths}): {final_price:.4f}")

plot_payoff_distribution(payoffs, option_type)


# --- Animated Asset Price Paths (like sample image) ---
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_asset_paths(paths):
    fig, ax = plt.subplots()
    n_paths, n_steps = paths.shape
    lines = [ax.plot([], [], lw=1)[0] for _ in range(n_paths)]
    ax.set_xlim(0, n_steps - 1)
    ax.set_ylim(np.min(paths) * 0.95, np.max(paths) * 1.05)
    ax.set_xlabel("Trading Day")
    ax.set_ylabel("Price")
    ax.set_title("Simulated Asset Price Paths")

    def update(frame):
        for i, line in enumerate(lines):
            line.set_data(np.arange(frame + 1), paths[i, :frame + 1])
        return lines

    ani = FuncAnimation(fig, update, frames=n_steps, interval=30, blit=True)
    plt.show()

# Generate and animate asset paths (10 paths, 250 steps)
paths = generate_gbm_paths(S0, r, sigma, T, 250, 10, seed)
animate_asset_paths(paths)
