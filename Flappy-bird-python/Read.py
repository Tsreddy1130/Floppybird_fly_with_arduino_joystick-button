import serial
import time

# Open serial port (COM7, 9600 baud)
ser = serial.Serial('COM10', 9600, timeout=1)

time.sleep(2)  # wait for Arduino reset

print("Reading SW pin values...")

while True:
    if ser.in_waiting > 0:
        sw_value = ser.readline().decode('utf-8').strip()
        print("SW Pin:", sw_value)
