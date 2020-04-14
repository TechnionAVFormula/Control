from pyFormulaClientNoNvidia import messages
from pyFormulaClientNoNvidia.FormulaClient import FormulaClient, ClientSource, SYSTEM_RUNNER_IPC_PORT

from tests.system_runner_tests.utils import print_file, parse_file

import math
import os


def add_list_of_cones_to_state(cones, start_id, cones_state_container):
    for cone in cones:
        state_cone = messages.state_est.StateCone()
        state_cone.cone_id = start_id
        start_id += 1
        position = messages.common.Vector2D()
        position.x = cone[0]
        position.y = cone[1]
        state_cone.position = position
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

<<<<<<< HEAD
    formula_state.current_state.position.x = 0.1
    formula_state.current_state.position.y = 0.1
    formula_state.current_state.velocity.x = 22
    formula_state.current_state.velocity.y = 0.1
    formula_state.current_state.theta_absolute = 0.1
=======
    car_state = messages.state_est.CarState()
    position = messages.common.Vector2D()
    position.x = 0
    position.y = 0
    velocity = messages.common.Vector2D()
    velocity.x = 22
    velocity.y = 0
    car_state.theta = 0
    car_state.position = position
    car_state.velocity = velocity
    car_state.theta_dot = 0
    car_state.steering_angle = 0
    
    formula_state.current_state = car_state

