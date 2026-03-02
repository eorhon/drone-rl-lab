import numpy as np
from sb3_contrib import RecurrentPPO
from stable_baselines3 import PPO
from src.envs.vertical_drone_env import VerticalDroneEnv


def run(model, recurrent=False, steps=300):
    env = VerticalDroneEnv(
        mass=1.0,
        mass_drift_per_sec=0.0,
        tau=0.15,
        include_thrust_in_obs=False,
    )
    obs, _ = env.reset()
    zs = []
    lstm_states = None
    episode_start = np.ones((1,), dtype=bool)

    for _ in range(steps):
        if recurrent:
            action, lstm_states = model.predict(
                obs,
                state=lstm_states,
                episode_start=episode_start,
                deterministic=True,
            )
            episode_start[:] = False
        else:
            action, _ = model.predict(obs, deterministic=True)

        obs, _, term, trunc, _ = env.step(action)
        zs.append(obs[0])
        if term or trunc:
            break

    zs = np.array(zs)
    print("mean z:", float(zs.mean()), "std z:", float(zs.std()), "last z:", float(zs[-1]))


if __name__ == "__main__":
    mlp = PPO.load("experiments/ppo_mlp_vertical_drone_lag_100k")
    lstm = RecurrentPPO.load("experiments/ppo_lstm_vertical_drone_lag_100k")

    print("MLP:")
    run(mlp, recurrent=False)
    print("LSTM:")
    run(lstm, recurrent=True)
