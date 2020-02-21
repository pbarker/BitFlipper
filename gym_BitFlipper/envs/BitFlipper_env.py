import numpy as np
import gym
from gym import spaces
from gym.utils import seeding

class BitFlipperEnv(gym.Env):
  '''Bit Flipping environment
      The state space is binary strings of length n.
      The action space is an index i from {0,1...n-1} which represents the agent flipping ith bit of the environment.
      Action = n means agent stays in the same state.
      Given an initial state the agent has to reach a goal state.
      Reward: Only goal state has reward 0,rest all states have reward -1
  '''
  metadata = {'render.modes': ['human','ansi']}
  def __init__(self,n=10,space_seed=None):
    self.n=n    
    self.action_space = spaces.Discrete(self.n)
    self.observation_space = spaces.MultiBinary(self.n)
    self.reward_range = (-1,0)
    self.initial_state = self.observation_space.sample()
    self.goal = self.observation_space.sample()
    self.state = self.initial_state
    self.envstepcount = 0
    # self.seed(seed=space_seed)
    self.reward_max = 0
  
  def step(self,action):
    '''
     accepts action and returns obs,reward, b_flag(episode start), info dict(optional)
    '''
    if(self.action_space.contains(action)):
      if(not(action==self.n)):
        self.state = self.bitflip(action)  ## computes s_t1
      reward = self.calculate_reward(self.goal,self.state)
      self.envstepcount += 1
      done = self.compute_done(reward)
      return  (np.array(self.state),reward,done,{})
    else:
       print("Invalid action")
        
  def reset(self,seed=None):  
    self.envstepcount = 0
    self.initial_state = self.observation_space.sample()
    self.goal = self.observation_space.sample()
    self.state = self.initial_state
    if(np.array_equal(self.goal,self.state)):
      self.reset()
    self.reward_max = 0
    return self.state
  
  def close(self):
    pass
  
  def render(self, mode='human', close=False):
    print_str = str("State: "+str(self.state.T)+" Steps done: "+str(self.envstepcount))
    if(mode=='human'):
      print(print_str)
    if(mode=='ansi'):
      return print_str 
  
  def seed(self, seed=None):
    self.np_random, seed = seeding.np_random(seed)
    return [seed]
  
  def bitflip(self,index):
    s2=np.array(self.state)
    s2[index] = not s2[index]
    return s2
  
  def calculate_reward(self,goal,state):
    if(np.array_equal(goal,state)):
      return 0.0
    else:
      return -1.0
    
  def compute_done(self,reward):
    if(reward==0 or self.envstepcount >=self.n):
      return True
    else:
      return False
  
