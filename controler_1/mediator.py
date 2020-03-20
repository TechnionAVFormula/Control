from typing import NamedTuple, Tuple
from __future__ import annotations

import numpy as np


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

    def convert_coord_sys(self) -> State:
        pass  # TODO: depends on the system runner from here

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
