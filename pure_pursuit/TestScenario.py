##Path Scenario Creator
import numpy as np
import math as mat
from numpy.random import randint
from numpy.linalg import norm
import matplotlib.pyplot as plt


def ScenarioCreator(NumberofCones, NumberofUTurn, Road_Width, *Path):
    if NumberofCones < NumberofUTurn * 3:
        return print("There are not enough cones!!!")
    if len(Path) == 0:
        Path = randint(500, size=(2, NumberofCones + 2))
    else:
        Path = Path[0]
    L_Cones_Line = np.empty([1, 2])
    R_Cones_Line = np.empty([1, 2])
    BPath = np.empty([2, 1])
    Ind = Path[0].argsort()
    Path = Path[:, Ind]
    for i in range(NumberofUTurn):
        Ind = randint(Path.shape[1] - 1)
        Path[:, [Ind - 1, Ind]] = Path[:, [Ind, Ind - 1]]
    R_perp = np.array([[0, -1], [1, 0]])
    Tval = np.linspace(0, 1, 10)
    Tval = np.array(
        [
            (1 - Tval) ** 3,
            3 * ((1 - Tval) ** 2) * Tval,
            3 * (1 - Tval) * (Tval ** 2),
            Tval ** 3,
        ]
    )
    for i in range(0, Path.shape[1] - 4, 4):
        BPath = np.append(BPath, Path[:, i : i + 4] @ Tval, axis=1)
    BPath = BPath[:, 1:]
    for i in range(1, BPath.shape[1]):
        L_Cones_Line = np.append(
            L_Cones_Line,
            np.array(
                [
                    R_perp
                    @ (BPath[:, i] - BPath[:, i - 1])
                    / norm((BPath[:, i] - BPath[:, i - 1]))
                    * Road_Width
                    + BPath[:, i - 1]
                ]
            ),
            axis=0,
        )
        R_Cones_Line = np.append(
            R_Cones_Line,
            np.array(
                [
                    -R_perp
                    @ (BPath[:, i] - BPath[:, i - 1])
                    / norm((BPath[:, i] - BPath[:, i - 1]))
                    * Road_Width
                    + BPath[:, i - 1]
                ]
            ),
            axis=0,
        )
    L_Cones_Line = L_Cones_Line.T[:, 1:]
    R_Cones_Line = R_Cones_Line.T[:, 1:]
    return BPath, L_Cones_Line, R_Cones_Line


NumberofSigments = 5
NumberofUTurn = 1
Road_Width = 2
BPath, L_Cones_Line, R_Cones_Line = ScenarioCreator(
    NumberofSigments, NumberofUTurn, Road_Width
)
plt.plot(BPath[0, :], BPath[1, :], "g")
plt.plot(L_Cones_Line[0, :], L_Cones_Line[1, :], "or", label="Left Cones")
plt.plot(R_Cones_Line[0, :], R_Cones_Line[1, :], "oy", label="Right Cones")
plt.legend()
plt.show()
