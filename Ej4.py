from machine import Pin                 # Herramienta para controlar los pines
import time                             # Herramienta para manejar pausas

# Inicializamos todos los LEDs apagados
pines = []                              # Lista para guardar los pines
for i in range(8):                      # Del GPIO0 al GPIO7
    pines.append(Pin(i, Pin.OUT, value=0))  # Configura como salida y los apaga (0)

# Definimos los pines que vamos a usar
LED4 = pines[4]                         # LED en GPIO4
LED5 = pines[5]                         # LED en GPIO5
LED6 = pines[6]                         # LED en GPIO6
LED7 = pines[7]                         # LED en GPIO7
BUZZ = Pin(22, Pin.OUT, value=0)        # Zumbador en GPIO22, empieza apagado
S1 = Pin(11, Pin.IN, Pin.PULL_UP)       # Botón S1 en GPIO11 con resistencia PULL_UP

while True:                             # Ciclo infinito
    if S1.value() == 1:                 # Si el botón NO está presionado (lee 1)
        LED4.value(0)                   # Apaga LED4
        LED5.value(0)                   # Apaga LED5
        LED6.value(0)                   # Apaga LED6
        LED7.value(0)                   # Apaga LED7
        BUZZ.value(0)                   # Apaga el zumbador
        print("Push button S1 liberado, '0'")  # Mensaje en consola
        print("Salidas en bajo")        # Mensaje en consola
        time.sleep(0.5)                 # Espera medio segundo
    else:                               # Si el botón SÍ está presionado (lee 0)
        LED4.value(1)                   # Enciende LED4
        LED5.value(1)                   # Enciende LED5
        LED6.value(1)                   # Enciende LED6
        LED7.value(1)                   # Enciende LED7
        BUZZ.value(1)                   # Enciende el zumbador
        print("Push button S1 presionado, '0'")  # Mensaje en consola
        print("Salidas en alto")        # Mensaje en consola
        time.sleep(0.5)                 # Espera medio segundo