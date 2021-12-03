# Created by Sphero Inc.
# Modified by Aaron Goff
# Additinoal code from ~/sphero/getting_started/asyncio/driving

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import asyncio

from helper_keyboard_input import KeyboardHelper
from sphero_sdk import SerialAsyncDal
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal
from sphero_sdk import DriveFlagsBitmask

# initialize global variables
key_helper = KeyboardHelper()
current_key_code = -1
driving_keys = [119, 97, 115, 100, 32]
speed = 0
speedSet = 0
heading = 0
headingAngle = 0
flags = 0

# Reference asyncio loop & SpheroRvrAsync
loop = asyncio.get_event_loop()
rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)

# Allow RVR to drive autonomously with code from ~/sphero/getting_started/asyncio/driving/drive_with_heading
async def autonomousDrive():
    await rvr.wake()

    # Give RVR time to wake up
    await asyncio.sleep(2)

    await rvr.reset_yaw()

    await rvr.drive_with_heading(
        speed=128,  # Valid speed values are 0-255
        heading=0,  # Valid heading values are 0-359
        flags=DriveFlagsBitmask.none.value
    )

    # Delay to allow RVR to drive
    await asyncio.sleep(1)

    await rvr.drive_with_heading(
        speed=128,  # Valid speed values are 0-255
        heading=0,  # Valid heading values are 0-359
        flags=DriveFlagsBitmask.drive_reverse.value
    )

    # Delay to allow RVR to drive
    await asyncio.sleep(1)

    await rvr.drive_with_heading(
        speed=128,  # Valid speed values are 0-255
        heading=90,  # Valid heading values are 0-359
        flags=DriveFlagsBitmask.none.value
    )

    # Delay to allow RVR to drive
    await asyncio.sleep(1)

    await rvr.drive_with_heading(
        speed=128,  # Valid speed values are 0-255
        heading=270,  # Valid heading values are 0-359
        flags=DriveFlagsBitmask.none.value
    )

    # Delay to allow RVR to drive
    await asyncio.sleep(1)

    await rvr.drive_with_heading(
        speed=0,  # Valid heading values are 0-359
        heading=0,  # Valid heading values are 0-359
        flags=DriveFlagsBitmask.none.value
    )

    # Delay to allow RVR to drive
    await asyncio.sleep(1)

# Update keycode and print
def keycode_callback(keycode):
    global current_key_code
    current_key_code = keycode
    print("Key code updated: ", str(current_key_code))

# Allow RVR to set forward & reverse speed
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
        
# Allow RVR to set left & right pitch angle       
def headingAng():
    global headingAngle
    if current_key_code == 114: # R - Angle Up
        headingAngle += 15
    elif current_key_code == 102: # F - Angle Down
        headingAngle -= 15
        
    # check the heading value, and wrap as necessary.
    if headingAngle > 90:
        headingAngle = 90
    elif headingAngle < 0:
        headingAngle = 0
    print('Current angle: ' + str(headingAngle))
        
# Start main and create loop
async def main():
    global current_key_code
    global speed
    global heading
    global flags

    await rvr.wake()

    await rvr.reset_yaw()
            
    # Create infinite loop to constantly watch for keyboard inputs      
    while True:

        if current_key_code == 121 or current_key_code == 104: # Y - Speed Up OR H - Speed Down
            speedChange()
        elif current_key_code == 114 or current_key_code == 102: # R - Angle Up OR F - Angle Down
            headingAng()
        elif current_key_code == 119:  # W - Forward
            flags = 0
            speed = speedSet
        elif current_key_code == 115:  # S - Reverse
            flags = 1
            speed = speedSet
        elif current_key_code == 97:  # A - Left
            heading -= (headingAngle)
        elif current_key_code == 100:  # D - Right
            heading += headingAngle
        elif current_key_code == 120:  # X - Autonomous
            await autonomousDrive()

        
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
