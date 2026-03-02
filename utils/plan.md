# PLAN.md
Independent Reinforcement Learning Research Roadmap

Author: Eftun Orhon
Machine: Monster Tulpar T7 V21.9
GPU: RTX 3070 Ti Laptop (8GB)
OS: Ubuntu 24.04 (dual boot)
Status: Infrastructure Complete

---

# 0. Philosophy

This is a long-term independent research track (2–5 years).

Goals:
- Deep expertise in reinforcement learning for robotic control
- Publishable conference-level work
- Strong sim-to-real capability
- Foundation for future technical leadership (CTO-level competence)

Principles:
- Slow, steady, disciplined
- Hypothesis-driven experiments
- Reproducibility first
- No chaotic experimentation
- No dependency pollution
- No employer IP overlap

---

# 1. Current Status (Week 1)

Infrastructure:
- Ubuntu dual boot installed
- NVIDIA driver working
- CUDA verified
- PyTorch GPU operational
- venv isolated and frozen
- GitHub SSH configured
- tmux configured
- Documentation structured

Lab status: Operational.

---

# 2. Time Constraints

Available time:
- Weekdays: ~1 hour
- Weekend: 3–4 hours
- Max sustainable: ~2 hours/day average

Must preserve:
- Family balance
- Work performance
- Long-term consistency

---

# 3. Research Direction

Primary Track (B Path):
Adaptive control under dynamics mismatch using RL.

Why:
- Aligned with robotics future
- Publishable
- Not employer-conflicting
- Suitable for simulation-first workflow
- Expandable to sim-to-real

Platform:
PX4 SITL (drone-based simulation)

---

# 4. Research Phases

## Phase 1 – Structured Baseline (4–6 weeks)

- Implement minimal experiment framework
- PPO baseline on nominal drone model
- Define metrics:
    - Tracking error
    - Stability
    - Sample efficiency
- Establish reproducible training pipeline

Deliverable:
Baseline performance report.

---

## Phase 2 – Dynamics Mismatch Study (6–10 weeks)

Introduce controlled variations:
- Mass perturbation
- Inertia change
- Actuator delay
- Sensor noise

Research questions:
- How robust is vanilla PPO?
- Does domain randomization help?
- What is the adaptation curve?

Deliverable:
Structured experiment results + ablation.

---

## Phase 3 – Adaptive Architecture (10–16 weeks)

Explore:
- Recurrent policies (LSTM)
- Context embedding
- Online identification + policy conditioning

Hypothesis:
Structured adaptation outperforms naive domain randomization.

Pre-registered success criterion (before training):
- Model A: PPO (MLP), Model B: RecurrentPPO (LSTM).
- Controlled setup (must be identical): same tau, same training timesteps, same seeds, same reward, same evaluation protocol.
- Only intended variable difference: memory (feedforward vs recurrent policy).
- Metric definition per model and drift level d: D(d) = (RMSE(d) - RMSE(0)) / RMSE(0).
- Primary adaptation metric: slope of D(d) vs drift d (robustness degradation slope).
- Decision rule: LSTM helps if mean slope is lower than MLP and the slope difference is statistically significant across seeds (two-sided Welch t-test, alpha = 0.05, minimum 5 shared seeds).
- Secondary report (not hard-gated): RMSE and relative improvement at each drift point, including d >= 0.20.
- This is an offline evaluation criterion only; it does not create any runtime controller threshold.

Deliverable:
Conference-level paper draft.

---

## Phase 4 – Sim-to-Real (Optional Future)

- Build small quadcopter
- Test sim-trained policy
- Study performance gap
- Investigate fine-tuning

### Decision Gate: RecurrentPPO viability

- RecurrentPPO (LSTM) was attempted with a stabilization sweep under controlled settings.
- If RecurrentPPO cannot learn stable hover, we will either switch to a different recurrent method or conclude MLP is preferred.
- Recurrent preference will only be revisited if partial observability is increased for real reasons (for example delay/dropout), not artificial complexity.

---

# 5. Publication Goal

Target:
- Conference-level publication (ICRA/IROS-level ambition)
- Independent or co-authored
- Eventually journal extension

Timeline:
12–24 months realistic.

---

# 6. Hard Rules

Before coding any experiment:

1. What is the hypothesis?
2. What is the measurable metric?
3. What is the baseline?
4. What variable am I isolating?
5. What does failure mean?

If undefined → do not start.

---

# 7. Weekly Execution Model

Each week:
- Define 3 tasks maximum
- Log results
- Log failures
- No scope expansion
- Stop at clean milestone

Consistency > intensity.