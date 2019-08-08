import sys
import os
import serial
import glob

try:
    from pyfirmata import Arduino,util
except:
    os.system('pip install pyfirmata')
    from pyfirmata import Arduino,util