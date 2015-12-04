import bluetooth

server_address = "98:D3:31:90:12:02"
# port = get_available_port( RFCOMM )
# noinspection PyBroadException
try:
    sockBluetooth = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sockBluetooth.connect((server_address, 1))
except bluetooth.btcommon.BluetoothError:
    print("Bluetooth Unreachable.")
    exit()
else:
    print("connected")
while 1:
    try:
        data = sockBluetooth.recv(1)
    except bluetooth.btcommon.BluetoothError:
        print("Bluetooth Disconnected.")
        exit()
    if data == '':
        print("Socket broken...")

    if data == b' ':
        print("Connection down...")

    else:

        print("'" + data.decode() + "'" + " received.")

        if data == b'A':
            print(repr(data))
        elif data == b'B':
            print(repr(data))
        elif data == b'C':
            print(repr(data))
        elif data == b'D':
            print(repr(data))

        elif data == b'E':
            print(repr(data))
        elif data == b'F':
            print(repr(data))
        elif data == b'G':
            print(repr(data))
        elif data == b'H':
            print(repr(data))
        elif data == b'I':
            print(repr(data))
        elif data == b'J':
            print(repr(data))
        elif data == b'K':
            print(repr(data))
        elif data == b'L':
            print(repr(data))
        elif data == b'M':
            print(repr(data))
        elif data == b'N':
            print(repr(data))
        elif data == b'O':
            print(repr(data))
        elif data == b'P':
            print(repr(data))

sockBluetooth.close()
sockBluetooth = None
del sockBluetooth
