from machine import Pin, PWM
import time

# ==========================================
# ACTIVIDAD 5 - Máquina de estados (Tabla 4-3)
# ==========================================

# --- Configuración de entradas (Tabla 4-3) ---
s2    = Pin(12, Pin.IN, Pin.PULL_DOWN)   # S2 en reposo = 0
s1    = Pin(11, Pin.IN, Pin.PULL_UP)     # S1 en reposo = 1
sw1_1 = Pin(8,  Pin.IN)                  # SW1_1
sw1_2 = Pin(9,  Pin.IN)                  # SW1_2
sw1_3 = Pin(10, Pin.IN)                  # SW1_3

# --- Configuración de salidas ---
leds = [Pin(i, Pin.OUT, value=0) for i in range(8)]  # GPIO0..GPIO7 apagados al inicio
buzzer = PWM(Pin(22))                                # Zumbador en GPIO22 como PWM
buzzer.duty_u16(0)                                   # Zumbador apagado al inicio

# --- Función rápida para leer el estado actual de los 5 pines ---
def leer_pines():
    return (s2.value(), s1.value(), sw1_1.value(), sw1_2.value(), sw1_3.value())

# --- Funciones auxiliares ---
def apagar_todo():
    for led in leds:
        led.value(0)
    buzzer.duty_u16(0)

def encender_todo():
    for led in leds:
        led.value(1)
    buzzer.duty_u16(0)

def alternar(valores):
    for i in range(8):
        leds[i].value(valores[i])
    buzzer.duty_u16(0)

# --- Programa principal ---
try:
    while True:
        estado = leer_pines()

        # S2=0, S1=1, SW1_1=0, SW1_2=0, SW1_3=0 → apagar todo
        if estado == (0, 1, 0, 0, 0):
            apagar_todo()

        # S2=0, S1=1, SW1_1=0, SW1_2=0, SW1_3=1 → encender todo
        elif estado == (0, 1, 0, 0, 1):
            encender_todo()

        # S2=0, S1=1, SW1_1=0, SW1_2=1, SW1_3=0 → patrón 01010101
        elif estado == (0, 1, 0, 1, 0):
            alternar([0, 1, 0, 1, 0, 1, 0, 1])

        # S2=0, S1=1, SW1_1=0, SW1_2=1, SW1_3=1 → patrón 10101010
        elif estado == (0, 1, 0, 1, 1):
            alternar([1, 0, 1, 0, 1, 0, 1, 0])

        # S2=0, S1=1, SW1_1=1, SW1_2=0, SW1_3=0 → corredor de GPIO7 a GPIO0
        elif estado == (0, 1, 1, 0, 0):
            for i in range(7, -1, -1):
                if leer_pines() != estado: break
                apagar_todo()
                leds[i].value(1)
                time.sleep(0.15)
            apagar_todo()

        # S2=0, S1=1, SW1_1=1, SW1_2=0, SW1_3=1 → corredor de GPIO0 a GPIO7, buzzer al final
        elif estado == (0, 1, 1, 0, 1):
            for i in range(8):
                if leer_pines() != estado: break
                apagar_todo()
                leds[i].value(1)
                if i == 7:
                    buzzer.freq(1000)
                    buzzer.duty_u16(32768)
                time.sleep(0.15)
            apagar_todo()

        # S2=0, S1=1, SW1_1=1, SW1_2=1, SW1_3=0 → patrón de colisión, buzzer al final
        elif estado == (0, 1, 1, 1, 0):
            pares = [(7, 0), (6, 1), (5, 2), (4, 3)]
            secuencia = pares + list(reversed(pares))
            for idx, (p1, p2) in enumerate(secuencia):
                if leer_pines() != estado: break
                apagar_todo()
                leds[p1].value(1)
                leds[p2].value(1)
                if idx == len(secuencia) - 1:
                    buzzer.freq(1000)
                    buzzer.duty_u16(32768)
                time.sleep(0.15)
            apagar_todo()

        # S2=0, S1=1, SW1_1=1, SW1_2=1, SW1_3=1 → parpadeo (encender/apagar todo)
        elif estado == (0, 1, 1, 1, 1):
            encender_todo()
            time.sleep(0.2)
            apagar_todo()
            time.sleep(0.2)

        # S2=0, S1=0, SW1_1=1, SW1_2=1, SW1_3=1 → contador ascendente 0-9
        elif estado == (0, 0, 1, 1, 1):
            for i in range(10):
                if leer_pines() != estado: break
                apagar_todo()
                for b in range(4):
                    leds[b + 3].value((i >> b) & 1)
                time.sleep(0.5)

        # S2=1, S1=1, SW1_1=1, SW1_2=1, SW1_3=1 → contador descendente 9-0
        elif estado == (1, 1, 1, 1, 1):
            for i in range(9, -1, -1):
                if leer_pines() != estado: break
                apagar_todo()
                for b in range(4):
                    leds[b + 3].value((i >> b) & 1)
                time.sleep(0.5)

        # S2=1, S1=0, SW1_1=1, SW1_2=1, SW1_3=1 → notas musicales
        elif estado == (1, 0, 1, 1, 1):
            apagar_todo()
            for freq in [261, 293, 329, 349, 392]:  # Do, Re, Mi, Fa, Sol
                if leer_pines() != estado: break
                buzzer.freq(freq)
                buzzer.duty_u16(32768)
                time.sleep(0.3)
            buzzer.duty_u16(0)
            time.sleep(0.2)

        else:
            apagar_todo()

        time.sleep(0.01)

except KeyboardInterrupt:
    apagar_todo()
    buzzer.deinit()
    print("\nSaliendo de la Actividad 5...")