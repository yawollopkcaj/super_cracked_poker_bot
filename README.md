# Super Duper Cracked Poker Bot

## Project Overview

My **Super Duper Cracked Poker Bot** is an open-source project focused on developing an **exploitative poker AI agent** using a blend of **machine learning**, **mathematical game theory**, and practical engineering. The project is designed as a robust, transparent, and adaptive poker agent that can compete, learn, and evolve against real opponents in real time so I can shit on my fraternity brothers and win back my dues.

This repository is intended for:
- Those interested in poker AI, opponent modeling, and reinforcement learning.
- Researchers or students with an interest in game theory, Bayesian inference, and online adaptation.

---

## Learning & Development Goals

### 1. Machine Learning: Opponent Modeling & Strategy

**Core Goals**
- Implement a Bayesian opponent model (e.g., Dirichlet-multinomial or HMM).
- Apply policy learning or imitation learning based on opponent history.
- Use ML classifiers or regressors (e.g., logistic regression, neural nets) to predict opponent ranges.
- Explore reinforcement learning approaches like DQN or PPO for adaptive play.

**Stretch Goals**
- Integrate meta-learning techniques (e.g., MAML, contextual bandits) for rapid adaptation.
- Use unsupervised learning to categorize player archetypes.
- Train sequential models (e.g., RNNs, transformers) to predict opponent behavior over time.

### 2. Mathematics & Game Theory

**Core Goals**
- Implement Counterfactual Regret Minimization (CFR).
- Analyze exploitability bounds in simplified poker games.
- Formalize games as Markov Decision Processes (MDPs) or Extensive Form Games.
- Use Bayesian inference to dynamically update beliefs about opponent strategies.

**Stretch Goals**
- Derive optimal exploit strategies for toy poker games.
- Apply convex optimization to calculate best responses.
- Study convergence properties of adaptive learning strategies under uncertainty.

### 3. Public Engagement & Communication

**Core Goals**
- Create a well-structured, documented GitHub repository with examples and tests.
- Write at least one blog post explaining the project in accessible terms.
- Develop simple visualizations to demonstrate bot behavior and adaptation.

**Stretch Goals**
- Release demo videos or animations via platforms like Twitter/X, Reddit, or YouTube.
- Launch a web-based interactive demo.
- Build a short tutorial series explaining both the theory and implementation.

---

## What's Missing in Existing Projects

1. **Lack of Transparency**  
   Many poker AIs operate as black boxes with little insight into their decision-making. Few expose their internal beliefs or opponent models in real time.

2. **Limited Use of Advanced ML**  
   Most bots rely on rule-based strategies, GTO solvers, or static evaluation functions. Projects using deep learning often underperform or fail to exploit opponents effectively.

3. **No Real-Time Adaptation**  
   Opponent models tend to be static or offline-trained. Few systems adapt in-game based on observed behavior.

4. **Weak Interfaces**  
   Open-source frameworks tend to prioritize backend simulations without providing intuitive UIs or public-facing visualizations.

5. **Low Visibility**  
   Many projects lack clear documentation, demos, or community presence. There’s often no narrative or interpretation layer for non-experts.

---

## What Sets This Project Apart

| Gap in Other Projects                           | This Project Delivers                                  |
|-------------------------------------------------|--------------------------------------------------------|
| Black-box logic                                 | Transparent, interpretable opponent modeling           |
| Static strategy                                 | Real-time adaptation via Bayesian and meta-learning    |
| Heads-up only                                   | Support for multi-player table formats                 |
| No live interaction                             | Interactive web-based visualizations and demos         |
| GTO-focused benchmarking                        | Performance evaluated on exploitation and adaptation   |
| Minimal community visibility                    | Public code, blog, video walkthroughs, and tutorials   |

---

## Deliverables

- Fully documented, modular codebase
- Bayesian opponent modeling with live updating
- Integration of deep RL components
- Blog post(s) explaining design decisions and math
- Interactive demo (via browser or CLI)
- Portfolio-quality visuals and writeups

