# Created by Sphero Inc.
# Modified by Aaron Goff

import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import asyncio

from helper_keyboard_input import KeyboardHelper
from sphero_sdk import SerialAsyncDal
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import RvrStreamingServices
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups

# Initialize values
key_helper = KeyboardHelper()
current_key_code = -1
red = 0
green = 0
blue = 0

# Reference asyncio loop & SpheroRvrAsync
loop = asyncio.get_event_loop()
rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)

def keycode_callback(keycode):
    global current_key_code
    current_key_code = keycode
    print("Key code updated: ", str(current_key_code))

# Set global variables for red, green, and blue and print color values from JSON
def color_detected_handlers(color_detected_data):
    global red
    global green
    global blue
    
    red = color_detected_data['ColorDetection']['R']
    green = color_detected_data['ColorDetection']['G']
    blue = color_detected_data['ColorDetection']['B']
    
    # Print out colors of Red, Green, and Blue on the terminal
    print("Red: " + str(red))
    print("Green: " + str(green))
    print("Blue: " + str(blue))

# Activate and gather information from color sensor
async def colorSensor():    
    try:      
        await rvr.enable_color_detection(is_enabled=True)
        await rvr.sensor_control.add_sensor_data_handler(
            service=RvrStreamingServices.color_detection,
            handler=color_detected_handlers
        )
        await rvr.sensor_control.start(interval=250)
        
        # Allow this program to run for 0.5 seconds
        await asyncio.sleep(.5)
        

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')
        breakFlag = 1

    finally:
        await rvr.sensor_control.clear()
        await ledOutput()

# Change LED colors
async def ledOutput():
    try:
        await rvr.set_all_leds(
            led_group=RvrLedGroups.all_lights.value, # All LED lights
            led_brightness_values=[color for _ in range(10) for color in Colors.off.value]
        )

        # Delay to show LEDs change
        time.sleep(1)

        await rvr.set_all_leds(
            led_group=RvrLedGroups.all_lights.value, # All LED lights
            led_brightness_values=[color for _ in range(10) for color in [red, green, blue]]
        )

        # Delay to show LEDs change
        await asyncio.sleep(1)

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        print("Color output successful")

# Start main and create loop
async def main():
    global current_key_code
        
    # Create infinite loop to constantly watch for keyboard inputs
    while True:
        if current_key_code == 122:  # Z - Activate color sensor
            await rvr.wake()
            await colorSensor()

        # reset the key code every loop
        current_key_code = -1

        # sleep the infinite loop for a 10th of a second to avoid flooding the serial port.
        await asyncio.sleep(0.1)

# Run loop
def run_loop():
    global loop
    global key_helper
    key_helper.set_callback(keycode_callback)
    loop.run_until_complete(
        asyncio.gather(
            main()
        )
    )

# Program starts here
if __name__ == "__main__":
    loop.run_in_executor(None, key_helper.get_key_continuous)
    try:
        run_loop()
    except KeyboardInterrupt:
        print("Keyboard Interrupt...")
        key_helper.end_get_key_continuous()
    finally:
        print("Press any key to exit.")
        exit(1)
