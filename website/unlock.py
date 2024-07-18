from flask import Flask, render_template, redirect, url_for
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

# GPIO setup
servo_pin = 18  # GPIO pin connected to the servo signal wire
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Function to control the servo motor
def move_servo(angle):
    pwm = GPIO.PWM(servo_pin, 50)  # PWM with frequency 50 Hz
    pwm.start(7.5)  # Initial position
    duty = angle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)
    pwm.stop()
