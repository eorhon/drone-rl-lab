# drone-rl-lab

Independent research on reinforcement learning for robotic control and sim-to-real autonomy.

---

## Objective

Build a structured, reproducible experimental framework to study adaptive control in aerial robotics using PX4 SITL.

This repository is not a tutorial project.
It is a long-term independent research track.

---

## Current Status

Infrastructure phase completed:

- Ubuntu 24.04 dual boot
- NVIDIA RTX 3070 Ti verified
- CUDA operational
- PyTorch GPU validated
- Virtual environment isolated
- SSH GitHub workflow active

Lab is operational.

---

## Research Direction

Initial focus:

Adaptive control under dynamics mismatch.

Core questions:

- How does RL adapt to mass/inertia variation?
- What is the effect of structured vs implicit adaptation?
- How does domain randomization influence robustness?

Future direction:

- Recurrent policies
- Explicit system identification + RL
- Sim-to-real transfer

---

## Environment Setup

Activate virtual environment:

    cd ~/rl_lab
    source venv/bin/activate

Verify CUDA:

    python gpu_smoke_test.py

---

## Research Discipline

Before any experiment:

1. Define hypothesis
2. Define measurable metric
3. Define baseline
4. Define isolated variable
5. Define failure condition

Experiments without structure are not allowed.

---

## Roadmap

Phase 1: Baseline control + PPO baseline  
Phase 2: Structured adaptation experiments  
Phase 3: Publishable conference submission  
Phase 4: Sim-to-real validation  

---

## Author

Independent researcher  
Robotics engineer  
Focused on long-term technical mastery