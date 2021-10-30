#Author: Sphero Inc.
#Modified by: Aaron Goff

# Here we will fix a section of code that is highlighted between lines 23 and 27
# Additionally we will create a loop that will change the colors between lines 43 and 49 - Change the colors in incriments of 50 or more
# YouTube Walk-through: https://www.youtube.com/watch?v=O_B6LGE8Pe8&list=PLBawh3P7dWoURbtf93DZwxW70LuZEBoGz&index=11

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

    try:




# FIX THIS CODE! (Original code)
#red=255
#green=
#blue=
# FIX THIS CODE! (Original code)

# FIX THIS CODE! (Finished)
        # Set int values for red, green, blue, and properly space them
        red=255
        green=0
        blue=0
# FIX THIS CODE! (Finished)




        rvr.wake()

        # Give RVR time to wake up
        time.sleep(2)

	#Turn off LEDs
        rvr.set_all_leds(
            led_group=RvrLedGroups.all_lights.value,
            led_brightness_values=[color for _ in range(10) for color in Colors.off.value]
        )

        # Delay to show LEDs change
        time.sleep(1)




#CREATE LOOP HERE! (Original code)
	# Set LED color
#        rvr.set_all_leds(
#            led_group=RvrLedGroups.all_lights.value,
#            led_brightness_values=[color for _ in range(10) for color in [red, green, blue]]
#        )
#CREATE LOOP HERE! (Original code)

#CREATE LOOP HERE! (Finished)
	# Run loop 6 times setting LED color and increasing green value by 50 each loop
        for i in range(6):
            time.sleep(.5)
            rvr.set_all_leds(
                led_group=RvrLedGroups.all_lights.value,
                led_brightness_values=[color for _ in range(10) for color in [red, green, blue]]
            )
            green += 50
#CREATE LOOP HERE! (Finished)




        # Delay to show LEDs change
        time.sleep(1)

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.close()


if __name__ == '__main__':
    main()
