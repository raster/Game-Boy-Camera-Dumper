#!/usr/local/bin/python3

"""\
Capture photos dumped from a Game Boy Camera

---------------------
"""

import serial
import argparse
import time
import os

parser = argparse.ArgumentParser(description='Capture photos dumped from a Game Boy Camera. (pySerial and argparse libraries required)')
parser.add_argument('device_file',
        help='serial device path')
args = parser.parse_args()

print("Ready to read data from " + args.device_file + "\n")

print("When you are done printing your photos press CTRL-C to end the program.\n")

# open an output file
f = open('gbc-output.txt','a')

# open serial port at proper baud rate
ser = serial.Serial(args.device_file,115200)

# flush serial input
ser.flushInput()

try:
    while True:
        str = ser.readline()
        str = str.decode("utf-8")
        print(str, end = '')
        f.write(str)
        f.flush()
except KeyboardInterrupt:
    ser.flushInput()
    pass


# flush the serial port
ser.flushInput()

# close serial port
ser.close()

# close file
f.close()

# end the madness
print("\nTransfer complete!\n")

print("Your images have been saved to gbc-output.txt \n")
