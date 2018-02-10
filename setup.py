from setuptools import setup

setup(name='gym_BitFlipper',
      version='0.0.1',
      install_requires=['gym>=0.2.3','baselines','custom_baselines'], 
      dependency_links = ['https://github.com/JoyChopra1298/baselines.git#egg=custom_baselines']
)  
