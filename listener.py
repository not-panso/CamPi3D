from subprocess import run
import RPi.GPIO as gpio
from time import sleep

pin = 16
gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.IN, pull_up_down=gpio.PUD_UP)

old_state = gpio.input(pin)

while True:
    sleep(0.1)
    state = gpio.input(pin)
    if old_state == 1 and state == 0:
        run(['python', 'campi.py'])
        sleep(1)
    old_state = state

gpio.cleanup()