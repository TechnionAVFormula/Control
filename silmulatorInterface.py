import gym
import gym
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
from silmulator import *
import time
class SilmulatorInerface:
    def __init__(self,num_of_episodes=10,num_of_steps=1000,environment=""):
        self.environment=CarRacing()
        self.observation=self.environment.reset()
        self.numOfEpisodes=num_of_episodes
        self.numOfSteps=num_of_steps
        self.reward=0
        self.information={}
        self.done=False
        self.f = open("state.log","a+")
        self.f.write("State n. | Speed | Steer | Score | AngularSpeed | time \n")
        self.f.close

    def takeTheNextStep(self,action):
        """take the next step, the value
         Parameters
        ----------
        action : list 
            [steer,gas,break]
            steer- the values in range[-1 -left, 1 - right]   
            gas-the values in range[0 - low, 1 - high]
            brake-the values in range[0 - low, 1 - high]   
        """
        start=time.time()
        self.environment.render()
        self.observation, self.reward, self.done, self.information = self.environment.step(action)
        end=time.time()
        self.f = open("state.log","a+")
        self.f.write(str(i)+"    |"+str(mySilmulator.getActualSpeed())+
        "   |" + str(mySilmulator.getSteeringWheel())+"   |"+
        str(mySilmulator.getScore())+"  |"+str(mySilmulator.getAngularVelocity())
        +"  |"+str(end-start)+"     \n")
        self.f.close
    def getCenterVec(self):
        return self.environment.getCenterVec()
    def getNumOfSteps(self):
        return self.numOfSteps

    def getForwadSpeedWheelSpeed(self,wheel):           
        """Return the forward wheel's speed of the car - the values in range [0,100]"""        
        return self.information["wheelsSpeed"][wheel][0]

    def getSideSpeedWheelSpeed(self,wheel):

        """Return the side wheel's speed of the car - the values in range [0,100]"""        
        return self.information["wheelsSpeed"][wheel][1]    

    def getAvgWheelSpeed(self,wheel):      
        """Return the general wheel's speed of the car - the values in range [0,100]""" 
        return self.information["wheelsSpeed"][wheel][2]


    def getAngularVelocity(self):
        """Return the Velocity angles of the car - the values in range [-10-left,10-right]"""
        return self.information["angularVelocity"]

    def getSlide(self):
        """Return the limit force and the force of the car
        - if the car's force>limit force then the car may slip"""
        return self.information['generalLimit'],self.information['generalForce']


    def getScore(self):
        """Return the actual reward"""
        return  self.reward 

    def getActualSpeed(self):
        """Return the actual speed- the values in range [0 ,100]"""
        return self.information["actualSpeed"]    

    def getSteeringWheel(self):
        """Return the steering wheel the values in range [-4.2 left,4.2 right]"""
        return self.information["steeringWheel"]
    def getPosition(self):
        return self.information["position"]    

if __name__ == "__main__":
    mySilmulator=SilmulatorInerface()
    for i in range(0,mySilmulator.getNumOfSteps()):
        mySilmulator.takeTheNextStep([0,0,0])
        print(mySilmulator.getPosition())
        #log insert
     #   print("the getForwadSpeedWheelSpeed is"+str(mySilmulator.getForwadSpeedWheelSpeed(1)))
     #   print("the Averege Speed is"+str(mySilmulator.getAvgGeneralSpeed()))
        #print("the slide is"+str(mySilmulator.getSlide()))
      #  print("the angles is"+str(mySilmulator.getAngle()))
    pass
           



#orian




