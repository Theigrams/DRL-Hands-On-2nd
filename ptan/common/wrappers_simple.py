"""
Simple wrappers
"""
import collections

import gymnasium as gym
import numpy as np


class FrameStack1D(gym.Wrapper):
    """
    Stacks observations into 1D array
    """

    def __init__(self, env, k):
        assert isinstance(env, gym.Env)
        assert isinstance(env.observation_space, gym.spaces.Box)
        assert len(env.observation_space.shape) == 1
        super(FrameStack1D, self).__init__(env)
        self.k = k
        self.frames = collections.deque([], maxlen=k)
        shp = env.observation_space.shape
        self.observation_space = gym.spaces.Box(
            low=np.min(env.observation_space.low),
            high=np.max(env.observation_space.high),
            shape=(env.observation_space.shape[0] * k,),
            dtype=env.observation_space.dtype,
        )

    def reset(self):
        ob, info = self.env.reset()
        for _ in range(self.k):
            self.frames.append(ob)
        return self._get_ob(), info

    def step(self, action):
        ob, reward, terminated, truncated, info = self.env.step(action)
        self.frames.append(ob)
        return self._get_ob(), reward, terminated, truncated, info

    def _get_ob(self):
        assert len(self.frames) == self.k
        return np.concatenate(self.frames)
