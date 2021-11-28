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


rvr = SpheroRvrObserver()
red = 0
green = 0
blue = 0

def color_detected_handlers(color_detected_data):
    # Set red, green, and blue as global to be used outside of function
    global red
    global green
    global blue

    # Store the Red, Green, and Blue values
    red = color_detected_data['ColorDetection']['R']
    green = color_detected_data['ColorDetection']['G']
    blue = color_detected_data['ColorDetection']['B']
    
    # Print out colors of Red, Green, and Blue on the terminal
    print("Red: " + str(red))
    print("Green: " + str(green))
    print("Blue: " + str(blue))


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
        time.sleep(1)
        

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.sensor_control.clear()
        
        if red > 150: # If value of red is high
            rvr.set_all_leds(
                led_group=RvrLedGroups.all_lights.value,
                led_brightness_values=[color for _ in range(10) for color in [255, 0, 0]] # Change all LED colors to the color red
        )
        else: # Value of red not high enough, cycle headlights
            counter = 0
            flag = 0
            while counter < 5: # Cycle headlight flashing five times
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
                counter += 1

        # Delay to allow RVR issue command before closing
        time.sleep(.5)
        
        rvr.close()


if __name__ == '__main__':
    main()
