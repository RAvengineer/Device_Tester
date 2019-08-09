from ArduinoControl import Arduino,sys,os,serial,glob
import subprocess as sp
class SerialPort():
    def __init__(self):
        self.result = []
    
    def get_serial_ports(self):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            x=sp.getoutput('mode')
            l=x.split()
            for i in l:
                if 'COM' in i:
                    ports=i[:-1]
            #ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = ["/dev/"+os.popen("dmesg | egrep ttyACM | cut -f3 -d: | tail -n1").read().strip()]
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
        for port in ports:
            try:
                board = Arduino(port)
                board.exit()
                self.result.append(port)
            except (OSError, serial.SerialException):
                print("Please try in the terminal:\n"
                    + "1. ls -l /dev/ttyACM*\n"
                    + "2. You will get something like: crw-rw---- 1 root dialout 188, 0 5 apr 23.01 ttyACM0\n"
                    + "3. The '0' at the end of ACM might be a different number, or multiple entries might be returned. \n"
                    + "The data we need is 'dialout' (is the group owner of the file).\n"
                    + "4. sudo usermod -a -G dialout $USER")
        return self.result

