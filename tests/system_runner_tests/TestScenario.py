##Path Scenario Creator
import numpy as np
import math as mat
from numpy.random import rand
from numpy.linalg import norm
import matplotlib.pyplot as plt


def ScenarioCreator(NumberofSigments, UTurn, Road_Width, *Path):
    if NumberofSigments < 3 * (UTurn == "yes"):
        return print("There are not enough cones!!!")
    if len(Path) == 0:
        Path = np.empty([2, NumberofSigments * 4 + 2])
        Path[:, 0] = np.zeros([2,])
        vec = np.array([[5 / 4], [0]])
        for i in range(1, NumberofSigments * 4):
            if UTurn == "yes":
                T = (
                    rand(1) * mat.pi * 1 / NumberofSigments / 2
                    - mat.pi * 1 / NumberofSigments / 16
                )
            elif UTurn == "spline":
                T = (
                    rand(1) * mat.pi * 1 / NumberofSigments * 2
                    - mat.pi * 1 / NumberofSigments
                )
            else:
                T = (
                    rand(1) * mat.pi * 1 / NumberofSigments / 8
                    - mat.pi * 1 / NumberofSigments / 16
                )
            R = np.array([[mat.cos(T), -mat.sin(T)], [mat.sin(T), mat.cos(T)]])
            vec = R @ vec
            Path[:, i] = vec.reshape([2,]) + Path[:, i - 1]
    else:
        Path = Path[0]
    L_Cones_Line = np.empty([1, 2])
    R_Cones_Line = np.empty([1, 2])
    BPath = np.empty([2, 1])
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
    for i in range(1, BPath.shape[1], 10):
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


##Choose number of Cones in the path
##Attention!!! for Uturn 3 is the minimum!!
NumberofSigments = 6
##defult easy path, yes for Uturn and spline for bend path.
UTurn = ["", "yes", "spline"]
for i, mode in enumerate(UTurn):
    Road_Width = 2.5
    BPath, L_Cones_Line, R_Cones_Line = ScenarioCreator(
        NumberofSigments, mode, Road_Width
    )
    plt.subplot(3, 1, i + 1)
    plt.plot(BPath[0, :], BPath[1, :], "g")
    plt.plot(L_Cones_Line[0, :], L_Cones_Line[1, :], "or", label="Left Cones")
    plt.plot(R_Cones_Line[0, :], R_Cones_Line[1, :], "oy", label="Right Cones")
    plt.legend()
    plt.grid()
plt.show()
