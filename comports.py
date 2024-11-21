import serial.tools.list_ports

# List all available serial ports and check for the Microbit
for port in serial.tools.list_ports.comports():
    if "BBC micro:bit" in port.description:
        print(f"Microbit found on {port.device}")
    else:
        print(f"No Microbit found on {port.device}")
