"""Specific module to calculate pressure"""
import json
import smbus
BUS = smbus.SMBus(1)

with open('sensorConfig.json') as json_file:
    FILE_DATA = json.load(json_file)


class Pressure(object):
    """Pressure Sensor GPIO pin 3 and pin 5"""
    def __init__(self):
        """"""
    def pressure(self):
        """specific method to calculate pressure in kPa from bits"""
        BUS.write_byte_data(FILE_DATA["pressure i2c address"],
                            FILE_DATA["pressure sensor write register 1"],
                            FILE_DATA["pressure sensor write register 2"])

        l_p = BUS.read_i2c_block_data(FILE_DATA["pressure i2c address"],
                                      FILE_DATA["pressure register address"], 4)
        data_p = (((((l_p[1] * 65536) + (l_p[2] * 256) + (l_p[3] & 240)) / 16) / 4.0) / 1000.0)
        return data_p
