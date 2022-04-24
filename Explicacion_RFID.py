# https://youtu.be/G7aQB6x0LHc?t=566
# https://youtu.be/1vfiKUIwZds

# https://docs.micropython.org/en/latest/esp32/quickref.html#software-spi-bus
# https://docs.micropython.org/en/latest/esp32/quickref.html#hardware-spi-bus
# https://docs.micropython.org/en/latest/library/machine.SPI.html#machine-spi

# https://github.com/cefn/micropython-mfrc522
# https://programarfacil.com/blog/arduino-blog/lector-rfid-rc522-con-arduino/

from machine import Pin, SPI 
import mfrc522
from time import *

spi = SPI(2, baudrate=2500000, polarity=0, phase=0)
spi.init()
rdr = mfrc522.MFRC522(spi=spi, gpioRst=13, gpioCs=5)
led = Pin(2, Pin.OUT)

def leer_id():
    Tarjeta = 'None'
    while Tarjeta == 'None':
        print("Coloca la tarjeta")
        (stat, tag_type) = rdr.request(rdr.REQIDL)    
        if stat == rdr.OK:
            (stat, raw_uid) = rdr.anticoll()
            if stat == rdr.OK:
                #print("Tarjeta detectada")
                #print("type: 0x%02x" % tag_type)
                Tarjeta = ("uid: 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1],
                                                        raw_uid[2], raw_uid[3]))            
                return Tarjeta            
        #return "No se detecta nada" 
        sleep(0.5)
    
def comparar_id(tro = "uid: 0xd9e0fb4e", trl = " "):
    if tro == trl:
        #print("Coincide")
        led.on()
    else:
        #print("No coincide")
        led.off()

def escribir_sector(direc = 1, datos = bytearray(16)):
    while True:
        print("Coloque la tarjeta para cambiar su información")      
        if type(datos) == type('str'):
            if len(datos) == 16:
                dat = bytes(datos, 'utf-8')
            else:
                completa = datos + " " * (16 - len(datos))
                dat = bytes(completa, 'utf-8')
        elif type(datos) == type(bytearray(1)):
            dat = datos
        else:
            dat = bytearray(datos)      
        (stat, tag_type) = rdr.request(rdr.REQIDL)
        if stat == rdr.OK:
            (stat, raw_uid) = rdr.anticoll()
            if stat == rdr.OK:
                print("Tarjeta detectada")
                print("  - tag type: 0x%02x" % tag_type)
                print("  - uid: 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1],
                                                       raw_uid[2], raw_uid[3]))
                print("")
                if rdr.select_tag(raw_uid) == rdr.OK:
                    key = b'\xff\xff\xff\xff\xff\xff'                
                    if rdr.auth(rdr.AUTHENT1A, direc, key, raw_uid) == rdr.OK:
                        stat = rdr.write(direc, dat)
                        rdr.stop_crypto1()
                        if stat == rdr.OK:
                            print("Datos escritos en la tarjeta")
                            led.on()
                            sleep(2)
                            break
                        else:
                            print("Proceso de escritura fallido")
                    else:
                        print("Error de autenticación")
                else:
                    print("Falla con el Tag")
                
def leer_sectores():
    while True:
        print("Coloca tarjeta a leer")
        (stat, tag_type) = rdr.request(rdr.REQIDL)
        if stat == rdr.OK:
            (stat, raw_uid) = rdr.anticoll()
            if stat == rdr.OK:
                print("Tarjeta detectada")
                print("type: 0x%02x" % tag_type)
                print("uid: 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1],
                                                   raw_uid[2], raw_uid[3]))
                print("")
                if rdr.select_tag(raw_uid) == rdr.OK:
                    key = b'\xff\xff\xff\xff\xff\xff'
                    ms = ticks_ms()
                    blockArray = bytearray(16)
                    for sector in range(0, 64):
                        if rdr.auth(rdr.AUTHENT1A, sector, key, raw_uid) == rdr.OK:
                            rdr.read(sector, into=blockArray)
                            print("datos@%d: %s" % (sector, blockArray))
                        else:
                            print("Error de autenticación")
                            break
                    rdr.stop_crypto1()
                    print("Datos leidos en: " + str(ticks_ms() - ms)) # took 4594 ms
                    break
                else:
                    print("Fallido")

datos_str = "Hola mundo"
escribir_sector(8, datos_str)
#led.off()
#sleep(3)
#tj = leer_id()
#print(tj)
#comparar_id(trl = tj)
#leer_sectores()
    
