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
    def __init__(self):
        self.fitness = []
        self.Generation = []
        self.Code = 0

    @property
    def Code(self):
        return self.__Code

    @Code.setter
    def Code(self, NumberofBits):
        Code = []
        for _ in range(NumberofBits):
            Code.append(randint(2))
        self.__Code = Code


class DNA(Candidate):
    def __init__(
        self, Number_of_Candidate, Val_max, Val_min, resulotion, controlarguments
    ):
        super().__init__()
        self.iteration = 0
        self.Number_of_Candidate = Number_of_Candidate
        self.Candidate_List = []
        self.Val_max = Val_max
        self.Val_min = Val_min
        self.Resulotion = resulotion
        self.Controlarguments = controlarguments
        self.NumberofBits = 0

    @property
    def Number_of_Candidate(self):
        return self.__Number_of_Candidate

    @property
    def NumberofBits(self):
        return self.__NumberofBits

    @Number_of_Candidate.setter
    def Number_of_Candidate(self, Number_of_Candidate):
        self.__Number_of_Candidate = Number_of_Candidate

    @NumberofBits.setter
    def NumberofBits(self, NumberofBits):
        if not mat.ceil(NumberofBits) % 2:
            self.__NumberofBits = mat.ceil(NumberofBits)
        else:
            self.__NumberofBits = mat.ceil(NumberofBits) + 1

    def Calculate_NumberofBits(self):
        self.NumberofBits = (
            mat.log2(np.abs(self.Val_max - self.Val_min) / self.Resulotion)
            * self.Controlarguments
        )

    def Initialize_Population(self):
        for i in range(self.Number_of_Candidate):
            self.Candidate_List.append(Candidate())
            self.Candidate_List[i].Code = self.NumberofBits


# K = DNA(10, 10, 1, 0.1, 2)
# K.Calculate_NumberofBits()
# K.Initialize_Population()
