from pynput.keyboard import Key, Controller

from time import sleep

keyboard = Controller()


def volumeUp():
    for i in range(2):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)


def volumeDown():
    for i in range(2):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)
