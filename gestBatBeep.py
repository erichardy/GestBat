from machine import PWM, Pin
from utime import sleep

# duration : second(s)
# repeat : nb time to make a beep
# speed : small is fast, large is slow
def beep(beepPin, freq, duty_u16, duration=.3, repeat=1, speed=.2):
    
    for t in range(0, repeat):
        beepPWM = PWM(Pin(beepPin), freq=freq, duty_u16=duty_u16)
        sleep(duration)
        beepPWM.duty_u16(0)
        beepPWM.deinit()
        beepPWM = Pin(beepPin, Pin.OUT)
        beepPWM.value(0)
        sleep(speed)

# examples :
# beep(5, 440, 65535, duration=.1, repeat=3, speed=2)
# beep(5, 440, 65535, duration=.1, repeat=3, speed=.05)

def beepTest3(t):
    beep(5, 440, 65535, duration=.1, repeat=3, speed=.05)

def beepTest2(t):
    beep(5, 440, 65535, duration=.1, repeat=2, speed=.5)
