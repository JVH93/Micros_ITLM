from machine import Pin, PWM
from time import *

servo1 = PWM(Pin(2), freq=50) # MG995

def prueba_rango(servo_pin, vmin, vmax, duracion):
    # Para el MG995 es aprox. 18-134 del PWM 
    for i in range (vmin,vmax):
        servo_pin.duty(i)
        print(i)
        sleep(duracion)
    
    for i in range (vmax,vmin,-1):
        servo_pin.duty(i)
        print(i)
        sleep(duracion)

def por_angulo(value, fromLow, fromHigh, toLow, toHigh):
    # https://www.arduino.cc/en/pmwiki.php?n=Reference/Map
    m = (value - fromLow) * (toHigh - toLow) / (fromHigh - toLow) + toLow
    return m

def control_servo(a, servo_pin):
    m = int(por_angulo(a, 0, 180, 18, 122))
    servo_pin.duty(m)
    

#prueba_rango(servo1, 10, 135, 0.1)
#sleep(1)

while True:
    a = int(input("Introduce un ángulo: "))
    control_servo(a, servo1)  