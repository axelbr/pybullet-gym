import gym  # open ai gym
import pybulletgym  # register PyBullet enviroments with open ai gym

env = gym.make('InvertedPendulumMuJoCoEnv-v0')
# env.render() # call this before env.reset, if you want a window showing the environment
env.reset()
env