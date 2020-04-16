##Optimization Genetic Approch
import math as mat
import numpy as np
from numpy.linalg import norm
from numpy.random import randint

##resulotion = 1/(2^n-1)*range ---> the resulotion of the argument
##Generation ---> number of optimization iterations
##controlarguments ---> the number of control efforts type
##fitness ---> the probability of the candidate to be choosen
##Code ---> the binary code for the candidate


class Candidate:
    def __init__(self, resulotion, controlarguments):
        self.fitness = []
        self.Generation = []
        self.resulotion = resulotion
        self.controlarguments = controlarguments
        self.Code = controlarguments * resulotion

    @property
    def Code(self):
        return self.__Code

    @Code.setter
    def Code(self, numberofcandidates):
        Code = []
        for i in range(numberofcandidates):
            Code.append(randint(2))
        self.__Code = Code

