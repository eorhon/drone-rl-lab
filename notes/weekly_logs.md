# Weekly Log

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