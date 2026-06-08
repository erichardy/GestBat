import time
from machine import Pin
from rotary_irq_rp2 import RotaryIRQ
from gestBatLCD import *

# Enter the two GPIO pins you connected to data pins A and B
# Note the order of the pins isn't strict, swapping the pins
# will swap the direction of change.
# rotary = RotaryIRQ(19, 20)
rotary = RotaryIRQ(20, 19)

# clic : the pin that SW is connected to on the Pico
rotaryBtn = Pin(21, Pin.IN)

defaultDelayTime = 30  # default number of minutes before start of charge
# defaultDelayTime = 1  # default number of minutes before start of charge

delayTime = defaultDelayTime
rotary.set(value=defaultDelayTime)

def setDelayTime():
    # lcd print : set delay and clic to validate
    global delayTime
    newDelayTime = delayTime
    nDT = newDelayTime
    display("Debut : " + str(nDT) + "mn", 0, 1, clear=False, clear1=True)
    while True:
        if rotaryBtn.value() == 0:  # Has the button been pressed?
            # print("We start battery charge..." + str(newDelayTime))
            time.sleep_ms(250) # A small delay to wait for the button to stop being pressed
            return newDelayTime
            
        nDT = rotary.value()  # What is the encoder value right now?
        
        if nDT != newDelayTime:  # The encoder value has changed!
            if nDT < 0 :
                nDT = 0
            if nDT > 120:
                nDT = 120
            rotary.set(value=nDT)
            print('Encoder value:', rotary.value())
            display("Debut : " + str(nDT) + "mn", 0, 1, clear1=True)
            
            newDelayTime = nDT

