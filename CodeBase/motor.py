class motor:
    def __init__(self):
        # Setting up pin numbers and pwm properties
        
        self.pinSelection = {'directionPin': -1, 'speedPin': -1, 'encoderPinA': -1, 'encoderPinB': -1}
        self.pwmSelection = {'pwmFrequency': -1, 'motorSpeed': -1, 'motorDirection': -1}

        
    def pinInitialization(self, directionPin, speedPin, encoderPinA, encoderPinB):
        # Initializing Rpi for the motor pins

        self.pinSelection = {'directionPin': directionPin, 'speedPin': speedPin, 'encoderPinA': encoderPinA, 'encoderPinB': encoderPinB}
        GPIO.setup(self.pinSelection['directionPin'], GPIO.OUT)
        GPIO.setup(self.pinSelection['speedPin'], GPIO.OUT)
        GPIO.setup(self.pinSelection['encoderPinA'], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(self.pinSelection['encoderPinB'], GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    def pwmInitialization(self, pwmFrequency, motorSpeed, motorDirection):
        # Starting the motor with the desired speed and direction

        self.pwmSelection = {'pwmFrequency': pwmFrequency, 'motorSpeed': motorSpeed, 'motorDirection': motorDirection}
        motor = GPIO.PWM(self.pinSelection['speedPin'], self.pwmSelection['pwmFrequency'])

        if self.pwmSelection['motorDirection'] == 'forward':
            GPIO.output(self.pinSelection['directionPin'], GPIO.HIGH)
        else:
            GPIO.output(self.pinSelection['directionPin'], GPIO.LOW)

        motor.start(self.pwmSelection['motorSpeed'])

    


        
        
        






