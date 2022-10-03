# MPIP
# DABM 2022-2

import serial

class Puerto:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate

    def abrir(self):
        puerto = serial.Serial(self.port, self.baudrate)
        self.puerto =puerto

    def leer(self):
        dato = self.puerto.readline().decode().strip()
        return dato