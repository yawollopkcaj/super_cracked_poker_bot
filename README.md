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

## Resources

- Academic papers: DeepStack, Slumbot, PokerBench, Exploitability Theory
- Tutorials on CFR, Bayesian ML, and multi-armed bandits
- Libraries: OpenSpiel, PokerRL, PettingZoo
- Datasets: Poker hand classification, custom self-play logs
- Cool read for 2 player poker... but I want to make a bot that does well in a ~6-8 player game (https://nn.cs.utexas.edu/downloads/papers/xun.gecco18.pdf).