>>>>>>> 912c0c233f8cba87891f02453e258e4a1439a54e

    # Create the message wrapper and save to file
    msg = messages.common.Message()
    msg.data.Pack(formula_state)
    state_est_conn.send_message(msg)

    ##### test 2 #####
    _running_id = 1

    # Create state data

    position.x = 0
    position.y = 0
    velocity.x = 21.04
    velocity.y = 6.43
    car_state.theta = 17*math.pi/180
    car_state.position = position
    car_state.velocity = velocity
    
    formula_state.current_state = car_state


    # Create the message wrapper and save to file
    msg = messages.common.Message()
    msg.data.Pack(formula_state)
    state_est_conn.send_message(msg)

    ##### test 3 #####
    _running_id = 1

    # Create state data

    position.x = 0
    position.y = 1.2
    velocity.x = 22
    velocity.y = 0
    car_state.theta = 0
    car_state.position = position
    car_state.velocity = velocity
    
    formula_state.current_state = car_state

    # Create the message wrapper and save to file
    msg = messages.common.Message()
    msg.data.Pack(formula_state)
    state_est_conn.send_message(msg)

    ##### test 4 #####
    _running_id = 1

    # Create state data

    position.x = 0
    position.y = 1.2
    velocity.x = 20.67
    velocity.y = -7.52
    car_state.theta = -math.pi/9
    car_state.position = position
    car_state.velocity = velocity
    
    formula_state.current_state = car_state


    # Create the message wrapper and save to file
    msg = messages.common.Message()
    msg.data.Pack(formula_state)
    # state_est_conn.send_message(msg)

    ##### test 5 ##### 
    _running_id = 1

    l_cones = [[0, 10.25], [8.1, 8.6], [15, 4], [19.6, -2.9]]
    r_cones = [[0, 4.25], [5.8, 3.1], [10.8, -0.2], [14.1, -5.2]]

    # Create state data
    add_right_and_left_cones_to_state(r_cones, l_cones, formula_state)

    position.x = -0.3
    position.y = 7.25
    velocity.x = 16.425
    velocity.y = 0
    car_state.theta = 0
    car_state.position = position
    car_state.velocity = velocity
    
    formula_state.current_state = car_state

    # Create the message wrapper and save to file
    msg = messages.common.Message()
    msg.data.Pack(formula_state)
    state_est_conn.send_message(msg)

    ##### test 6 ##### 
    _running_id = 1

    # Create state data

    position.x = -0.3
    position.y = 7.25
    velocity.x = 17.45
    velocity.y = -5.34
    car_state.theta = -17*math.pi/180
    car_state.position = position
    car_state.velocity = velocity
    
    formula_state.current_state = car_state

    # Create the message wrapper and save to file
    msg = messages.common.Message()
    msg.data.Pack(formula_state)
    state_est_conn.send_message(msg)

    ##### test 7 ##### 
    _running_id = 1

    # Create state data

    position.x = -0.3
    position.y = 8.6
    velocity.x = 16.425
    velocity.y = 0
    car_state.theta = 0
    car_state.position = position
    car_state.velocity = velocity
    
    formula_state.current_state = car_state

    # Create the message wrapper and save to file
    msg = messages.common.Message()
    msg.data.Pack(formula_state)
    state_est_conn.send_message(msg)

    ##### test 8 ##### 
    _running_id = 1

    # Create state data

    position.x = -0.3
    position.y = 8.6
    velocity.x = 15.975
    velocity.y = -5.814
    car_state.theta = -math.pi/9
    car_state.position = position
    car_state.velocity = velocity
    
    formula_state.current_state = car_state

    # Create the message wrapper and save to file
    msg = messages.common.Message()
    msg.data.Pack(formula_state)
    state_est_conn.send_message(msg)

    ##### test 13 #####
    _running_id = 1

    l_cones = [[1, 2.5], [4, 2.6], [6.8, 2.2], [10, 2.5]]
    r_cones = [[1, -2.8], [3.9, -2.5], [7, -2.8], [10.1, -2.3]]
    # Create state data
    add_right_and_left_cones_to_state(r_cones, l_cones, formula_state)
    
    position.x = 1.5
    position.y = 0
    velocity.x = 0
    velocity.y = 12
    car_state.theta = math.pi
    car_state.position = position
    car_state.velocity = velocity
    
    formula_state.current_state = car_state

    # Create the message wrapper and save to file
    msg = messages.common.Message()
    msg.data.Pack(formula_state)
    state_est_conn.send_message(msg)

    ##### test 15 #####
    _running_id = 1

    l_cones = [[1, 2.5], [4, 2.6], [6.8, 2.2], [10, 2.5]]
    r_cones = [[1, -2.8], [3.9, -2.5], [7, -2.8], [10.1, -2.3]]

    # Create state data
    formula_state = messages.state_est.FormulaState()
    add_right_and_left_cones_to_state(r_cones, l_cones, formula_state)

    formula_state.distance_to_finish = 6

    position.x = 0
    position.y = 0.4
    velocity.x = 20
    velocity.y = 0
    car_state.theta = 0
    car_state.position = position
    car_state.velocity = velocity
    
    formula_state.current_state = car_state

    # Create the message wrapper and save to file
    msg = messages.common.Message()
    msg.data.Pack(formula_state)
    state_est_conn.send_message(msg)

    ##### test 16 #####
    _running_id = 1

    # Create state data

    formula_state.distance_to_finish = -1

    position.x = 0
    position.y = 0.3
    velocity.x = 14.141
    velocity.y = 16.853
    car_state.theta = 5*math.pi/18
    car_state.position = position
    car_state.velocity = velocity
    
    formula_state.current_state = car_state

    # Create the message wrapper and save to file
    msg = messages.common.Message()
    msg.data.Pack(formula_state)
    state_est_conn.send_message(msg)
    
    ##### test 17 ##### 
    _running_id = 1

    l_cones = [[0, -26.25], [5.8, -25], [10.7, -21.8], [14.1, -16.8]]
    r_cones = [[0, -32.25], [8.1, -30.7], [15, -26.1], [19.6, -19.2]]

    # Create state data
    add_right_and_left_cones_to_state(r_cones, l_cones, formula_state)

    position.x = -0.3
    position.y = -29.25
    velocity.x = 10.99
    velocity.y = 12.206
    car_state.theta = 4*math.pi/15
    car_state.position = position
    car_state.velocity = velocity
    
    formula_state.current_state = car_state

    # Create the message wrapper and save to file
    msg = messages.common.Message()
    msg.data.Pack(formula_state)
    # state_est_conn.send_message(msg)

    exit_data = messages.server.ExitMessage()
    exit_msg = messages.common.Message()
    exit_msg.data.Pack(exit_data)
    state_est_conn.send_message(exit_msg)


if __name__ == '__main__':
    main()
    print_file('state_est.messages')
    # print(parse_file('state_est.messages'))
