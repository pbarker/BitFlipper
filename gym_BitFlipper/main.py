import gym
from baselines import deepq
import gym_BitFlipper
import numpy as np
from gym.envs.registration import register 
import os
import tensorflow as tf


def callback(lcl, _glb):
    #for deepq training
    #stop training when mean reward for last 100 episodes <= (reward_max - reward_dist)
    reward_dist = 0.1
    is_solved = lcl['saved_mean_reward']==(lcl['env'].reward_max - reward_dist)
    return is_solved

def make_env(n=10,space_seed=0):
  # create environment
  id = "BitFlipper"+str(n)+":"+str(space_seed)+"-v0"
  try :
    register(id=id,entry_point='gym_BitFlipper.envs:BitFlipperEnv',kwargs = {"space_seed":space_seed,"n":n})
  except :
    print("Environment with id = "+id+" already registered.Continuing with that environment.")
  env=gym.make(id)
  return env

def train(env,save_path):
  #train deepq agent on env
  print("Initial State: "+str((env.initial_state).T))
  print("Goal State: "+str((env.goal).T))
  print("Max_reward: "+str(env.reward_max))
  #agent has 1 mlp hidden layer with 256 units
  a=deepq.models.mlp([256])
  act = deepq.learn(env,q_func=a,lr=1e-3,max_timesteps=80000*env.n,buffer_size=500000,exploration_fraction=0.02,
      exploration_final_eps=0.02,train_freq=1,batch_size=128,
      print_freq=200,checkpoint_freq=1000,target_network_update_freq=16*env.n,callback=callback)
  #save trained model 
  print("Saving model to "+save_path)
  act.save(save_path)

def test(env,load_path,num_episodes=100):
  act = deepq.load(load_path)
  success_count=0.0
  for i in range(num_episodes):
      obs, done = env.reset(), False
      episode_rew = 0.0
      while not done:
          env.render()
          obs, rew, done, _ = env.step(act(obs[None])[0])
          episode_rew += rew
      env.render()    
      if(episode_rew > -env.n):
        print("Episode successful with reward ",episode_rew)
        success_count+=1.0
      else:
        print("Episode unsuccessful with reward ",episode_rew)
  success_rate = success_count/num_episodes
  print("Success Rate: ",success_rate)
  return success_rate

def main(n_list=[5,10],  space_seed_list=[0]):
  results_file = open("test_results","w")
  for n in n_list:
    for space_seed in space_seed_list:
        print("started for "+str(n)+","+str(space_seed))
        env = make_env(n,space_seed)
        path = "bitflip"+str(n)+":"+str(space_seed)+".pkl"
        with tf.Graph().as_default():
            train(env,path)
        with tf.Graph().as_default():
            success_rate = test(env,path) 
            results_file.write(str(n)+","+str(space_seed)+","+str(success_rate)+"\n")
  results_file.close()
