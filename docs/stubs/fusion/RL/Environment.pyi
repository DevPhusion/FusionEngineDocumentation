"""
Headless RL stepping API
"""
from __future__ import annotations
import fusion as fusion
import gymnasium as gym
import gymnasium.core
import numpy as np
import numpy
import numpy.typing
import os as os
from stable_baselines3.a2c.a2c import A2C
from stable_baselines3.common.vec_env.dummy_vec_env import DummyVecEnv
from stable_baselines3.ddpg.ddpg import DDPG
from stable_baselines3.ppo.ppo import PPO
from stable_baselines3.sac.sac import SAC
from stable_baselines3.td3.td3 import TD3
import typing
__all__: list[str] = ['A2C', 'DDPG', 'DummyVecEnv', 'PPO', 'SAC', 'TD3', 'clear_cache', 'fusion', 'get_action_space', 'get_observation_space', 'get_snapshot', 'gym', 'is_training', 'load_model', 'np', 'os', 'predict', 'reset', 'step']
class _LoadedModel:
    __slots__: typing.ClassVar[tuple] = ('model', 'vecnorm', 'mtime')
    def __init__(self, model, vecnorm, mtime):
        ...
class _SpaceOnlyEnv(gymnasium.core.Env):
    """
    Placeholder env exposing only the spaces set_venv() needs to attach to — never reset
        or stepped, just used to construct a matching DummyVecEnv for the restored wrapper.
    """
    __parameters__: typing.ClassVar[tuple] = tuple()
    def __init__(self, observation_space, action_space):
        ...
    def reset(self, *, seed = None, options = None):
        ...
    def step(self, action):
        ...
def _resolve_algo_class(algorithm):
    ...
def _resolve_existing_path(abs_path):
    """
    Returns the actual file path that exists on disk (path or path + '.zip'), or None.
    """
def _try_load_vecnormalize(existing_model_path, model, display_path):
    ...
def clear_cache():
    ...
def get_action_space() -> typing.Any:
    """
    Returns the gymnasium.spaces.Space configured via AgentComponent.set_action_space() on the scene's first AgentComponent.
    """
def get_observation_space() -> typing.Any:
    """
    Returns the gymnasium.spaces.Space configured via AgentComponent.set_observation_space(), or None if unset (in which case a default Box inferred from observation length is used).
    """
def get_snapshot(width: typing.SupportsInt | typing.SupportsIndex = 128, height: typing.SupportsInt | typing.SupportsIndex = 128) -> numpy.typing.NDArray[numpy.uint8]:
    """
    Render the scene off-screen (works even during headless training) and return it as an (height, width, 3) uint8 RGB array.
    
    Example:
        ```python
        frame = fusionRL.Environment.get_snapshot(84, 84)
        self.agent.add_observation((frame.astype('float32') / 255.0).flatten().tolist())
        ```
    """
def load_model(path, algorithm = 'PPO'):
    ...
def predict(loaded, observation, deterministic = True):
    ...
def reset() -> list:
    """
    Reload the editing scene, run one priming tick, and return the initial observation.
    """
def step(action: typing.Any) -> tuple[list, float, bool]:
    """
    Advance the simulation by one physics tick with the given action applied (type must match the configured action_space), returning (observation, reward, done).
    """
_model_cache: dict = {}
is_training: bool = False
