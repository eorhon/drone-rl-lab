import numpy as np
from stable_baselines3 import PPO
from src.envs.vertical_drone_env import VerticalDroneEnv

MODEL_PATH = "experiments/ppo_mlp_vertical_drone_lag_100k"

def evaluate_model(model, mass_drift, n_episodes=10):
    rmse_list = []

    for _ in range(n_episodes):
        env = VerticalDroneEnv(
            mass=1.0,
            mass_drift_per_sec=mass_drift,
            tau=0.15,
            include_thrust_in_obs=False,
        )

        obs, _ = env.reset()
        done = False
        errors = []

        while not done:
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated
            errors.append(info["err"])

        errors = np.array(errors)
        rmse = np.sqrt(np.mean(errors**2))
        rmse_list.append(rmse)

    return np.mean(rmse_list), np.std(rmse_list)


def relative_degradation(rmse_drift, rmse_nominal):
    denom = max(float(rmse_nominal), 1e-9)
    return (float(rmse_drift) - float(rmse_nominal)) / denom


if __name__ == "__main__":
    model = PPO.load(MODEL_PATH)

    drift_levels = [0.0, 0.05, 0.1, 0.2, 0.3]
    mean_by_drift = []

    print("\n=== MLP PPO Evaluation Under Mass Drift ===\n")

    for drift in drift_levels:
        mean_rmse, std_rmse = evaluate_model(model, drift)
        mean_by_drift.append(mean_rmse)
        print(f"Drift: {drift:.2f} | RMSE: {mean_rmse:.4f} ± {std_rmse:.4f}")

    rmse0 = mean_by_drift[0]
    degradations = [relative_degradation(rmse, rmse0) for rmse in mean_by_drift]

    print("\nRelative degradation D(d) = (RMSE(d)-RMSE(0))/RMSE(0):")
    for drift, deg in zip(drift_levels, degradations):
        print(f"Drift: {drift:.2f} | D(d): {deg:.4f}")

    slope, intercept = np.polyfit(np.array(drift_levels), np.array(degradations), 1)
    print(f"\nDegradation slope: {slope:.4f} (intercept: {intercept:.4f})")
