from machine import Pin
from time import *

in1 = Pin(23, Pin.OUT)
in2 = Pin(22, Pin.OUT)
in3 = Pin(21, Pin.OUT)
in4 = Pin(19, Pin.OUT)

def pasos(v1, v2, v3, v4):
    in1.value(v1)
    in2.value(v2)
    in3.value(v3)
    in4.value(v4)    

def motor_pasos(vel, direccion):
    if direccion == 1:
        pasos(1, 0, 0, 0)
        sleep_ms(vel)
        pasos(0, 1, 0, 0)
        sleep_ms(vel)
        pasos(0, 0, 1, 0)
        sleep_ms(vel)
        pasos(0, 0, 0, 1)
        sleep_ms(vel)
    elif direccion == 2:
        pasos(0, 0, 0, 1)
        sleep_ms(vel)
        pasos(0, 0, 1, 0)
        sleep_ms(vel)
        pasos(0, 1, 0, 0)
        sleep_ms(vel)
        pasos(1, 0, 0, 0)
        sleep_ms(vel)
    else:
        pasos(0, 0, 0, 0)
        
while True:
    motor_pasos(100, 2)      