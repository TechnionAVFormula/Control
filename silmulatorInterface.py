import gym
import gym
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
from silmulator import *

class SilmulatorInerface:
    def __init__(self,num_of_episodes=10,num_of_steps=50,environment=""):
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

    def getNumOfSteps(self):
        return self.numOfSteps

    def getForwadSpeedWheelSpeed(self,wheel):           
        #return the wheel's speed in array [forwadSpeed,sideSpeed,(foradSpeed**2+sideSpeed**2)**0.5]
        return self.information["wheelsSpeed"][wheel][0]

    def getSideSpeedWheelSpeed(self,wheel):           
        #return the wheel's speed in array [forwadSpeed,sideSpeed,(foradSpeed**2+sideSpeed**2)**0.5]
        return self.information["wheelsSpeed"][wheel][1]    

    def getAvgWheelSpeed(self,wheel):      
         
        #return the wheel's speed in array [foradSpeed,sideSpeed,(foradSpeed**2+sideSpeed**2)**0.5]
        return self.information["wheelsSpeed"][wheel][2]

   
    # def getAngle(self):
    #     return self.information["angle"]

    def getAngularVelocity(self):
        return self.information["angularVelocity"]

    def getScore(self):
        return  self.reward

    # def getAvgGeneralSpeed(self):
    #    return self.information["avgGeneralSpeed"]     

    def getActualSpeed(self):
        return self.information["actualSpeed"]    

    def getSteeringWheel(self):
        return self.information["steeringWheel"]    

if __name__ == "__main__":
    print("yes!!!!")
    mySilmulator=SilmulatorInerface()
    for i in range(0,mySilmulator.getNumOfSteps()):
        mySilmulator.takeTheNextStep([5,1000,0])
        mySilmulator.takeTheNextStep([0,0,0])
        print("the ActualSpeed is"+str(mySilmulator.getActualSpeed()))
     #   print("the Averege Speed is"+str(mySilmulator.getAvgGeneralSpeed()))
        print("the AvgWheelSpeed is"+str(mySilmulator.getAvgWheelSpeed(1)))


      #  print("the angles is"+str(mySilmulator.getAngle()))
    pass
           



#orian




