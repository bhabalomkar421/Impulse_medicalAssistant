import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)


def LightUnit(r, y, g):
    GPIO.setup(r, GPIO.OUT)
    GPIO.setup(y, GPIO.OUT)
    GPIO.setup(g, GPIO.OUT)

    GPIO.output(r, True)
    time.sleep(2)
    GPIO.output(r, False)
    time.sleep(1)

    GPIO.output(y, True)
    time.sleep(2)
    GPIO.output(y, False)
    time.sleep(1)

    GPIO.output(g, True)
    time.sleep(2)
    GPIO.output(g, False)
    time.sleep(1)


if __name__ == '__main__':
    LightUnit(29, 31, 33)
    GPIO.cleanup()

    LightUnit(11, 13, 15)
    GPIO.cleanup()

    LightUnit(36, 38, 40)
    GPIO.cleanup()

    LightUnit(29, 31, 32)
    GPIO.cleanup()
