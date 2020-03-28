from pyFormulaClientNoNvidia import messages
from pyFormulaClientNoNvidia.FormulaClient import FormulaClient, ClientSource, SYSTEM_RUNNER_IPC_PORT

import os

def main(): 
    client = FormulaClient(ClientSource.SERVER, 
        read_from_file=os.devnull, write_to_file='state_est.messages')
    conn = client.connect(SYSTEM_RUNNER_IPC_PORT)
    

    ##### test 1 #####
    _running_id = 1

    l_cone = [[1,2.5],[4,2.6],[6.8,2.2],[10,2.5]]
    r_cone = [[1,-2.8],[3.9,-2.5],[7,-2.8],[10.1,-2.3]]

    # Create state data
    fomula_state = messages.state_est.FormulaState()
    car_state = messages.state_est.CarState()
    # right cone border
    for cone in r_cone:
        state_cone = messages.state_est.StateCone()
        state_cone.cone_id = _running_id
        _running_id += 1
        position = messages.common.Vector2D
        position.x = cone[0]
        position.y = cone[1]
        state_cone.position = position
        fomula_state.right_bound_cones.append(state_cone)
    
    # left cone border
    for cone in l_cone:
        state_cone = messages.state_est.StateCone()
        state_cone.cone_id = _running_id
        _running_id += 1
        position = messages.common.Vector2D
        position.x = cone[0]
        position.y = cone[1]
        fomula_state.left_bound_cones.append(state_cone)

    fomula_state.distance_to_finish = -1
    fomula_state.is_finished = False

    carPosition = messages.common.Vector2D
    carVelocity = messages.common.Vector2D
    carPosition.x = 0
    carPosition.y = 0
    carVelocity.x = 22
    carVelocity.y = 0
    car_state.theta_absolute = 0
    car_state.position = carPosition
    car_state.velocity = carVelocity
    fomula_state.current_state = car_state

    # Create the message wrapper and save to file
    state_est_msg = messages.common.Message()
    state_est_msg.data.Pack(fomula_state)
    conn.send_message(state_est_msg)

    ##### test 2 ##### 
    _running_id = 1

    l_cone = [[1,2.5],[4,2],[6.8,1.4],[10,1]]
    r_cone = [[1,-2.8],[3.9,-2.9],[7,-3.8],[10.1,-3.9]]

    # Create state data
    fomula_state = messages.state_est.FormulaState()
    car_state = messages.state_est.CarState()
    # right cone border
    for cone in r_cone:
        state_cone = messages.state_est.StateCone()
        state_cone.cone_id = _running_id
        _running_id += 1
        position = messages.common.Vector2D
        position.x = cone[0]
        position.y = cone[1]
        state_cone.position = position
        fomula_state.right_bound_cones.append(state_cone)
    
    # left cone border
    for cone in l_cone:
        state_cone = messages.state_est.StateCone()
        state_cone.cone_id = _running_id
        _running_id += 1
        position = messages.common.Vector2D
        position.x = cone[0]
        position.y = cone[1]
        fomula_state.left_bound_cones.append(state_cone)

    fomula_state.distance_to_finish = -1
    fomula_state.is_finished = False

    carPosition = messages.common.Vector2D
    carVelocity = messages.common.Vector2D
    carPosition.x = 0
    carPosition.y = 0
    carVelocity.x = 20
    carVelocity.y = 0
    car_state.theta_absolute = 0
    car_state.position = carPosition
    car_state.velocity = carVelocity
    fomula_state.current_state = car_state

    # Create the message wrapper and save to file
    state_est_msg = messages.common.Message()
    state_est_msg.data.Pack(fomula_state)
    conn.send_message(state_est_msg)

    ##### test 3 ##### TODO: change cone and car position as well as car speed and angle
    _running_id = 1

    l_cone = [[0,10.25],[8.1,8.6],[15,4],[19.6,-2.9]]
    r_cone = [[0,4.25],[5.8,3.1],[10.8,-0.2],[14.1,-5.2]]

    # Create state data
    fomula_state = messages.state_est.FormulaState()
    car_state = messages.state_est.CarState()
    # right cone border
    for cone in r_cone:
        state_cone = messages.state_est.StateCone()
        state_cone.cone_id = _running_id
        _running_id += 1
        position = messages.common.Vector2D
        position.x = cone[0]
        position.y = cone[1]
        state_cone.position = position
        fomula_state.right_bound_cones.append(state_cone)
    
    # left cone border
    for cone in l_cone:
        state_cone = messages.state_est.StateCone()
        state_cone.cone_id = _running_id
        _running_id += 1
        position = messages.common.Vector2D
        position.x = cone[0]
        position.y = cone[1]
        fomula_state.left_bound_cones.append(state_cone)

    fomula_state.distance_to_finish = -1
    fomula_state.is_finished = False

    carPosition = messages.common.Vector2D
    carVelocity = messages.common.Vector2D
    carPosition.x = -0.3
    carPosition.y = 7.25
    carVelocity.x = 22
    carVelocity.y = 0
    car_state.theta_absolute = 0
    car_state.position = carPosition
    car_state.velocity = carVelocity
    fomula_state.current_state = car_state

    # Create the message wrapper and save to file
    state_est_msg = messages.common.Message()
    state_est_msg.data.Pack(fomula_state)
    conn.send_message(state_est_msg)

    
    
    exit_data = messages.server.ExitMessage()
    exit_msg = messages.common.Message()
    exit_msg.data.Pack(exit_data)
    conn.send_message(exit_msg)


if __name__ == '__main__':
    main()
