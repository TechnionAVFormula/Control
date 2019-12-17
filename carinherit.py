from gym.envs.box2d.car_dynamics import Car
class carinherit(Car):
    def forward_speed():
        for w in self.wheels:
            # Force
            forw = w.GetWorldVector( (0,1) )
            side = w.GetWorldVector( (1,0) )
            v = w.linearVelocity
            vf = forw[0]*v[0] + forw[1]*v[1]  # forward speed
            return vf
    pass