
# Monte Carlo Option Pricing Animator

## dev/creator: tubakhxn

## Problem Overview

This project demonstrates how to price European call and put options using Monte Carlo simulation, visualizing the convergence of the simulated price to the analytical Black-Scholes price. It is designed for beginners interested in quantitative finance and Python animation.

## What is this project about?
This project is a beginner-friendly Python tool to:
- Simulate asset price paths using Geometric Brownian Motion
- Price European call and put options using Monte Carlo simulation
- Compare simulated prices to the analytical Black-Scholes price
- Visualize convergence and payoff distributions with animated plots

It is ideal for students, educators, and anyone interested in financial engineering or computational finance.

## How to Fork This Project
1. Log in to your GitHub account.
2. Go to the repository page (if hosted on GitHub).
3. Click the **Fork** button at the top right.
4. Clone your forked repository:
   ```bash
   git clone https://github.com/your-username/Monte-Carlo-Option-Pricing-Animator.git
   ```
5. Install dependencies and run as described below.

## Relevant Wikipedia Links
- [Monte Carlo Method](https://en.wikipedia.org/wiki/Monte_Carlo_method)
- [Black–Scholes Model](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model)
- [Geometric Brownian Motion](https://en.wikipedia.org/wiki/Geometric_Brownian_motion)
- [European Option](https://en.wikipedia.org/wiki/Option_(finance)#European_option)

## Features
- Monte Carlo pricing for European call and put options
- Animated plot showing convergence to Black-Scholes price
- Optional bar chart of simulated payoff distribution
- Modular, beginner-friendly code with comments
- Auto-installs dependencies (numpy, matplotlib, scipy)

## Test Cases
- Price a European call with S0=100, K=100, r=0.05, sigma=0.2, T=1.0
- Price a European put with S0=100, K=90, r=0.03, sigma=0.25, T=0.5
- Try different volatilities, strikes, and maturities to see convergence

## Key Insight
Monte Carlo simulation provides a flexible way to price options, and the convergence to the Black-Scholes price illustrates the law of large numbers in practice.

## How to Run
1. Ensure Python 3.7+ is installed.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run:
   ```bash
   pip install -r requirements.txt
   python src/main.py
   ```

## Output
- Animated line plot: Monte Carlo price converging to Black-Scholes price
- Console: Prints analytical and simulated prices
- Optional: Histogram of simulated payoffs

## Tech Stack
- Python 3.7+
- numpy
- matplotlib
- scipy

## Applications
- Financial engineering education
- Quantitative finance prototyping
- Demonstrating Monte Carlo methods

## Future Improvements
- Add support for American options
- Allow user input via GUI
- Add more advanced visualizations (e.g., 3D surface plots)
- Parallelize simulation for speed
