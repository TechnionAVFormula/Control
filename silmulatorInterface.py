import gym
import gym
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
from silmulator import CarRacing
class SilmulatorInerface:
    def __init__(num_of_episodes=100,num_of_steps=200 ):
        i=5
        self.environment=CarRacing()
        #self.environment=gym.make('CarRacing-v0')        
        self.observation=self.environment.reset()
        self.numOfEpisodes=num_of_episodes
        self.numOfSteps=num_of_steps
        self.reward=0
        self.done=False
        self.information=0
        self.actualSteering=0
        self.actualSpeed=0
        self.steeringDiagram=[]
        self.speedDiagram=[]
        self.gyroDiagram=[]
        self.actualGyro=0
        self.aps=[]

    def takeTheNextStep(self,action):
        self.environment.render()
        self.observation, self.reward, self.done, self.information = self.environment.step(action)        
        detais=[]
        detais=compute_steering_speed_gyro_abs(bottom_black_bar_bw)
        self.actualSteering=detais[0]
        self.actualSpeed=detais[1]
        self.actualGyro=detais[2]  
        self.speedDiagram.append(self.actualSpeed)
        self.gyroDiagram.append(self.actualGyro)
        self.steeringDiagram.append(self.steeringDiagram)



if __name__ == "__main__":
    pass
           








