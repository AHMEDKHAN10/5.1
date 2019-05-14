import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.OUT)
import time
try:
    while 1:
        GPIO.output(29, GPIO.HIGH)
        time.sleep(0.25)
        GPIO.output(29, GPIO.LOW)
        time.sleep(0.25)
except KeyboardInterrupt:       
    GPIO.cleanup()