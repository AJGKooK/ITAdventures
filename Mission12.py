# Created by Sphero Inc.
# Modified by Aaron Goff

import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import RvrStreamingServices
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups

# Reference RVR Observer
rvr = SpheroRvrObserver()

# Printing color values from JSON
def color_detected_handlers(color_detected_data):

    # Print out colors of Red, Green, and Blue on the terminal
    print("Red: " + str(color_detected_data['ColorDetection']['R']))
    print("Green: " + str(color_detected_data['ColorDetection']['G']))
    print("Blue: " + str(color_detected_data['ColorDetection']['B']))

# Start main
def main():
    try:
        rvr.wake()

        # Give RVR time to wake up
        time.sleep(2)

        rvr.enable_color_detection(is_enabled=True)
        rvr.sensor_control.add_sensor_data_handler(
            service=RvrStreamingServices.color_detection,
            handler=color_detected_handlers
        )
        rvr.sensor_control.start(interval=250)

        # Allow this program to run for 0.5 seconds
        time.sleep(.5)
        
        rvr.set_all_leds(
        led_group=RvrLedGroups.all_lights.value,
        led_brightness_values=[color for _ in range(10) for color in [red, green, blue]]
        )

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.sensor_control.clear()
        # Delay to allow RVR issue command before closing
        time.sleep(.5)
        rvr.close()

# Program starts here
if __name__ == '__main__':
    main()