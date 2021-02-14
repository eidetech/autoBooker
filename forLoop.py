from pynput.keyboard import Key, Controller
import time
from time import sleep
keyboard = Controller()
for i in range(10):
    keyboard.press(Key.backspace)
    sleep(1)
