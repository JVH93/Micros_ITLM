from machine import Pin
from time import *
# https://github.com/lemariva/micropython-camera-driver
import camera
import gc

# LED integrado
"""
led_flash = Pin(4, Pin.OUT)
led_flash.on()
sleep(1)
led_flash.off()
"""

def tomar_foto(nombre= 'Foto.jpg', voltear= 1, espejo= 1):    
    camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)    
    #camera.framesize(camera.FRAME_240X240)    
    camera.framesize(camera.FRAME_VGA)    
    camera.flip(voltear)
    camera.mirror(espejo)    
    buf = camera.capture()    
    f = open(nombre, "wb")
    f.write(buf)
    f.close()
    camera.deinit()
    return buf

led_flash = Pin(4, Pin.OUT)
led_flash.on()
gc.collect()
buf = tomar_foto()
sleep(1)
led_flash.off()   
