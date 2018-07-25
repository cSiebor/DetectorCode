"""Specific module to calculate relative humidity with the sensor"""
import json
from sht_sensor import Sht

with open('sensorConfig.json') as json_file:
    FILE_DATA = json.load(json_file)

SHT = Sht(FILE_DATA["sht sensor pin numbers 1"], FILE_DATA["sht sensor pin numbers 2"])


class RelativeHumidity(object):
    """Relative Humidity Sensor GPIO pin 11 and 13"""
    def __init__(self):
        """"""
    def relative_humidity(self):
        """Specific method to get relative humidity in %RH"""
        return SHT.read_rh()
