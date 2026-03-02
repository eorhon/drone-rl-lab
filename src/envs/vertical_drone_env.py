import gymnasium as gym
import numpy as np
from gymnasium import spaces

class VerticalDroneEnv(gym.Env):
    """
    Minimal 1D vertical 'drone' environment to study dynamics mismatch.
    State: [z, z_dot]
    Action: thrust command (normalized in [-1, 1]) mapped to [0, max_thrust]
    Dynamics: z_ddot = (thrust / mass) - g
    """
    metadata = {"render_modes": []}
    Z_MAX = 10.0

    def __init__(
        self,
        dt: float = 0.02,
        episode_seconds: float = 6.0,
        mass: float = 1.0,
        mass_drift_per_sec: float = 0.0,  # used during evaluation
        tau: float = 0.15,
        include_thrust_in_obs: bool = False,
        g: float = 9.81,
        max_thrust: float = 25.0,
        z_target: float = 1.0,
        seed: int | None = None,
    ):
        super().__init__()
        self.dt = dt
        self.steps = int(episode_seconds / dt)
        self.mass0 = float(mass)
        self.mass_drift_per_sec = float(mass_drift_per_sec)
        self.tau = float(tau)
        self.include_thrust_in_obs = bool(include_thrust_in_obs)
        self.g = float(g)
        self.max_thrust = float(max_thrust)
        self.z_target = float(z_target)

        # Action: normalized thrust command
        self.action_space = spaces.Box(low=-1.0, high=1.0, shape=(1,), dtype=np.float32)

        # Observation: z, z_dot (+ optional thrust state)
        if self.include_thrust_in_obs:
            obs_high = np.array([10.0, 20.0, self.max_thrust], dtype=np.float32)
        else:
            obs_high = np.array([10.0, 20.0], dtype=np.float32)
        self.observation_space = spaces.Box(-obs_high, obs_high, dtype=np.float32)

        self._rng = np.random.default_rng(seed)
        self._t = 0
        self._z = 0.0
        self._zd = 0.0
        self._thrust = 0.0

    def _obs(self):
        if self.include_thrust_in_obs:
            return np.array([self._z, self._zd, self._thrust], dtype=np.float32)
        return np.array([self._z, self._zd], dtype=np.float32)

    def _current_mass(self) -> float:
        # Linear drift in mass over time (for evaluation)
        return max(0.1, self.mass0 * (1.0 + self.mass_drift_per_sec * (self._t * self.dt)))

    def reset(self, seed: int | None = None, options=None):
        super().reset(seed=seed)
        if seed is not None:
            self._rng = np.random.default_rng(seed)

        self._t = 0
        self._z = float(self._rng.normal(loc=0.0, scale=0.05))
        self._zd = float(self._rng.normal(loc=0.0, scale=0.05))
        self._thrust = 0.0

        obs = self._obs()
        info = {"mass": self._current_mass()}
        return obs, info

    def step(self, action):
        self._t += 1

        # Clip and map normalized action to thrust
        a = float(np.clip(action[0], -1.0, 1.0))
        thrust_cmd = (a + 1.0) * 0.5 * self.max_thrust  # [0, max_thrust]

        # First-order actuator lag: thrust_actual follows thrust_cmd
        alpha = self.dt / max(self.tau, 1e-6)
        alpha = float(np.clip(alpha, 0.0, 1.0))
        self._thrust = (1.0 - alpha) * self._thrust + alpha * thrust_cmd

        m = self._current_mass()
        zdd = (self._thrust / m) - self.g

        # Integrate
        self._zd = float(np.clip(self._zd + zdd * self.dt, -20.0, 20.0))
        self._z = float(self._z + self._zd * self.dt)

        # Reward: tracking + mild control penalty
        err = self._z - self.z_target
        reward = - (err * err) - 0.001 * (a * a)

        terminated = abs(self._z) > self.Z_MAX
        truncated = self._t >= self.steps

        if terminated:
            reward -= 100.0

        obs = self._obs()
        info = {"mass": m, "thrust_cmd": thrust_cmd, "thrust": self._thrust, "err": err}
        if terminated:
            info["terminated_reason"] = "z_bound"
        return obs, float(reward), terminated, truncated, info
