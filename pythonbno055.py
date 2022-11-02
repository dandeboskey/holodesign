import serial
import time

arduinotime = "Time in ms of arduino serial"
arduino = serial.Serial(port='/dev/cu.usbserial-02655245', baudrate=115200, timeout=.1)

def values(x): 
        line = arduino.readline()
        decoded = line.decode("utf-8")
        if x == 0:
            if 'O' in decoded:
                splitted = decoded.split(',')
                xorient = int(float(splitted[1]))
                yorient = int(float(splitted[2]))
                zorient = int(float(splitted[3]))
                return [xorient, yorient, zorient]
        elif x == 1:
            if 'A' in decoded:
                splitted = decoded.split(',')
                xacc = float(splitted[1])
                yacc = float(splitted[2])
                zacc = float(splitted[3])
                return [xacc, yacc, zacc]
        elif x == 2:
            if 'O' in decoded:
                splitted = decoded.split(',')
                xorient = int(float(splitted[1]))
                yorient = int(float(splitted[2]))
                zorient = int(float(splitted[3]))
                print([xorient, yorient, zorient])
            if 'A' in decoded:
                splitted = decoded.split(',')
                xacc = float(splitted[1])
                yacc = float(splitted[2])
                zacc = float(splitted[3])
                print([xacc, yacc, zacc])

print(values(1))

def calibration():
    positionmat_i = [0,0,0]
    positionmat_f = [0,0,0]
"Calibration function"

"Position matrix"

"Tracking function"
