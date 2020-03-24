import numpy as np

from mediator import State

from math import sqrt
A_MAX = 0.9
DELTA_T = 0.2
EPSILON= 10^-3
FIRSTDITANCE = 100
FIRSTTIME="global"
FIRSTTIME=True


class ActionPlanner:
    def __init__(self, state: State):
        self.new_wheel_angle = None
        self.new_speed = None
        self.state = state
        self.is_first_time = True

    def update_action(self, state: State, p: np.ndarray):
        self.state = state
        self._calc_speed(p)
        self._calc_wheel_ang(self.state)

    def _calc_wheel_ang(self, state: State):
        self.new_wheel_angle = min(self._wheel_angle_upper_bound(state.speed, self.new_speed), ) #TODO: how to add the p.p out ang

    def _calc_speed(self, p: np.ndarray):
        if self.state.dist_to_end < 0:
            self.new_speed = self._speed_upper_bound(p)
        else:
            # calculate R
            self.new_speed = self._clac_ending_speed(self.state.dist_to_end, self.state.speed)

    def _clac_ending_speed(self, dist: float, speed: float):

        global FIRSTDITANCE
        global FIRSTTIME
        if FIRSTTIME:
            FIRSTTIME = True
            FIRSTDITANCE = dist

        if (dist - speed * DELTA_T < EPSILON):
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
    def _speed_upper_bound(self, p: np.ndarray):
        road = lambda x: p[0] * x ** 3 + p[1] * x ** 2 + p[2] * x + p[3]
        road_dx = lambda x: 3 * p[0] * x ** 2 + 2 * p[1] * x + p[2]
        road_d2x = lambda x: 6 * p[0] * x + 2 * p[1]

        # radius of curvature
        rc = lambda x: abs(1 + road_dx(x) ** 2) ** (3 / 2) / abs(road_d2x(x))
        # fastest velocity without sliding
        v = lambda x: np.sqrt(A_MAX * rc(x))

        return v  # it is a function of x, gives the maximal speed allowed without sliding

    def _wheel_angle_upper_bound(self, old_speed: float, new_speed: float):
        return np.arctan(DELTA_T * (old_speed + new_speed) * 0.5 / (new_speed * new_speed / A_MAX))

