from pyFormulaClientNoNvidia import messages
from pyFormulaClientNoNvidia.FormulaClient import FormulaClient, ClientSource, SYSTEM_RUNNER_IPC_PORT

from tests.system_runner_tests.utils import print_file, parse_file

import os


def add_list_of_cones_to_state(cones, start_id, cones_state_container):
    for cone in cones:
        state_cone = messages.state_est.StateCone()
        state_cone.cone_id = start_id
        start_id += 1
        state_cone.position.x = cone[0]
        state_cone.position.y = cone[1]
        cones_state_container.append(state_cone)


def add_right_and_left_cones_to_state(r_cones, l_cones, formula_state):
    _running_id = 1

    # right cone border
    add_list_of_cones_to_state(r_cones, _running_id, formula_state.right_bound_cones)
    # left cone border
    _running_id += len(r_cones)
    add_list_of_cones_to_state(l_cones, _running_id, formula_state.left_bound_cones)


def main():
    # Establish the client:
    state_est_client = FormulaClient(ClientSource.STATE_EST,
                                     read_from_file=os.devnull, write_to_file='state_est.messages')
    state_est_conn = state_est_client.connect(SYSTEM_RUNNER_IPC_PORT)

    ##### test 1 #####
    _running_id = 1

    l_cones = [[1, 2.5], [4, 2.6], [6.8, 2.2], [10, 2.5]]
    r_cones = [[1, -2.8], [3.9, -2.5], [7, -2.8], [10.1, -2.3]]

    # Create state data
    formula_state = messages.state_est.FormulaState()
    add_right_and_left_cones_to_state(r_cones, l_cones, formula_state)

    formula_state.distance_to_finish = -1
    formula_state.is_finished = False

    formula_state.current_state.position.x = 0
    formula_state.current_state.position.y = 0
    formula_state.current_state.velocity.x = 22
    formula_state.current_state.velocity.y = 0
    formula_state.current_state.theta_absolute = 0

    # Create the message wrapper and save to file
    msg = messages.common.Message()
    msg.data.Pack(formula_state)
    state_est_conn.send_message(msg)

    ##### test 2 #####
    _running_id = 1

    l_cones = [[1, 2.5], [4, 2], [6.8, 1.4], [10, 1]]
    r_cones = [[1, -2.8], [3.9, -2.9], [7, -3.8], [10.1, -3.9]]

    # Create state data
    formula_state = messages.state_est.FormulaState()
    add_right_and_left_cones_to_state(r_cones, l_cones, formula_state)

    formula_state.distance_to_finish = -1
    formula_state.is_finished = False

    formula_state.current_state.position.x = 0
    formula_state.current_state.position.y = 0
    formula_state.current_state.velocity.x = 20
    formula_state.current_state.velocity.y = 0
    formula_state.current_state.theta_absolute = 0

    # Create the message wrapper and save to file
    msg = messages.common.Message()
    msg.data.Pack(formula_state)
    state_est_conn.send_message(msg)

    ##### test 3 ##### TODO: change cone and car position as well as car speed and angle
    _running_id = 1

    l_cones = [[0, 10.25], [8.1, 8.6], [15, 4], [19.6, -2.9]]
    r_cones = [[0, 4.25], [5.8, 3.1], [10.8, -0.2], [14.1, -5.2]]

    # Create state data
    formula_state = messages.state_est.FormulaState()
    add_right_and_left_cones_to_state(r_cones, l_cones, formula_state)

    formula_state.distance_to_finish = -1
    formula_state.is_finished = False

    formula_state.current_state.position.x = -0.3
    formula_state.current_state.position.y = 7.25
    formula_state.current_state.velocity.x = 22
    formula_state.current_state.velocity.y = 0
    formula_state.current_state.theta_absolute = 0

    # Create the message wrapper and save to file
    msg = messages.common.Message()
    msg.data.Pack(formula_state)
    state_est_conn.send_message(msg)

    exit_data = messages.server.ExitMessage()
    exit_msg = messages.common.Message()
    exit_msg.data.Pack(exit_data)
    state_est_conn.send_message(exit_msg)


if __name__ == '__main__':
    main()
    print_file('state_est.messages')
    # print(parse_file('state_est.messages'))
