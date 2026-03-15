import gym
from gym import spaces

class TradingEnv(gym.Env):

    def __init__(self):
        super().__init__()

        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(low=-1, high=1, shape=(10,))
