from ArduinoControl import Arduino, util
from ArduinoControl.utils.SerialPort import SerialPort

class arduinoControl():
    def __init__(self):
        port = SerialPort()
        ports = port.get_serial_ports()
        if len(ports)>0:
            self.board = Arduino(ports[0])
            self.iterator = util.Iterator(self.board)
            self.iterator.start()
            self.board.pass_time(1)
    
    def noPortAvailable(self):
        pass
    
    def close(self):
        self.board.exit()
    