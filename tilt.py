import serial

ser = serial.Serial('COM2', 115200)

def get_tilt_data():
    """
    Reads the serial data from the micro:bit and returns the tilt data as a 
    tuple of integers. Expects accelerations data in the form 'ax ay az'.
    """

    # have to read 2 lines to reduce delay... for some reason.
    _    = ser.readline().decode('utf-8').strip() 
    line = ser.readline().decode('utf-8').strip()

    print(line)

    try:
        mgx, mgy, mgz = line.split()
        return int(mgx), int(mgy), int(mgz)
    except ValueError:
        raise ValueError('Expected string of <SPACE> separated floats, got: "' + line + '"')