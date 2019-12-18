from controller import PurePursuitController
import math
import numpy as np
from matplotlib import pyplot

controller = PurePursuitController(3,0.32)
# print(controller._max_steering_angle)
pyplot.xlim(0,700)
pyplot.ylim(-40,600)
state = [0,5,20,(math.pi/4)]
path = []
for i in range(50):
    path.append([12.4*i, 10*i])
    pyplot.plot(path[i][0],path[i][1],'o')
controller.update_state(state[0],state[1],state[2],state[3])
controller.update_path(path)
print(state[0], ", ", state[1], ", ", state[3])
pyplot.arrow(state[0], state[1], 10*math.cos(state[3]), 10*math.sin(state[3]), width=1, head_width=2)
for i in range(30):
    state[3] = state[3] + controller.calculate_steering()/2
    state[0] = state[0] + state[2]*math.cos(state[3])
    state[1] = state[1] + state[2]*math.sin(state[3])
    controller.update_state(state[0],state[1],state[2],state[3])
    print(state[0], ", ", state[1], ", ", (state[3]*180/math.pi))
    pyplot.arrow(state[0], state[1], 10*math.cos(state[3]), 10*math.sin(state[3]), width=1, head_width=2)

pyplot.show()