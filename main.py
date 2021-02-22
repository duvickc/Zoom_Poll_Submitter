# This is an attempt at automating answering a zoom poll and submitting it.
# This is used for getting the points for zoom attendance.
# requires pyautogui

import os
from time import sleep
import pyautogui as py


def get_image_position(option_image):
    return py.locateCenterOnScreen(option_image)


def get_image_path(name):
    script_dir = os.path.dirname(__file__)
    image_path = os.path.join(
        script_dir,
        'images',
        name
    )
    return image_path


def countdown_timer(time_to_wait=10):
    print("Countdown:")
    for i in range(time_to_wait, 0, -1):
        print(i, end=" ", flush=True)
        sleep(1)
    print("Start")


def main():
    py.FAILSAFE = True
    countdown_timer(5)

    option_image = get_image_path('option.PNG')
    position = get_image_position(option_image)
    while position is None:
        print('no position')
        sleep(3)
        position = get_image_position(option_image)
    py.click(position.x, position.y)

    submit_image = get_image_path('submit.PNG')
    position = get_image_position(submit_image)
    py.click(position.x, position.y)
    print('submitted')


main()
