
import bluetooth

bd_addr = "98:D3:31:90:12:02"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello MAK!!\r\n")

sock.close() 
