from gym.envs.box2d.car_dynamics import Car
import numpy as np
#orr
SIZE = 0.02
ENGINE_POWER            = 100000000*SIZE*SIZE
WHEEL_MOMENT_OF_INERTIA = 4000*SIZE*SIZE
FRICTION_LIMIT          = 1000000*SIZE*SIZE     # friction ~= mass ~= size^2 (calculated implicitly using density)

class CarInherit(Car):

    def __init__(self, world, init_angle, init_x, init_y):
         Car.__init__(self, world, init_angle, 5, 30)
         self.hull.linearVelocity[1]=100
         self.omega=100
         #self.phase=

    def step(self, dt):
        dicInformation={}
        wheelsSpeed=[]
        generalLimit=0
        generalForce=0
        for w in self.wheels:
            # Steer each wheel
            dir = np.sign(w.steer - w.joint.angle)
        
           # print("the angle is"+w.joint.angle)
            val = abs(w.steer - w.joint.angle)
            w.joint.motorSpeed = dir*min(50.0*val, 3.0)
          
            # Position => friction_limit
            grass = True
            friction_limit = FRICTION_LIMIT*0.6  # Grass friction if no tile
            for tile in w.tiles:
                friction_limit = max(friction_limit, FRICTION_LIMIT*tile.road_friction)
                grass = False
            # Force
            forw = w.GetWorldVector( (0,1) )
            side = w.GetWorldVector( (1,0) )
            v = w.linearVelocity
            vf = forw[0]*v[0] + forw[1]*v[1]  # forward speed
            #print(vf)
         #   print("the forward is:"+str(vf))
            vs = side[0]*v[0] + side[1]*v[1]  # side speed
         #   print("the side is:"+str(vs))
            wheelsSpeed.append([vf,vs,(vf**2+vs**2)**0.5])
            # WHEEL_MOMENT_OF_INERTIA*np.square(w.omega)/2 = E -- energy
            # WHEEL_MOMENT_OF_INERTIA*w.omega * domega/dt = dE/dt = W -- power
            # domega = dt*W/WHEEL_MOMENT_OF_INERTIA/w.omega
            w.omega += dt*ENGINE_POWER*w.gas/WHEEL_MOMENT_OF_INERTIA/(abs(w.omega)+5.0)  # small coef not to divide by zero
            self.fuel_spent += dt*ENGINE_POWER*w.gas

            if w.brake >= 0.9:
                w.omega = 0
            elif w.brake > 0:
                BRAKE_FORCE = 15    # radians per second
                dir = -np.sign(w.omega)
                val = BRAKE_FORCE*w.brake
                if abs(val) > abs(w.omega): val = abs(w.omega)  # low speed => same as = 0
                w.omega += dir*val
            w.phase += w.omega*dt

            vr = w.omega*w.wheel_rad  # rotating wheel speed
           # print(vr) GOOD
            f_force = -vf + vr        # force direction is direction of speed difference
            p_force = -vs

            # Physically correct is to always apply friction_limit until speed is equal.
          
            # But dt is finite, that will lead to oscillations if difference is already near zero.
            f_force *= 205000*SIZE*SIZE  # Random coefficient to cut oscillations in few steps (have no effect on friction_limit)
            p_force *= 205000*SIZE*SIZE
            force = np.sqrt(np.square(f_force) + np.square(p_force))
            # Skid trace
            generalLimit=2.0*friction_limit
            generalForce=abs(force)
            if abs(force) > 2.0*friction_limit:
                if w.skid_particle and w.skid_particle.grass==grass and len(w.skid_particle.poly) < 30:
                    w.skid_particle.poly.append( (w.position[0], w.position[1]) )
                  #  print("the w.skid_particle.poly"+str(len(w.skid_particle.poly)))
    
                elif w.skid_start is None:
                    w.skid_start = w.position
                else:
                    w.skid_particle = self._create_particle( w.skid_start, w.position, grass )
                    w.skid_start = None
            else:
                w.skid_start = None
                w.skid_particle = None

            if abs(force) > friction_limit:
                f_force /= force
                p_force /= force
                force = friction_limit  # Correct physics here
                f_force *= force
                p_force *= force

            w.omega -= dt*f_force*w.wheel_rad/WHEEL_MOMENT_OF_INERTIA

            w.ApplyForceToCenter( (
                p_force*side[0] + f_force*forw[0],
                p_force*side[1] + f_force*forw[1]), True )
        dicInformation['wheelsSpeed']=wheelsSpeed
        avgForwardSpeed=0
        avgSideSpeed=0
        avgGeneralSpeed=0
        for w in wheelsSpeed:
            avgForwardSpeed+=w[0]
            avgSideSpeed+=w[1]
            avgGeneralSpeed+=w[2]
        avgForwardSpeed/=4
        avgSideSpeed/=4
        avgGeneralSpeed/=4
        dicInformation['avgForwardSpeed']=avgForwardSpeed
        dicInformation['avgSideSpeed']=avgSideSpeed
        dicInformation['avgGeneralSpeed']=avgGeneralSpeed
        dicInformation['generalLimit']=generalLimit
        dicInformation['generalForce']=generalForce
        position=[0,0]
        for w in self.wheels:
            position[0]+=w.position[0]
            position[1]+=w.position[1]
        position[0]/=4
        position[1]/=4
        dicInformation["position"]=position
        return dicInformation.copy()

#    def forward_speed():
   #     for w in self.wheels:
            # Force
 #           forw = w.GetWorldVector( (0,1) )
 #           side = w.GetWorldVector( (1,0) )
 #           v = w.linearVelocity
  #          vf = forw[0]*v[0] + forw[1]*v[1]  # forward speed
  #          return vf
    pass