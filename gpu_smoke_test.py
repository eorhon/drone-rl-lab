import torch

print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
    x = torch.randn(4096, 4096, device="cuda")
    y = x @ x
    print("Matmul OK. y mean:", y.mean().item())
