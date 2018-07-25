"""Specific module to calculate dust concentration"""
import serial
import json

with open('sensorConfig.json') as json_file:
    FILE_DATA = json.load(json_file)

ARDUINO = serial.Serial(FILE_DATA["serial number"],
                        FILE_DATA["serial baudrate"])


class Dust(object):
    """Dust Concentration Sensor connected over Arduino"""
    def __init__(self):
        """"""
    def dust(self):
        """Specific method to get the dust concentration in ug/m^3"""
        data_d = ARDUINO.readline()
        return data_d
