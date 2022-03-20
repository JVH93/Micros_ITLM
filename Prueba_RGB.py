from machine import PWM, Pin # Importar la función PWM y  Pin del módulo machine
from time import *

verde = PWM(Pin(18)) # El pin del RGB rojo está en el GPIO 18 
azul = PWM(Pin(5)) # El pin del RGB azul está en el GPIO 5
rojo = PWM(Pin(19)) # El pin del RGB verde está en el GPIO 19

def rgb (r, g, b): # Función para controlar RGB
    rojo.duty(r)
    verde.duty(g)
    azul.duty(b)    
    
def recorrido(): # Cambio de intensidad de cada color 
    for i in range (255):
        rgb (i, 0, 0)
        print(i)
        sleep_ms(10)
    for i in range (255):
        rgb (0, i, 0)
        print(i)
        sleep_ms(10)
    for i in range (255):
        rgb (0, 0, i)
        print(i)
        sleep_ms(10)

def arcoiris(tiempo): # https://guiasistem.com/codigos-de-colores-del-arco-iris-de-vibgyor/
    rgb(255,0,0) # Rojo
    sleep(tiempo)
    rgb(255,127,0) # Naranja
    sleep(tiempo)
    rgb(255,255,0) # Amarillo
    sleep(tiempo)
    rgb(0,255,0) # Verde
    sleep(tiempo)
    rgb(0,0,255) # Azul
    sleep(tiempo)
    rgb(75,0,130) # Indigo
    sleep(tiempo)
    rgb(148,0,211) # Violeta
    sleep(tiempo)
        
    
while True:
    recorrido()
    rgb(0,0,0)
    sleep(1)
    rgb(255,255,255)
    sleep(1)
    rgb(0,0,0)
    arcoiris(1)
