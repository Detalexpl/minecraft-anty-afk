from pynput.mouse import Button, Controller
import time

mouse = controller()

while True:
    time.sleep(0.01)
    mouse.move (5,-5)
    time.sleep(0.01)
    mouse.move(-5,5)
    time.sleep(0.01)