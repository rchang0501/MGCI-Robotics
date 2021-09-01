#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedDPS, MoveTank, MoveSteering, SpeedPercent

drive = MoveTank(OUTPUT_B, OUTPUT_C)

    
drive.on_for_seconds(left_speed=90,right_speed=90,seconds=10)
