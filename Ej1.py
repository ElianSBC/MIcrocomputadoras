from machine import Pin                 # Trae la herramienta para controlar los pines
import time                             # Trae la herramienta para manejar pausas (tiempos)

sw1_1 = Pin(8, Pin.IN)                  # Configura el GPIO8 como entrada. Aquí está conectado el interruptor SW1

while True:                             # Repite todo lo que sigue para siempre
    if sw1_1.value() == 1:              # Pregunta: ¿el interruptor está cerrado? (lee un 1)
        print("Interruptor cerrado'1'")  # Si está cerrado, muestra este mensaje en la consola
        time.sleep(0.5)                 # Espera medio segundo antes de volver a revisar
    else:                               # Si no está cerrado (lee un 0)
        print("Interruptor abierto'0'")  # Muestra este otro mensaje en la consola
        time.sleep(0.5)                 # Espera medio segundo antes de volver a revisar