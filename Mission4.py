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
    
    print("is_valid: " + str(color_detected_data['ColorDetection']['is_valid']))
    print("Index: " + str(color_detected_data['ColorDetection']['Index']) + " " + "Confidence: " + str(color_detected_data['ColorDetection']['Confidence']))
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
        rvr.close()


if __name__ == '__main__':
    main()
