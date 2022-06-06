import RPi.GPIO as GPIO
import time

class RGB:
    def __init__(self, red, green, blue):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.red = red
        self.green = green
        self.blue = blue

        GPIO.setup(self.red, GPIO.OUT)
        GPIO.setup(self.green, GPIO.OUT)
        GPIO.setup(self.blue, GPIO.OUT)


    def Red(self):
        GPIO.output(self.red, GPIO.HIGH)
        GPIO.output(self.green, GPIO.LOW)
        GPIO.output(self.blue, GPIO.LOW)

    def RedFlash(self):
        GPIO.output(self.red, GPIO.HIGH)
        GPIO.output(self.green, GPIO.LOW)
        GPIO.output(self.blue, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(self.red, GPIO.LOW)
        time.sleep(0.5)

    def Green(self):
        GPIO.output(self.green, GPIO.HIGH)
        GPIO.output(self.red, GPIO.LOW)
        GPIO.output(self.blue, GPIO.LOW)

    def GreenFlash(self):
        GPIO.output(self.green, GPIO.HIGH)
        GPIO.output(self.red, GPIO.LOW)
        GPIO.output(self.blue, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(self.green, GPIO.LOW)
        time.sleep(0.5)

    def Blue(self):
        GPIO.output(self.red, GPIO.LOW)
        GPIO.output(self.green, GPIO.LOW)
        GPIO.output(self.blue, GPIO.HIGH)

    def White(self):
        GPIO.output(self.red, GPIO.HIGH)
        GPIO.output(self.green, GPIO.HIGH)
        GPIO.output(self.blue, GPIO.HIGH)

    def WhiteFlash(self):
        GPIO.output(self.red, GPIO.HIGH)
        GPIO.output(self.green, GPIO.HIGH)
        GPIO.output(self.blue, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(self.red, GPIO.LOW)
        GPIO.output(self.green, GPIO.LOW)
        GPIO.output(self.blue, GPIO.LOW)
        time.sleep(0.5)

    def Orange(self):
        GPIO.output(self.red, GPIO.HIGH)
        GPIO.output(self.green, GPIO.HIGH)
        GPIO.output(self.blue, GPIO.LOW)

    def OrangeFlash(self):
        GPIO.output(self.red, GPIO.HIGH)
        GPIO.output(self.green, GPIO.HIGH)
        GPIO.output(self.blue, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(self.red, GPIO.LOW)
        GPIO.output(self.green, GPIO.LOW)
        GPIO.output(self.blue, GPIO.LOW)
        time.sleep(0.5)

    def Stop(self):
        GPIO.cleanup()