#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedDPS, MoveTank, MoveSteering, SpeedPercent
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, LightSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from time import sleep
import sys

# LLight = LightSensor(INPUT_1)
# RLight = LightSensor(INPUT_2)
Lcs = ColorSensor(INPUT_2)
Rcs = ColorSensor(INPUT_3)
sound = Sound()
btn = Button()
drive = MoveTank(OUTPUT_B, OUTPUT_C)
steer = MoveSteering(OUTPUT_B, OUTPUT_C)
MAX_SPEED = 90 # More than 90 is unreliable
TEST_SPEED = 10

def sensordata():
    print("Left cs: {}, Right cs: {}, Color Lcs: {}, Color Rcs: {}".format(Lcs.reflected_light_intensity, Rcs.reflected_light_intensity, Lcs.color_name, Rcs.color_name), file = sys.stderr)

def whiteline():
    lv = Lcs.reflected_light_intensity
    rv = Rcs.reflected_light_intensity
    if (lv > 50) or (rv > 50):
        return True

def move_until_reverse():
    lv = Lcs.reflected_light_intensity
    rv = Rcs.reflected_light_intensity
    if lv < 50 and rv < 50:
        drive.on(left_speed=MAX_SPEED, right_speed=MAX_SPEED)    
    else:
        return

while not btn.any():
    sensordata()
    if Lcs.color_name == "Black" and Rcs.color_name == "Black":
        drive.on(left_speed=TEST_SPEED, right_speed=TEST_SPEED)
    elif Lcs.color_name == "White" or Rcs.color_name == "White":
        drive.on_for_degrees(left_speed=-1 * TEST_SPEED, right_speed=-1 * TEST_SPEED, degrees = 50)


        