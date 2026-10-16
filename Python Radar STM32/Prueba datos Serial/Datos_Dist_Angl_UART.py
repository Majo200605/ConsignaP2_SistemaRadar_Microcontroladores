import serial
import time
import sys

PUERTO_SERIAL = 'COM7' 
BAUD_RATE = 115200

try:
    # 1. Creación del objeto serial para abrir la interfaz física
    puerto = serial.Serial(PUERTO_SERIAL, BAUD_RATE, timeout=1)
    
    while True:
        # Se lee del objeto 'puerto', no del string 'PUERTO_SERIAL'
        linea = puerto.readline().decode('utf-8').strip()
        print(f"Crudo recibido: '{linea}'")
        if linea:
            datos = linea.split(',')
            if len(datos) == 2:
                try:
                    angulo_actual = int(datos[0])
                    distancia_actual = float(datos[1])
                    print(f"Angulo: {angulo_actual}°, Distancia: {distancia_actual}")
                except ValueError:
                    # 2. Protección contra tramas corruptas
                    pass

except serial.SerialException as e:
    print(f"Error al abrir el puerto {PUERTO_SERIAL}. Verifica que no esté abierto en otro programa: {e}")
except KeyboardInterrupt:
    print("\nLectura finalizada por el usuario.")
    if 'puerto' in locals() and puerto.is_open:
        puerto.close()