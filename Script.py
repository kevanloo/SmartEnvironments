#!/usr/bin/env python
# -*- coding: utf-8 -*-

HOST = "localhost"
PORT = 4223
UID = "rkQ" # Change XYZ to the UID of your Temperature Bricklet
UID1 = "j6b"
UID2 = "maf"

from ip_connection import IPConnection
from bricklet_temperature import BrickletTemperature
from bricklet_dual_button import BrickletDualButton
from bricklet_ambient_light import BrickletAmbientLight

if __name__ == "__main__":
    ipcon = IPConnection() # Create IP connection
    t = BrickletTemperature(UID, ipcon) # Create device object
    db = BrickletDualButton(UID1, ipcon)
    al = BrickletAmbientLight(UID2, ipcon)

    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    while True:
    # Get current temperature (unit is °C/100)
        temperature = t.get_temperature()
        illuminance = al.get_illuminance()
        
        print("Temperature: " + str(temperature/100.0) + " °C")
        print("Illuminance: " + str(illuminance/10.0) + " Lux")
        
        if((illuminance/10.0)>250):
            y = 2
        else:
            y = 3
        
        if((temperature/100.0)>30):
            x = 2
        else:
            x = 3
           
        db.set_led_state(x,y)
        
    raw_input("Press key to exit\n") # Use input() in Python 3
    ipcon.disconnect()
    