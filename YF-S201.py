from machine import Pin, Timer


sf = Pin(25, Pin.IN)

np = 0 # Numero de pulsos

reloj = Timer(0)

def conteo(pin):
    global np
    np += 1

def freq(timer):
    global np, Q
    frec = np     
    Q = frec / 7.5    
    print (f"f= {frec} y Q= {Q}")
    np = 0  


sf.irq(trigger = Pin.IRQ_RISING, handler = conteo)
reloj.init(mode= Timer.PERIODIC, period= 1000, callback= freq)

"""
Pulse frequency (Hz) = 7.5Q, Q is flow rate in Litres/minute
Flow Rate (Litres/hour) = (Pulse frequency x 60 min) / 7.5Q

In other words:

Sensor Frequency (Hz) = 7.5 * Q (Liters/min)
Litres = Q * time elapsed (seconds) / 60 (seconds/minute)
Litres = (Frequency (Pulses/second) / 7.5) * time elapsed (seconds) / 60
Litres = Pulses / (7.5 * 60)
Behind The Curtain
"""
