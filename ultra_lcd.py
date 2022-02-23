from machine import Pin
from esp32_gpio_lcd import GpioLcd
from utime import sleep_ms, ticks_ms
from hcsr04 import HCSR04
import time as t

lcd = GpioLcd(rs_pin=Pin(4), enable_pin=Pin(15),d4_pin=Pin(5),d5_pin=Pin(18),
d6_pin=Pin(21),d7_pin=Pin(22),num_lines=2, num_columns=16)

sensor = HCSR04(trigger_pin=13, echo_pin=12, echo_timeout_us=1000000)


while True:
    distance = sensor.distance_cm()
    #print('Distance:', distance, 'cm')
    lcd.move_to(0, 0)
    lcd.putstr(str(distance))    
    t.sleep_ms(800)
    #lcd.clear()