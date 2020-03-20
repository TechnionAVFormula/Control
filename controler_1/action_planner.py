import numpy as np

from mediator import State

A_MAX = 0.9
DELTA_T = 0.2


class ActionPlanner:
    def __init__(self, state: State):
        self.new_wheel_angle = None
        self.new_speed = None
        self.state = state

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
            self.new_speed = self._clac_ending_speed(self.state.dist_to_end, self.state.speed)

    def _calc_ending_speed(self, dist: float, speed: float):
        pass #TODO: add or's code

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

