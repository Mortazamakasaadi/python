
import serial
import time
# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
)

ser.isOpen()
ooo = ''
time.sleep(1)
#ser.write(b"AT\r\n")
ooo = ser.readline()

print(ooo)
