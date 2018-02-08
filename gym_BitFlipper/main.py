import gym
from baselines import deepq
import gym_BitFlipper
import numpy as np
from gym.envs.registration import register 

reward_max=0
def callback(lcl, _glb):  ##  make changes
  
    # stop training if reward exceeds 199
    #is_solved = lcl['t'] > 100 and sum(lcl['episode_rewards'][-101:-1]) / 100 >= 199
    reward_dist = 0.1
    reward_max = -np.sum(np.bitwise_xor(lcl['env'].initial_state,lcl['env'].goal))+1
    is_solved = len(lcl['episode_rewards']) > 100 and sum((lcl['episode_rewards'])[-101:-1])/100 >= (reward_max - reward_dist)
    return is_solved
  
def main(n=10,space_seed=0):
  # create environment
  id = "BitFlipper"+str(n)+":"+str(space_seed)+"-v0"
  try :
    register(id=id,entry_point='gym_BitFlipper.envs:BitFlipperEnv',kwargs = {"space_seed":space_seed,"n":n})
  except :
    print("Environment with id = "+id+" already registered.Continuing with that environment.")
  
  env=gym.make(id)
  reward_max = -np.sum(np.bitwise_xor(env.initial_state,env.goal))+1
  
  print("Initial State: "+str((env.initial_state).T))
  print("Goal State: "+str((env.goal).T))
  print("Max_reward: "+str(reward_max))
  # learning agent
  a=deepq.models.mlp([256])
  act = deepq.learn(env,q_func=a,lr=1e-4,max_timesteps=1000000,buffer_size=100000,exploration_fraction=0.02,
      exploration_final_eps=0.05,train_freq=1,batch_size=64,
      print_freq=200,checkpoint_freq=600,callback=callback)
  
  print("Saving model to bitflip.pkl")
  act.save("bitflip.pkl")
  
