import os

from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.monitor import Monitor
from src.envs.vertical_drone_env import VerticalDroneEnv

def make_env():
    env = VerticalDroneEnv(mass=1.0, mass_drift_per_sec=0.0, tau=0.15, include_thrust_in_obs=False)
    return Monitor(env)

if __name__ == "__main__":
    total_timesteps = int(os.getenv("TOTAL_TIMESTEPS", "100000"))

    env = DummyVecEnv([make_env])

    model = PPO(
        policy="MlpPolicy",
        env=env,
        verbose=1,
        n_steps=2048,
        batch_size=64,
        learning_rate=3e-4,
        gamma=0.99,
        tensorboard_log="logs/tb_mlp",
    )

    model.learn(total_timesteps=total_timesteps)
    model.save("experiments/ppo_mlp_vertical_drone_lag_100k")
