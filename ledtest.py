import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
data=""
red=27
yellow=17
green=4
buzz=22

def led_on(color):
	GPIO.output(color,GPIO.HIGH)
def led_off(color):
	GPIO.output(color,GPIO.LOW)
def buzz_on():
	GPIO.output(buzz,GPIO.HIGH)
def buzz_off():
	GPIO.output(buzz,GPIO.LOW)




















