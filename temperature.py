"""Specific module to calculate temperature"""
import json
from sht_sensor import Sht

with open('sensorConfig.json') as json_file:
    FILE_DATA = json.load(json_file)

SHT = Sht(FILE_DATA["sht sensor pin numbers 1"], FILE_DATA["sht sensor pin numbers 2"])


class Temperature(object):
    """Temperature Sensor GPIO pin 11 and 13"""
    def __init__(self):
        """"""
    def temperature(self):
        """Specific method to get temperature in degrees C"""
        return SHT.read_t()
