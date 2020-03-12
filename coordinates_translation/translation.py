
MAX_SPEED = (80/3.6)  # max speed is 80 km/h, convert to m/s
SAMPLING_RATE = 40  # 40 samples per second


def convertToCarCoordinates(carCoordinates, ConusCoordinates, velocity=MAX_SPEED, ignoreSpeed=False):
    # define the deviation because of the car's speed
    car_speed_deviation = (1/SAMPLING_RATE)*velocity
    if ignoreSpeed:
        car_speed_deviation = 0
    return (ConusCoordinates[0] - carCoordinates[0],  # x axis
            ConusCoordinates[1] - carCoordinates[1],  # y axis
            car_speed_deviation + ConusCoordinates[2] + carCoordinates[2]  # deviation
            )
