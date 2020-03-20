from typing import NamedTuple, Tuple
from __future__ import annotations

import numpy as np

MAX_SPEED = 80  # max speed is 80 km/h
SAMPLING_RATE = 40  # 40 samples per second


class State(NamedTuple):
    """
    :r_road_bound: (N, 2) shape array of (x,y) coordinates, sampled from right edge of the road [m]
    :l_road_bound: (N, 2) shape array of (x,y) coordinates, sampled from left edge of the road [m]
    :pos: (1, 2) shape array of the vehicle location in the given state (x,y) [m]
    :angle: the angle of the vehicle velocity vector and the road [radians]
    :x_t: terminal x coordinate [m]
    :deviation: position error radius [m]
    :is_course_complete: a flag that indicates whether the vehicle completed a full course path
    :dist_to_end: the distance between the car and the end of the route, if the end of the route is not seen, value will be -1
    :speed: the speed of the car
    """
    deviation: float  # a+b
    x_t: float  # a
    r_road_bound: np.ndarray  # a
    l_road_bound: np.ndarray  # a
    angle: float  # a+b
    pos: np.ndarray  # a+b
    is_course_complete: bool  # a
    dist_to_end: float  # b
    speed: float  # b
    abs_pos: np.ndarray  # a+b
    abs_prev_pos: np.ndarray  # a+b
    prev_angle: float # a+b

    def _convert_to_car_coordinates(self, car_coordinates, ConusCoordinates):
        return (ConusCoordinates[0] - car_coordinates[0],  # x axis
                ConusCoordinates[1] - car_coordinates[1]  # y axis
                )

    def convert_coord_sys(self):
        self.x_t = self.x_t - self.pos[0]
        self.deviation = self.deviation + (1 / SAMPLING_RATE) * self.speed
        for l_cone in self.l_road_bound:
            l_cone = self._convert_to_car_coordinates(self.pos, l_cone)
        for r_cone in self.r_road_bound:
            r_cone = self._convert_to_car_coordinates(self.pos, r_cone)
        self.pos = np.array([0, 0])

    def compare(self, state: State) -> Tuple[bool, bool]:
        a_changed = self.deviation != state.deviation or self.x_t != state.x_t \
                    or self.r_road_bound != state.r_road_bound or self.l_road_bound != state.l_road_bound \
                    or self.angle != state.angle or self.pos != state.pos or self.is_course_complete != state.is_course_complete
        b_changed =  self.deviation != state.deviation or self.angle != state.angle or self.pos != state.pos \
                    or self.dist_to_end != state.dist_to_end or self.speed != state.speed
        return a_changed,b_changed


class InMsg(NamedTuple):
    state: State  # TODO: depends on the system runner from here


class OutMsg(NamedTuple):
    wheel_angle: float
    speed: float


def read_msg_from_q() -> InMsg:
    pass  # TODO: depends on the system runner from here


def write_msg_to_q(out_msg: OutMsg):
    pass  # TODO: depends on the system runner from here
