from machine import Pin                 # Herramienta para controlar los pines
import time                             # Herramienta para manejar pausas

LED = Pin(0, Pin.OUT, value=0)          # Configura el GPIO0 como salida y lo apaga al inicio
push_S2 = Pin(12, Pin.IN, Pin.PULL_DOWN)  # Configura el GPIO12 como entrada con resistencia interna PULL_DOWN

while True:                             # Ciclo infinito
    if push_S2.value() == 0:            # Si el botón NO está presionado (lee 0)
        LED.value(0)                    # Apaga el LED del GPIO0
        print("Push Button S2 en espera; ... lectura: '1'")  # Muestra mensaje (ojo: el texto dice '1' pero lee 0)
        time.sleep(0.5)                 # Espera medio segundo
    else:                               # Si el botón SÍ está presionado (lee 1)
        LED.value(1)                    # Enciende el LED del GPIO0
        print("Push Button S2 presionado; ... lectura: '0'")  # Muestra mensaje (ojo: el texto dice '0' pero lee 1)
        time.sleep(0.5)                 # Espera medio segundo