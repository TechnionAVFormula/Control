

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt,fabs
DELTA_T = 0.2
EPSILON= 10^-1
R = "global"
FIRSTSPEED = "global"
FIRSTDITANCE = 100
FIRSTTIME="global"
FIRSTTIME=True





def _clac_ending_speed_help(dist: float, speed: float):
    if FIRSTDITANCE >= dist - speed * DELTA_T > FIRSTDITANCE * 1 / 2:
        return speed

    if FIRSTDITANCE * 1 / 2 >= dist - 0.95 * speed * DELTA_T > FIRSTDITANCE * 1 / 4:
        return speed * 0.95

    if FIRSTDITANCE * 1/ 4 >= dist - 0.925 * speed * DELTA_T > FIRSTDITANCE * 1 / 8:
        return speed * 0.925

    if FIRSTDITANCE * 1/ 8 >= dist - 0.9 * speed * DELTA_T > FIRSTDITANCE * 1 / 16:
        return speed * 0.9

    if FIRSTDITANCE * 1/ 16 >= dist - 0.875 * speed * DELTA_T > FIRSTDITANCE * 1 / 32:
        return speed * 0.875

    if FIRSTDITANCE * 1/ 32 >= dist - 0.85 * speed * DELTA_T > FIRSTDITANCE * 1 / 64:
        return speed * 0.85

    if FIRSTDITANCE * 1/ 64 >= dist - 0.825 * speed * DELTA_T > FIRSTDITANCE * 1 / 128:
        return speed * 0.825

    if FIRSTDITANCE * 1 / 128 >= dist - 0.8 * speed * DELTA_T > FIRSTDITANCE * 1 / 256:
        return speed * 0.8

    return speed * 0.775






def _clac_ending_speed(dist: float, speed: float):

 if(dist-speed*DELTA_T<EPSILON):
     return 0


 elif FIRSTDITANCE >= dist - speed * DELTA_T > FIRSTDITANCE * 1 / 2:
     return speed

 elif FIRSTDITANCE * 1 / 2 >= dist - 0.95 * speed * DELTA_T > FIRSTDITANCE * 1 / 4:
     return speed * 0.95

 elif FIRSTDITANCE * 1 / 4 >= dist - 0.925 * speed * DELTA_T > FIRSTDITANCE * 1 / 8:
     return speed * 0.925

 elif FIRSTDITANCE * 1 / 8 >= dist - 0.9 * speed * DELTA_T > FIRSTDITANCE * 1 / 16:
     return speed * 0.9

 elif FIRSTDITANCE * 1 / 16 >= dist - 0.875 * speed * DELTA_T > FIRSTDITANCE * 1 / 32:
     return speed * 0.875

 elif FIRSTDITANCE * 1 / 32 >= dist - 0.85 * speed * DELTA_T > FIRSTDITANCE * 1 / 64:
     return speed * 0.85

 elif FIRSTDITANCE * 1 / 64 >= dist - 0.825 * speed * DELTA_T > FIRSTDITANCE * 1 / 128:
     return speed * 0.825

 elif FIRSTDITANCE * 1 / 128 >= dist - 0.8 * speed * DELTA_T > FIRSTDITANCE * 1 / 256:
     return speed * 0.8


 return speed * 0.775


if __name__ == '__main__':

    speedList=[]
    distanceList=[]
    distance = 75
    speed = 80/3.6
    is_first_time= True
    speedList.append(speed)
    distanceList.append(distance)
    while( distance> 0 and speed > 0) :
        speed =_clac_ending_speed(distance,speed)
        distance = distance-DELTA_T*speed
        speedList.append(speed)
        distanceList.append(distance)
        print("the speed is"+str(speed))
        print("the dist is"+str(distance))

    fig, ax = plt.subplots()
    ax.plot(distanceList,speedList)


    ax.set(ylabel='speed', xlabel='distance',
       title='About as simple as it gets, folks')
    ax.grid()
    plt.show()