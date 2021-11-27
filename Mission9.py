# Created by Sphero Inc.
# Modified by Aaron Goff

import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups


rvr = SpheroRvrObserver()


def main():
    """ This program demonstrates how to set the all the LEDs.
    """

    flag = 0

    try:
        rvr.wake()

        # Give RVR time to wake up
        time.sleep(2)

        rvr.set_all_leds(
            led_group=RvrLedGroups.all_lights.value,
            led_brightness_values=[color for _ in range(10) for color in Colors.off.value]
        )

        # Delay to show LEDs change
        time.sleep(1)
        # Set red, green, and blue values accordingly
        red = 255
        green = 0
        blue = 0

        rvr.set_all_leds(
            led_group=RvrLedGroups.all_lights.value,
            led_brightness_values=[color for _ in range(10) for color in [red, green, blue]] # Change all LED colors
        )

        # Delay to show LEDs change
        time.sleep(1)
        # Set red, green, and blue values accordingly
        red = 0
        green = 0
        blue = 255

        rvr.set_all_leds(
            led_group=RvrLedGroups.all_lights.value,
            led_brightness_values=[color for _ in range(10) for color in [red, green, blue]] # Change all LED colors
        )

        # Delay to show LEDs change
        time.sleep(1)
        # Set red, green, and blue values accordingly
        red = 0
        green = 255
        blue = 0

        rvr.set_all_leds(
            led_group=RvrLedGroups.all_lights.value,
            led_brightness_values=[color for _ in range(10) for color in [red, green, blue]] # Change all LED colors
        )
        
        while True: # Cycle headlights until terminate command given
            time.sleep(1)
            if flag == 1:
                rvr.set_all_leds(
                    led_group=RvrLedGroups.headlight_right.value, # Set right headlight, flag 1
                    led_brightness_values=[255, 255, 0]
                )        

                rvr.set_all_leds(
                    led_group=RvrLedGroups.headlight_left.value, # Set left headlight, flag 1
                    led_brightness_values=[0, 255, 255]
                )
                flag = 0
            else:
                
                rvr.set_all_leds(
                    led_group=RvrLedGroups.headlight_right.value, # Set right headlight, flag 0
                    led_brightness_values=[0, 255, 255]
                )        

                rvr.set_all_leds(
                    led_group=RvrLedGroups.headlight_left.value, # Set left headlight, flag 0
                    led_brightness_values=[255, 255, 0]
                )
                flag = 1
                
            

        # Delay to show LEDs change
        

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.close()


if __name__ == '__main__':
    main()
