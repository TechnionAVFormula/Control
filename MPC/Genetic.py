##Optimization Genetic Approch
import math as mat
import numpy as np
import time
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
        self.Target_Value = []
        self.Generation = []
        self.Code = 0
        self.Value = []

    @property
    def Code(self):
        return self.__Code

    @Code.setter
    def Code(self, NumberofBits):
        Code = []
        for _ in range(NumberofBits):
            Code.append(randint(2))
        self.__Code = np.asarray(Code)


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
        self.Resulotion_init = resulotion
        self.Resulotion = []
        self.Controlarguments = controlarguments
        self.argument_bits = []
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

        self.__NumberofBits = NumberofBits

    def Calculate_NumberofBits(self):
        for i in range(self.Controlarguments):
            self.NumberofBits = self.NumberofBits + mat.ceil(
                (
                    mat.log2(
                        np.abs(self.Val_max[i] - self.Val_min[i] + self.Resulotion_init)
                        / self.Resulotion_init
                    )
                )
            )
            self.argument_bits.append(
                mat.ceil(
                    (
                        mat.log2(
                            np.abs(
                                self.Val_max[i] - self.Val_min[i] + self.Resulotion_init
                            )
                            / self.Resulotion_init
                        )
                    )
                )
            )
            self.Resulotion.append(
                (self.Val_max[i] - self.Val_min[i]) / (2 ** (self.argument_bits[i]) - 1)
            )

    def Initialize_Population(self):
        for i in range(self.Number_of_Candidate):
            self.Candidate_List.append(Candidate())
            self.Candidate_List[i].Code = self.NumberofBits
            self.Candidate_List[i].Value = self.Calculate_Value(
                self.Candidate_List[i].Code,
                self.Controlarguments,
                self.argument_bits,
                self.Resulotion,
                self.Val_min,
            )
            while not self.Constraint(self.Candidate_List[i].Value):
                self.Candidate_List[i].Code = self.NumberofBits
                self.Candidate_List[i].Value = self.Calculate_Value(
                    self.Candidate_List[i].Code,
                    self.Controlarguments,
                    self.argument_bits,
                    self.Resulotion,
                    self.Val_min,
                )

    def DNA_fitness(self):
        Min_value = 0
        for i in range(self.Number_of_Candidate):
            self.Candidate_List[i].Target_Value = self.Calculate_Target(
                self.Candidate_List[i].Value
            )
            if i == 0 or Min_value > self.Candidate_List[i].Target_Value:
                Min_value = self.Candidate_List[i].Target_Value
        if Min_value < 0:
            for i in range(self.Number_of_Candidate):
                self.Candidate_List[i].fitness = 1 / (
                    1 + self.Candidate_List[i].Target_Value - Min_value
                )
        else:
            for i in range(self.Number_of_Candidate):
                self.Candidate_List[i].fitness = 1 / (
                    1 + self.Candidate_List[i].Target_Value
                )

    # def Up_date(self):
    #     ProbList = np.array([])
    #     for i in range(self.Number_of_Candidate):

    @staticmethod
    def Calculate_Value(Code, Number_of_arguments, argument_bits, Resulotion, Val_min):
        Value = np.zeros([Number_of_arguments,])
        Running = 0
        for i in range(Number_of_arguments):
            Multi = 2 ** (argument_bits[i] - 1)
            for j in range(Running, argument_bits[i] + Running):
                Value[i] = Value[i] + Code[j] * Multi
                Multi = Multi / 2
            Running = Running + argument_bits[i]
            Value[i] = (Value[i] - 1) * Resulotion[i] + Val_min[i]
        return Value

    @staticmethod
    def Constraint(Control_efforts):
        if np.sum(Control_efforts) > 8:
            return 1
        else:
            return 0

    @staticmethod
    def Calculate_Target(Control_efforts):
        return norm(Control_efforts)


K = DNA(10, np.array([10, 2]), np.array([5, 1]), 1, 2)
K.Calculate_NumberofBits()
tic = time.time()
K.Initialize_Population()
print(time.time() - tic)
K.DNA_fitness()
