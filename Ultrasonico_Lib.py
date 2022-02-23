from hcsr04 import HCSR04

sensor = HCSR04(trigger_pin=13, echo_pin=12, echo_timeout_us=1000000)

distance = sensor.distance_cm()

print('Distance:', distance, 'cm')