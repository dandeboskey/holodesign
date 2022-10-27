import serial
import time
import numpy

arduino = serial.Serial(port='/dev/cu.usbserial-02655245', baudrate=115200, timeout=.1)

def values(x):
    while True:
        line = arduino.readline()
        decoded = line.decode("utf-8")
        if x == 0:
            if 'O' in decoded:
                splitted = decoded.split(',')
                xorient = int(float(splitted[1]))
                yorient = int(float(splitted[2]))
                zorient = int(float(splitted[3]))
                return[xorient, yorient, zorient]
        elif x == 1:
            if 'A' in decoded:
                splitted = decoded.split(',')
                xacc = float(splitted[1])
                yacc = float(splitted[2])
                zacc = float(splitted[3])
                return[xacc, yacc, zacc]
        elif x == 2:
            if 'O' in decoded:
                splitted = decoded.split(',')
                xorient = int(float(splitted[1]))
                yorient = int(float(splitted[2]))
                zorient = int(float(splitted[3]))
                return[xorient, yorient, zorient]
            if 'A' in decoded:
                splitted = decoded.split(',')
                xacc = float(splitted[1])
                yacc = float(splitted[2])
                zacc = float(splitted[3])
                return[xacc, yacc, zacc]

while True:
    values(2)