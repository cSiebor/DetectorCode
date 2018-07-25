"""Specific module to calculate vacuum pressure"""
import json
import smbus
BUS = smbus.SMBus(1)

with open('sensorConfig.json') as json_file:
    FILE_DATA = json.load(json_file)


class Vacuum(object):
    """Vacuum Sensor GPIO pin 3 and 5"""
    def __init__(self):
        """"""
    def vacuum(self):
        """Specific method to calculate pressure in kPa from bits"""
        l_vp = BUS.read_i2c_block_data(FILE_DATA["vacuum i2c address"],
                                       FILE_DATA["vacuum register address"], 4)
        data_vp = float(((l_vp[0] & 63) << 8) | l_vp[1]) * 15.0 / 16384.0
        return data_vp
