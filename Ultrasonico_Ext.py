from machine import Pin
import time 


trig = Pin(13, Pin.OUT)
echo = Pin(12, Pin.IN)
distancia = duracion = inicio = fin = 0

def ultra():  
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()
    global distancia, inicio, fin, duracion
    while  echo.value() == 0:
        inicio = time.ticks_us()
    while echo.value() == 1:
        fin = time.ticks_us()
        duracion = fin - inicio
        distancia = (duracion * 0.0343)/2
    return distancia 



while True:
    print(("Distancia: {} cm".format(ultra())))
    time.sleep_ms(100)