---

## Research and Resources

### Academic Papers
- DeepStack  
- Slumbot  
- PokerBench  
- Exploitability Theory  

### Tutorials
- Tutorials on CFR  
- Bayesian Machine Learning  
- Multi-Armed Bandits  

### Libraries
- OpenSpiel  
- PokerRL  
- PettingZoo  

### Datasets
- Poker hand classification  
- Custom self-play logs  

### Other Resources
- [Cool read for 2-player poker... but I want to make a bot that does well in a 6-player game](https://nn.cs.utexas.edu/downloads/papers/xun.gecco18.pdf)  
- [MUST READ, still gathering resources](https://news.ycombinator.com/item?id=20414905)  
- Pre-existing bots to look into:  
  - **Pluribus** – first AI to beat humans in multiplayer poker (2019)  
  - **ReBeL** – uses recursive reasoning + RL  
  - **PokerSnowie** – commercial AI trained via self-play  
- [Another interesting read but potentially outdated](https://poker-ai.org/page/2/)  

---

## Main Research

### Pluribus

**Abstract:**  
The Pluribus poker bot is the first AI to beat professionals in multiplayer no-limit Texas Hold'em (2019).

**What makes this project special?**  
- **Solving Multiplayer No-Limit Hold'em:** Prev AI triumphs were limited to heads-up (two-player) games. Pluribus is the first to consistently win at 6-player.  
- **Hybrid Strategy: Equilibrium + Search:** Uses approximate Nash equilibrium strategies precomputed for abstracted game states. At runtime, it performs limited-depth search with real-time opponent modeling and robust Monte Carlo sampling, discarding opponent actions that are off-path or degenerate.  
- **Efficiency:** Unlike earlier systems requiring supercomputers, Pluribus runs on a single machine with multiple cores, making it more accessible.

**How can I apply these techniques to my poker bot?**  
- **Abstract Large Games:** Simplify the game by mapping similar hands into fewer "buckets." Use equilibrium computation (e.g., CFR) over the abstracted version.  
- **Combine Offline + Online Strategy:** Precompute offline and at runtime use online search (depth-limited) combined with opponent-specific adjustments based on recent play.  
- **Multiplayer Scaling:** Adopt abstractions and search only around your node to manage computational complexity.  
- **Opponent Modeling for Bluffing:** Fit a simple model (e.g., logistic regression, Bayesian updates) to track tendencies like frequency of bluffing or folding, adjusting your strategy exploitatively when edges are found.  
- **Leverage Poker Frameworks:** Use tools like PokerKit for game state management and abstraction, and deep reinforcement learning for strategy fine-tuning.

---

### PokerGPT: An End-to-End Lightweight Solver for Multi-Player Texas Hold'em via LLM (Jan 2024)

**What makes this project special?**  
PokerGPT overcomes exponential game tree growth of CFR in multiplayer games by transforming a set of textual records acquired from real games into prompts, and uses them to fine-tune a lightweight pre-trained LLM — further processing them into textual instructions using prompt engineering techniques.

**How can I apply these techniques to my poker bot?**  
Try using an LLM for high-level reasoning and pair it with quick numeric modules to compute odds precisely — mitigating LLM math weakness.

---

### TL;DR

Pluribus is a true equilibrium-seeking agent with robust theory and real-time adjustments. It’s the gold standard for competitive and provably strong multiplayer poker AI.  
PokerGPT is a flexible, lightweight, text-first system that’s easier to build, train, and scale — but it sacrifices GTO rigor, math precision, and adaptive play.

Make sure to leverage frameworks like **OpenHoldem** to benchmark and evaluate the bot alongside baselines.

---

### 🔗 Sources
- Pluribus: https://news.ycombinator.com/item?id=20414905  
- PokerGPT: https://arxiv.org/abs/2401.06781


