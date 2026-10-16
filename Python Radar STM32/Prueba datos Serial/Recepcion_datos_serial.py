import serial
import time
import sys

# Configura el puerto según el que asigne tu sistema operativo (ej. COM3 en Windows, /dev/ttyUSB0 en Linux)
PUERTO_SERIAL = 'COM7' 
BAUD_RATE = 115200

try:
    # Inicialización de la comunicación serial
    conexion = serial.Serial(PUERTO_SERIAL, BAUD_RATE, timeout=1)
    print(f"Conectado a {PUERTO_SERIAL} a {BAUD_RATE} baudios.")
    print("Esperando datos del STM32... (Presiona Ctrl+C para salir)\n")
    
    # Bucle infinito de lectura
    while True:
        if conexion.in_waiting > 0:
            # Lee la línea entrante, decodifica los bytes a texto y elimina espacios/saltos de línea
            dato_crudo = conexion.readline().decode('utf-8').strip()
            
            # Verificación básica para asegurar que la cadena no esté vacía antes de imprimir
            if dato_crudo.isdigit():
                print(f"ADC Promedio Estabilizado: {dato_crudo}")

except serial.SerialException as e:
    print(f"Error abriendo el puerto serial: {e}")
    print("Verifica que el puerto sea correcto y no esté abierto en otro programa (como CubeIDE).")
except KeyboardInterrupt:
    print("\nCaptura finalizada por el usuario.")
finally:
    if 'conexion' in locals() and conexion.is_open:
        conexion.close()
        print("Puerto serial cerrado de forma segura.")
        sys.exit(0)