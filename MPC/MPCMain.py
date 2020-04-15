###
import math as mat
import numpy as np
from numpy.linalg import norm

##Cost function
class Order:
    def __init__(self):
        self.X = 0
        self.Y = 1
        self.Vx = 2
        self.Vy = 3
        self.Theta = 4
        self.Vehicle_Total_Length = 1.535
        self.Vehicle_Rear_Length = 0.7675
        self.Throttle = 0
        self.Steering = 1


class MPC(Order):
    def __init__(self, Time_Delta):
        super().__init__()
        self.State = []
        self.slip_angle = []
        self.Control_Command = []
        self.Rotational_Speed = []
        self.Time_Delta = Time_Delta
        self.Target_Path = np.array([])
        self.Orthogonal_error = []
        self.Predicted_path = []

    @property
    def State(self):
        return self.__State

    @property
    def Target_Path(self):
        return self.__Target_Path

    @State.setter
    def State(self, State):
        self.__State = State

    @Target_Path.setter
    def Target_Path(self, Target_Path):
        self.__Target_Path = Target_Path

    def Kinematic_Model(self):
        # Calculate the absolute velocity
        V_abs = norm(self.State[[self.Vx, self.Vy]])
        # Calculate The slip angle maybe take it from state!!!
        self.Slip_angle = mat.atan2(
            mat.tan(self.Control_Command[self.Steering]) * self.Vehicle_Rear_Length,
            self.Vehicle_Total_Length,
        )
        # Calculate the rotational speed maybe take it from state!!!
        self.Rotational_Speed = (
            V_abs
            * mat.cos(self.Slip_angle)
            * mat.tan(self.Control_Command[self.Steering])
            / self.Vehicle_Total_Length
        )
        # Calculate the process advancement
        advancement = np.array(
            [
                self.Time_Delta * self.State[self.Vx]
                + (self.Time_Delta ** 2)
                / 2
                * mat.cos(self.State[self.Theta] + self.Slip_angle)
                * self.Control_Command[self.Throttle],
                self.Time_Delta * self.State[self.Vy]
                + (self.Time_Delta ** 2)
                / 2
                * mat.sin(self.State[self.Theta] + self.Slip_angle)
                * self.Control_Command[self.Throttle],
                self.Time_Delta
                * mat.cos(self.State[self.Steering] + self.Slip_angle)
                * self.Control_Command[self.Throttle],
                self.Time_Delta
                * mat.sin(self.State[self.Theta] + self.Slip_angle)
                * self.Control_Command[self.Throttle],
                self.Time_Delta * self.Rotational_Speed,
            ],
            dtype="float",
        )
        # Update the state
        self.State = self.State + advancement

    def Target_function(self):
        # calculating the initial error
        # Phi_ref = np.atan2(
        #     self.Target_Path[1, 0] - self.State[self.X],
        #     self.Target_Path[0, 0] - self.State[self.Y],
        # )
        pass


##optimal path function
##constraints
## initial condition
##kinmatic model
##track bounds
##saturation constraints


##dynamic model
##slip constrints
