class motor:

    def __init__(self):
        # Setting up pin numbers and pwm properties
        
        self.pinSelection = {'directionPin': 0, 'speedPin': 0, 'encoderPinA': 0, 'encoderPinB': 0}
        self.pwmSelection = {'pwmFrequency': 0, 'motorSpeed': 0, 'motorDirection': 0}
        self.encoderProperties = {'encoderCounts': 0, 'encoderSpeed': 0}
        self.encoderStatus = {'encoderA': {'present': 0, 'past': 0}, 'encoderB': {'present': 0, 'past': 0}, 'missCounts': 0}
        
        
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

    def updateEncoderA(self, channel):

        self.encoderStatus['encoderA']['present'] = GPIO.input(self.pinSelection['encoderA'])
        self.encoderStatus['encoderB']['present'] = GPIO.input(self.pinSelection['encoderB'])

        if ((self.encoderStatus['encoderA']['present'], self.encoderStatus['encoderB']['past']) == (1,0)) or ((self.encoderStatus['encoderA']['present'], self.encoderStatus['encoderB']['past']) == (0,1)):
            self.encoderProperties['encoderCounts']+=1
          
        elif ((self.encoderStatus['encoderA']['present'], self.encoderStatus['encoderB']['past']) == (1,1)) or ((self.encoderStatus['encoderA']['present'], self.encoderStatus['encoderB']['past']) == (0,0)):
            self.encoderProperties['encoderCounts']-=1

        else:
            self.encoderStatus['missCounts']+=1

        
        self.encoderStatus['encoderA']['past'], self.encoderStatus['encoderB']['past'] = self.encoderStatus['encoderA']['present'], self.encoderStatus['encoderB']['present']
        

    def updateEncoderB(self, channel):

        self.encoderStatus['encoderA']['present'] = GPIO.input(self.pinSelection['encoderA'])
        self.encoderStatus['encoderB']['present'] = GPIO.input(self.pinSelection['encoderB'])

        if ((self.encoderStatus['encoderB']['present'], self.encoderStatus['encoderA']['past']) == (1,1)) or ((self.encoderStatus['encoderB']['present'], self.encoderStatus['encoderA']['past']) == (0,0)):
            self.encoderProperties['encoderCounts']+=1

        elif ((self.encoderStatus['encoderB']['present'], self.encoderStatus['encoderA']['past']) == (1,0)) or ((self.encoderStatus['encoderB']['present'], self.encoderStatus['encoderA']['past']) == (0,1)):
            self.encoderProperties['encoderCounts']-=1

        else:
            self.encoderStatus['missCounts']+=1


        self.encoderStatus['encoderA']['past'],self.encoderStatus['encoderB']['past'] = self.encoderStatus['encoderA']['present'], self.encoderStatus['encoderB']['present']



        

    def retrieveEncoderInfo(self):
        


        
        
        






