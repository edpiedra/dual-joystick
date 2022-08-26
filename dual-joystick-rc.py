#!/usr/bin/env python3 

from ads1115_joystick import Joystick 

joy = Joystick()

while True:
    left, right = joy._get_differential_speed()    
    print("left: {:.4f}, right: {:.4f}".format(left, right))
    
    joy._get_pan_tilt()
    print("pan: {:.4f}, tilt: {:.4f}".format(
        joy.pan_step, joy.tilt_step
    ))