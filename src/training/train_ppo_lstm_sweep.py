from sb3_contrib import RecurrentPPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.monitor import Monitor
from src.envs.vertical_drone_env import VerticalDroneEnv


def make_env():
    env = VerticalDroneEnv(
        mass=1.0,
        mass_drift_per_sec=0.0,
        tau=0.15,
        include_thrust_in_obs=False,
    )
    return Monitor(env)


if __name__ == "__main__":
    variants = [
        {
            "name": "lr1e4_ns1200",
            "learning_rate": 1e-4,
            "n_steps": 1200,
            "save_path": "experiments/ppo_lstm_lag_lr1e4_ns1200",
        },
        {
            "name": "lr1e4_ns2400",
            "learning_rate": 1e-4,
            "n_steps": 2400,
            "save_path": "experiments/ppo_lstm_lag_lr1e4_ns2400",
        },
        {
            "name": "lr3e4_ns2400",
            "learning_rate": 3e-4,
            "n_steps": 2400,
            "save_path": "experiments/ppo_lstm_lag_lr3e4_ns2400",
        },
    ]

    for variant in variants:
        print(f"\n=== Training variant: {variant['name']} ===")
        env = DummyVecEnv([make_env])

        model = RecurrentPPO(
            policy="MlpLstmPolicy",
            env=env,
            verbose=1,
            n_steps=variant["n_steps"],
            batch_size=64,
            learning_rate=variant["learning_rate"],
            gamma=0.99,
            tensorboard_log=f"logs/tb_lstm_sweep/{variant['name']}",
        )

        model.learn(total_timesteps=100_000)
        model.save(variant["save_path"])

        env.close()
