import math
import numpy as np
from sympy import solve
from sympy.abc import x

class PurePursuitController:
    """[this a class to define a controller object of a pure pursuite controller
        
        the controller gets
            the current state of the car(x,y coordinates, velocity and current angle),
            the currnet path that the car should follow
        and then calculates the steering angle requiered to course correct according to the car's velocity
        in order to update the data in the controller it's update methods need to be called.]
    
    Returns:
        calculate_steering [double] -- [the requierd steering angle in radians to course correct]
    """    

    def __init__(self, car_length=3, kdd=1, max_steering_angle=24, poly_fit_deg=5): # initializes the controller and sets the initial values
        self._car_length = car_length
        self._kdd = kdd
        self._max_steering_angle = max_steering_angle*2*math.pi/360
        self._poly_fit_deg  = poly_fit_deg
        self.path = np.poly1d([0,0,0,0])
        self.coordinates = []
        self.orientation = 0
        self.velocity = 0
            
    def update_state(self, x, y, v, orientation): # update the current state of the car in the controller for calculations
        self.coordinates = [x, y]
        self.velocity = v
        self.orientation = orientation

    def update_path(self, path, v): # update the path for the controller for calculations
        self.path = np.poly1d(path)
        self.update_state(0,0,v,0)

    def calculate_steering(self): # calc the needed steering angle to course correct to the next waypoint
        ld = self.velocity * self._kdd
        look_ahead_point = self._calculate_look_ahead_point(ld)
        # print(look_ahead_point)

        alpha = math.atan2(look_ahead_point[1] - self.coordinates[1], look_ahead_point[0] - self.coordinates[0]) - self.orientation # error angle
        delta = 1/math.atan2(2*self._car_length*math.sin(alpha), ld)
        return (max(delta, -self._max_steering_angle) if (delta < 0) else min(delta, self._max_steering_angle))/(2*math.pi/360)

    def _calculate_look_ahead_point(self, ld):
        x_vec = solve((self.path[3]*x**3 + self.path[2]*x**2 + self.path[1]*x + self.path[0] - self.coordinates[1])**2 + (x - self.coordinates[0])**2 - ld**2, x)
        x_options = []
        for x in x_vec:
            if not np.iscomplex(x):
                if x > self.coordinates[0]:
                    x_options.append(x)
    
        return [x_options[0], self.path.polyval(x_options[0])]

    # def _find_near_point_index(self):
    #     near_point = self.path[0]
    #     near_point_distance = self._point_distance(near_point)
    #     for way_point in self.path:
    #         way_point_distance = self._point_distance(way_point)
    #         if (near_point_distance > way_point_distance):
    #             near_point = way_point
    #             near_point_distance = self._point_distance(near_point)

    #     return self.path.index(near_point)

    def _point_distance(self, point):
        return math.sqrt((self.coordinates[0] - point[0])**2 + (self.coordinates[1] - point[1])**2)

    # def _target_point_index(self, x_vector, y_vector, distance):
    #     for point_index in range(len(x_vector)):
    #         # print("limited path: " + str([x_vector[point_index], y_vector[point_index]]))
    #         if(self._point_distance([x_vector[point_index], y_vector[point_index]]) > distance):
    #             # alpha = math.atan2(y_vector[point_index] - self.coordinates[1], x_vector[point_index] - self.coordinates[0]) - self.orientation
    #             # if(abs(alpha)<((math.pi)/2)):   # making sure the chosen look ahead point is not behind the car
    #                 return point_index
    #     return (len(x_vector)-1)


