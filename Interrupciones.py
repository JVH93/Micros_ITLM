""" INTERRUPCIONES CON EL ESP32 """
# Importar módulos  necesarios 
from machine import Pin, Timer # En Pin tenemos las externas y en Timer el temporizador
import time as t # Manejo de retardos y cronómetros 


# Definir pines de entradas y salidas

led_rojo = Pin(27, Pin.OUT)
led_azul = Pin(14, Pin.OUT)
led_amarillo = Pin(26, Pin.OUT)

sw = Pin(25, Pin.IN, Pin.PULL_DOWN)


# Definir funciones de interrupción 

def int_ext(pin):
    print(f"Se activó la interrupción externa del pin: {pin}")
    if led_amarillo.value():
        led_amarillo.off()
    else:
        led_amarillo.on()
  

def desborde(timer):
    print(f"Se desbordó el timer {timer}")
    if led_azul.value():
        led_azul.off()
    else:
        led_azul.on()


# Interrupciones externas 

# Pin.irq(handler=None, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, *, priority=1, wake=None, hard=False)
sw.irq(trigger=Pin.IRQ_RISING, handler=int_ext) # Inturrupción externa con flanco de subida 


# Interrupción por temporizador 
# Timer.init(*, mode=Timer.PERIODIC, period=- 1, callback=None)

temp= Timer(0) # Declarar el temporizador a utlizar 
temp.init(period= 100, mode=Timer.PERIODIC, callback=desborde)


while True:
    print("Led rojo")
    led_rojo.on()
    t.sleep(2)
    led_rojo.off()
    t.sleep(3)

