# Created by Sphero Inc.
# Modified by Aaron Goff

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import asyncio

from helper_keyboard_input import KeyboardHelper
from sphero_sdk import SerialAsyncDal
from sphero_sdk import SpheroRvrAsync

# initialize global variables
key_helper = KeyboardHelper()
current_key_code = -1
driving_keys = [119, 97, 115, 100, 32]
speed = 0
speedSet = 0
heading = 0
flags = 0

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


def speedChange():
    global speedSet
    if current_key_code == 121: # Y - Speed Up
        speedSet += 64
    elif current_key_code == 104: # H - Speed Down
        speedSet -= 64
        
    if speedSet > 255:
        speedSet = 192
    elif speedSet < 0:
        speedSet = 0
    print('Current Speed: ' + str(speedSet))
        

async def main():
    """
    Runs the main control loop for this demo.  Uses the KeyboardHelper class to read a keypress from the terminal.

    W - Go forward.  Press multiple times to increase speed.
    A - Decrease heading by -10 degrees with each key press.
    S - Go reverse. Press multiple times to increase speed.
    D - Increase heading by +10 degrees with each key press.
    Spacebar - Reset speed and flags to 0. RVR will coast to a stop

    """
    global current_key_code
    global speed
    global heading
    global flags

    await rvr.wake()

    await rvr.reset_yaw()
            
            
    while True:

        if current_key_code == 121: # Y - Speed Up
            speedChange()
        elif current_key_code == 104: # H - Speed Down
            speedChange()
        elif current_key_code == 119:  # W - Forward
            flags = 0
            speed = speedSet
        elif current_key_code == 115:  # S - Reverse
            flags = 1
            speed = speedSet
        elif current_key_code == 97:  # A - Left
            heading -= 15
        elif current_key_code == 100:  # D - Right
            heading += 15

        
        elif current_key_code == 32:  # SPACE - Stop
            # reset speed and flags, but don't modify heading.
            speed = 0
            flags = 0


        # check the heading value, and wrap as necessary.
        if heading > 359:
            heading = heading - 359
        elif heading < 0:
            heading = 359 + heading

        # reset the key code every loop
        current_key_code = -1

        # issue the driving command
        await rvr.drive_with_heading(speed, heading, flags)

        # sleep the infinite loop for a 10th of a second to avoid flooding the serial port.
        await asyncio.sleep(0.1)


def run_loop():
    global loop
    global key_helper
    key_helper.set_callback(keycode_callback)
    loop.run_until_complete(
        asyncio.gather(
            main()
        )
    )


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
