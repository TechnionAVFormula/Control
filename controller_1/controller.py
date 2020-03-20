from action_planner import ActionPlanner
from mediator import State, read_msg_from_q, write_msg_to_q, OutMsg
from route_optimizer import RouteOptimizer


class BasicController:
    def __init__(self):
        self.state: State = None  # TODO: maybe some other initial state?
        self.route_optimizer = RouteOptimizer(state=self.state)
        self.action_planner = ActionPlanner(state=self.state)

    def _update_state(self, state: State):
        state.abs_prev_pos = self.state.abs_pos
        state.prev_angle = self.state.angle
        converted_state = state.convert_coord_sys()
        a_changed, b_changed = converted_state.compare(self.state)
        self.state = converted_state

        if a_changed:
            self.route_optimizer.update_optimal_route(self.state)
            self.action_planner.pp_controller.update_path(self.route_optimizer.get_optimal_route(),self.state.speed)
        if b_changed:
            self.action_planner.update_action(self.state, self.route_optimizer.get_optimal_route())

    def main_loop(self):

        while True:
            # TODO: when to exit loop?
            in_msg = read_msg_from_q()
            state = in_msg.state
            self._update_state(state)

            out_msg = OutMsg(wheel_angle=self.action_planner.new_wheel_angle, speed=self.action_planner.new_speed)
            write_msg_to_q(out_msg)
