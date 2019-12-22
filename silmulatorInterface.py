import gym
import gym
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
from silmulator import *

class SilmulatorInerface:
    def __init__(self,num_of_episodes=100,num_of_steps=200):
        self.environment=CarRacing()
        #self.environment=gym.make('CarRacing-v0')        
        self.observation=self.environment.reset()
        self.numOfEpisodes=num_of_episodes
        self.numOfSteps=num_of_steps
        self.reward=0
        self.information={}
        self.done=False

    def takeTheNextStep(self,action):
        self.environment.render()
        self.observation, self.reward, self.done, self.information = self.environment.step(action)
        print("the dic is:")
        print(self.information)

    def getNumOfSteps(self):
        return self.numOfSteps


        

if __name__ == "__main__":
    print("yes!!!!")
    mySilmulator=SilmulatorInerface()
    for i in range(0,mySilmulator.getNumOfSteps()):
        mySilmulator.takeTheNextStep([0,10,0])
    pass
           



#orian




