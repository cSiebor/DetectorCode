"""Main module that runs continously to monitor
assorted sensors"""

import time
import json
import graphyte
from pressure import Pressure
from vacuum import Vacuum
from dust import Dust
from temperature import Temperature
from relative_humidity import RelativeHumidity

T = Temperature()
P = Pressure()
V = Vacuum()
D = Dust()
RH = RelativeHumidity()

with open('sensorConfig.json') as json_file:
    FILE_DATA = json.load(json_file)

graphyte.init(FILE_DATA["ip address"])  # initializes Grafana to send data to this ip address

RUN = True

while RUN:

    VACUUM_DATA = V.vacuum()
    PRESSURE_DATA = P.pressure()
    DUST_DATA = D.dust()
    TEMPERATURE_DATA = T.temperature()
    RELATIVE_HUMIDITY_DATA = RH.relative_humidity()

    graphyte.send("Vacuum_Pressure_Sensor", VACUUM_DATA)  # sends vacuum pressure data
    graphyte.send("Pressure_Sensor", PRESSURE_DATA)  # sends pressure data
    graphyte.send("Dust_Concentration_Sensor", DUST_DATA)  # sends dust concentration data
    graphyte.send("Temperature_Sensor", TEMPERATURE_DATA)  # sends temperature data
    graphyte.send("Relative_Humidity_Sensor", RELATIVE_HUMIDITY_DATA)  # sends humidity data

    print PRESSURE_DATA + " kPa"
    print VACUUM_DATA + " kPa"
    print DUST_DATA + " ug/m^3"
    print TEMPERATURE_DATA + " degrees C"
    print RELATIVE_HUMIDITY_DATA + " %"

    time.sleep(1)
