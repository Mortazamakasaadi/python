import serial
import sys, time

port=serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
        timeout=1)


while True:
		t=port.read(1)
		print(t)



