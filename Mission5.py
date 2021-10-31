# Author: Sphero Inc.
# Modified by: Aaron Goff

import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import RvrStreamingServices
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups


rvr = SpheroRvrObserver()


def color_detected_handlers(color_detected_data):
    global red
    global green
    global blue

    red = color_detected_data['ColorDetection']['R']
    green = color_detected_data['ColorDetection']['G']
    blue = color_detected_data['ColorDetection']['B']
    

    print("Red: " + str(color_detected_data['ColorDetection']['R']))
    print("Green: " + str(color_detected_data['ColorDetection']['G']))
    print("Blue: " + str(color_detected_data['ColorDetection']['B']))

#is_valid
#R
#G
#B
#Index
#Confidence


def main():
    """ This program demonstrates how to use the color sensor on RVR (located on the down side of RVR, facing the floor)
        to report colors detected.
    """

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

        # Allow this program to run for 10 seconds
        time.sleep(.5)

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.sensor_control.clear()
        # Delay to allow RVR issue command before closing
        time.sleep(.5)
        

# Cut from set_all_leds
    try:
        rvr.set_all_leds(
            led_group=RvrLedGroups.all_lights.value,
            led_brightness_values=[color for _ in range(10) for color in Colors.off.value]
        )

        # Delay to show LEDs change
        time.sleep(1)

        rvr.set_all_leds(
            led_group=RvrLedGroups.all_lights.value,
            led_brightness_values=[color for _ in range(10) for color in [red, green, blue]]
        )

        # Delay to show LEDs change
        time.sleep(1)

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.close()



if __name__ == '__main__':
    main()
