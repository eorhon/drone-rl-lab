# AGENTS.MD
Independent Robotics & Reinforcement Learning Research Track

---

## 1. Identity

This repository represents an independent research lab focused on:

- Reinforcement Learning for robotic control
- Drone-based simulation research (PX4 SITL)
- Adaptive control under dynamics mismatch
- Sim-to-real robustness

This work is:

- Not affiliated with any university
- Not tied to employer IP
- Intended for long-term capability growth
- Structured toward publishable research

Roles:

- Human = Principal Investigator, Architect, Experiment Designer
- AI Tools = Software Engineers, Research Assistants
- Final authority = Human

---

## 2. Long-Term Vision

### Phase 1 — Infrastructure (Completed)
- Ubuntu 24.04 dual boot
- NVIDIA driver working
- CUDA runtime verified
- PyTorch GPU validated
- Python venv isolated
- GitHub SSH configured

### Phase 2 — Research Foundation
- Modular experiment framework
- Reproducible RL training loop
- Baseline controllers (classical + RL)
- Controlled experiment protocol

### Phase 3 — Publishable Research
- Structured hypothesis-driven experiments
- Ablation studies
- Conference-level submission

### Phase 4 — Advanced Direction
- Implicit vs explicit adaptation comparison
- Recurrent policies
- Sim-to-real experiments
- Journal extension

---

## 3. Research Protocol (MANDATORY)

Before writing any experiment code, define:

1. What is the hypothesis?
2. What is the measurable metric?
3. What is the baseline?
4. What variable am I isolating?
5. What does failure mean?

If these are not written clearly → experiment does not begin.

No uncontrolled tinkering.

---

## 4. Python Environment Discipline

All research-related Python work must be performed inside a virtual environment.

Rules:

- Never install research packages globally.
- Always activate venv before running experiments.
- Freeze dependencies after major updates.
- Rebuild venv instead of polluting system Python.

Activation:

    cd ~/rl_lab
    source venv/bin/activate

Deactivation:

    deactivate

Reproducibility is mandatory.

---

## 5. Intellectual Boundaries

The following topics are restricted due to employer overlap:

- Interception systems
- Classified navigation components
- Proprietary system architectures

Independent work must be:

- Clean-room implemented
- Publicly publishable
- Legally and ethically safe

---

## 6. Infrastructure Status

GPU: RTX 3070 Ti Laptop  
Driver: 590.x  
CUDA: 13.1  
PyTorch: cu121 build  
Virtual environment: Active and isolated  
tmux: Configured  
SSH GitHub: Active  

Lab status: Operational.

---

## 7. Operating Principles

1. Infrastructure before ambition
2. Measurement before iteration
3. Isolation before complexity
4. Reproducibility before novelty
5. Discipline before motivation
6. Stop at clean milestones

---

## 8. Weekly Review Protocol

Every week:

- Log progress
- Log failures
- Log lessons
- Define next week’s 3 tasks only
- Avoid scope creep

This is a long-term research arc (2–5 years).
Slow, deliberate growth.