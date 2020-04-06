#from __future__ import annotations

from dataclasses import dataclass
from typing import NamedTuple, Tuple

import numpy as np

MAX_SPEED = 80  # max speed is 80 km/h
SAMPLING_RATE = 40  # 40 samples per second


@dataclass
class State:
    """
    :deviation: position error radius [m]
    :r_road_bound: (N, 2) shape array of (x,y) coordinates, sampled from right edge of the road [m]
    :l_road_bound: (N, 2) shape array of (x,y) coordinates, sampled from left edge of the road [m]
    :angle: the angle of the vehicle velocity vector and the road [radians]
    :pos: (1, 2) shape array of the vehicle location in the given state (x,y) [m]
    :is_course_complete: a flag that indicates whether the vehicle completed a full course path
    :dist_to_end: the distance between the car and the end of the route, if the end is not seen, value will be -1
    :speed: the speed of the car
    :x_t: terminal x coordinate [m]
    :abs_pos: (1, 2) shape array of the vehicle location in the given state (x,y) [m], will stay in global coordinates
    :abs_prev_pos: (1, 2) shape array of the vehicle prev location in the given state (x,y) [m], in global coordinates
    :prev_angle: the prev angle of the vehicle velocity vector and the road [radians]

    """
    deviation: float  # a+b
    r_road_bound: np.ndarray  # a
    l_road_bound: np.ndarray  # a
    angle: float  # a+b
    pos: np.ndarray  # a+b
    is_course_complete: bool  # a
    dist_to_end: float  # b
    speed: float  # b
    x_t: float = None  # a
    abs_pos: np.ndarray = None  # b
    abs_prev_pos: np.ndarray = None  # b
    prev_angle: float = None  # b

    @staticmethod
    def _convert_to_car_coordinates(car_coordinates, conus_coordinates):
        return (conus_coordinates[0] - car_coordinates[0],  # x axis
                conus_coordinates[1] - car_coordinates[1]  # y axis
                )

    def convert_coord_sys(self) -> State:
        self.x_t = self.x_t - self.pos[0]
        self.deviation = self.deviation + (1 / SAMPLING_RATE) * self.speed
        for l_cone in self.l_road_bound:
            l_cone = self._convert_to_car_coordinates(self.pos, l_cone)
        for r_cone in self.r_road_bound:
            r_cone = self._convert_to_car_coordinates(self.pos, r_cone)
        self.pos = np.array([0, 0])
        return self

    def compare(self, state: State) -> Tuple[bool, bool]:
        a_changed = self.deviation != state.deviation or self.x_t != state.x_t \
                    or self.r_road_bound != state.r_road_bound or self.l_road_bound != state.l_road_bound \
                    or self.angle != state.angle or self.pos != state.pos or self.is_course_complete != state.is_course_complete
        b_changed = self.deviation != state.deviation or self.angle != state.angle or self.pos != state.pos \
                    or self.dist_to_end != state.dist_to_end or self.speed != state.speed
        return a_changed, b_changed


class OutMsg(NamedTuple):
    wheel_angle: float
    speed: float
    gas: float
    breaks: float


def control_state_from_est(state_est):

    deviation = 0.01
    r_road_bound = []
    l_road_bound = []
    for r_cone in state_est.right_bound_cones:
        r_road_bound.append(np.array([r_cone.position.x, r_cone.position.y]))
    for l_cone in state_est.left_bound_cones:
        l_road_bound.append(np.array([l_cone.position.x, l_cone.position.y]))

    angle = state_est.current_state.theta_absolute
    pos = np.array(state_est.current_state.position.x, state_est.current_state.position.y)
    is_course_complete = state_est.is_finished
    dist_to_end = state_est.distance_to_finish
    speed = np.sqrt(state_est.current_state.velocity.x ** 2 + state_est.current_state.velocity.y ** 2)

    return State(deviation=deviation, r_road_bound=np.array(r_road_bound), l_road_bound=np.array(l_road_bound),
                 angle=angle, pos=pos, is_course_complete=is_course_complete, dist_to_end=dist_to_end,
                 speed=speed)
