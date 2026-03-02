# Weekly Log

---

## Week X – RecurrentPPO Failure Analysis & Env Stabilization

### Environment Fix

- Replaced altitude clipping pathology with explicit episode termination when altitude exceeds bound (`|z| > Z_MAX`).
- Added terminal penalty on bound termination.
- Why this was necessary: clipping hid failure modes at the state boundary and produced pathological learning/evaluation behavior.

### MLP Results (Post-Fix)

- Sanity hover stable: mean z ≈ 0.924, last z ≈ 0.996.

Drift RMSE (mass drift):

| Drift | RMSE |
|---|---:|
| 0.00 | 0.2575 |
| 0.05 | 0.2584 |
| 0.10 | 0.2556 |
| 0.20 | 0.2851 |
| 0.30 | 0.3278 |

### LSTM Results (Post-Fix)

- Sanity hover unstable: mean z ≈ -3.50, last z ≈ -10.
- Drift RMSE remains high and nearly flat across drift levels (~5.28).

### RecurrentPPO Sweep Results

| Variant | mean z | last z | RMSE@0.0 | RMSE@0.3 |
|---|---:|---:|---:|---:|
| lr=1e-4, n_steps=1200 | -3.9045 | -10.0453 | 5.7062 | 5.5057 |
| lr=1e-4, n_steps=2400 | -3.9654 | -10.0165 | 5.8378 | 5.5892 |
| lr=3e-4, n_steps=2400 | -3.8822 | -8.5580 | 5.5026 | 5.5307 |

Conclusion: RecurrentPPO failed to learn hover under tested settings; likely optimization/rollout/algorithm limitation.

### Lessons Learned

- State clipping can hide instability and create misleading training outcomes.
- Fast sanity tests (hover behavior) are critical before full metric interpretation.
- Critic health signals (especially explained variance) are key for diagnosing policy learning quality.
- Recurrent setups can be unstable even when feedforward baselines are stable under identical environment conditions.

### Next Actions

- Decide next recurrent direction: new recurrent algorithm or revised recurrent training protocol.
- Consider adding a classical adaptive baseline as a comparison anchor.
- Keep the environment fixed while testing controller/training alternatives.

---

## Week 1 — Infrastructure Bring-Up

### Completed

- Ubuntu 24.04 dual boot installed
- Windows boot priority corrected
- NVIDIA driver installed
- CUDA verified via nvidia-smi
- PyTorch CUDA build installed (cu121)
- Virtual environment created and isolated
- Dependencies frozen
- GPU smoke test successful
- tmux configured
- GitHub SSH authentication configured

### Technical Validation

torch.cuda.is_available() → True  
RTX 3070 Ti detected  
CUDA matrix multiplication test passed  

### Lessons Learned

- UEFI boot order can override GRUB silently
- nomodeset required for initial NVIDIA live boot
- venv isolation prevents system-level pip conflicts
- SSH authentication is cleaner than HTTPS tokens

### Lab Status

Operational.

### Next Week Focus

1. Finalize VS Code interpreter configuration
2. Create minimal experiment skeleton
3. Define first formal hypothesis