
from gym.envs.registration import register
#id='BitFlipper-n:space_seed'
register(
    'BitFlipper2-v0',
    entry_point='gym_BitFlipper.envs:BitFlipperEnv',
    max_episode_steps=2,
    kwargs = {"space_seed":0,"n":2}
)
register(
    'BitFlipper5-v0',
    entry_point='gym_BitFlipper.envs:BitFlipperEnv',
    max_episode_steps=5,
    kwargs = {"space_seed":0,"n":5}
)
register(
    'BitFlipper8-v0',
    entry_point='gym_BitFlipper.envs:BitFlipperEnv',
    max_episode_steps=8,
    kwargs = {"space_seed":0,"n":8}
)
register(
    'BitFlipper10-v0',
    entry_point='gym_BitFlipper.envs:BitFlipperEnv',
    max_episode_steps=10,
    kwargs = {"space_seed":0,"n":10}
)
register(
    'BitFlipper15-v0',
    entry_point='gym_BitFlipper.envs:BitFlipperEnv',
    max_episode_steps=15,
    kwargs = {"space_seed":0,"n":15}
)
register(
    'BitFlipper20-v0',
    entry_point='gym_BitFlipper.envs:BitFlipperEnv',
    max_episode_steps=20,
    kwargs = {"space_seed":0,"n":20}
)
register(
    'BitFlipper25-v0',
    entry_point='gym_BitFlipper.envs:BitFlipperEnv',
    max_episode_steps=25,
    kwargs = {"space_seed":0,"n":25}
)
register(
    'BitFlipper30-v0',
    entry_point='gym_BitFlipper.envs:BitFlipperEnv',
    max_episode_steps=30,
    kwargs = {"space_seed":0,"n":30}
)
register(
    'BitFlipper40-v0',
    entry_point='gym_BitFlipper.envs:BitFlipperEnv',
    max_episode_steps=40,
    kwargs = {"space_seed":0,"n":40}
)
register(
    'BitFlipper50-v0',
    entry_point='gym_BitFlipper.envs:BitFlipperEnv',
    max_episode_steps=50,
    kwargs = {"space_seed":0,"n":50}
)

