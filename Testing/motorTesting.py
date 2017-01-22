import RPi.GPIO as GPIO
from time import sleep

""" Setting up hardware """
GPIO.setmode(GPIO.BCM)
pwmPin = 13
dirPin = 26
encoderA_pin = 21 
encoderB_pin = 20
GPIO.setup(dirPin, GPIO.OUT)
GPIO.setup(pwmPin, GPIO.OUT)
GPIO.setup(encoderA_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(encoderB_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
motor = GPIO.PWM(pwmPin, 500)
pauseTime = 2


""" Function definition """
def update_encoderA(channel):
	global counts
	global error
	global encoderA
	global encoderB
	global encoderA_old
	global encoderB_old

	encoderA,encoderB = GPIO.input(encoderA_pin),GPIO.input(encoderB_pin)

	if ((encoderA,encoderB_old) == (1,0)) or ((encoderA,encoderB_old) == (0,1)):
		counts+=1
	elif ((encoderA,encoderB_old) == (1,1)) or ((encoderA,encoderB_old) == (0,0)):
		counts-=1
	else:
		error+=1
	encoderA_old,encoderB_old = encoderA,encoderB

def update_encoderB(channel):
	global counts
	global error
	global encoderA
	global encoderB
	global encoderA_old
	global encoderB_old

	encoderA,encoderB = GPIO.input(encoderA_pin),GPIO.input(encoderB_pin)

	if ((encoderB,encoderA_old) == (1,1)) or ((encoderB,encoderA_old) == (0,0)):
		counts+=1
	elif ((encoderB,encoderA_old) == (1,0)) or ((encoderB,encoderA_old) == (0,1)):
		counts-=1
	else:
		error+=1
	encoderA_old,encoderB_old = encoderA,encoderB


""" Declaring global variables """
encoderA = 0
encoderB = 0
encoderA_old = 0
encoderB_old = 0
counts = 0
error = 0
runTime = 10

""" Running motor """
GPIO.add_event_detect(encoderA_pin, GPIO.BOTH, callback = update_encoderA)
GPIO.add_event_detect(encoderB_pin, GPIO.BOTH, callback = update_encoderB)
motor.start(100)
GPIO.output(dirPin, GPIO.LOW)
counter = 0
#sleep(pauseTime)

while counter<runTime:
	sleep(pauseTime)
	print "Encoder counts = " + str(counts)
	print "Error in counts = " + str(error)
	counter+=1
print "Encoder counts = " + str(counts)
	
GPIO.output(dirPin, GPIO.HIGH)
counter = -1
while counter<runTime:
	sleep(pauseTime)
	print "Encoder counts = " + str(counts)
	print "Error in counts = " + str(error)
	counter+=1


motor.stop()
GPIO.cleanup()



