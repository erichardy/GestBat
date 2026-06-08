from machine import Timer, freq, RTC
from utime import sleep
from gestBatRotary import *
from gestBatBeep import *
from gestBatLCD import *

global remainingTime

def beepTest3(t3):
    beep(5, 440, 65535, duration=.1, repeat=3, speed=.05)

def beepTest2(t2):
    beep(5, 440, 65535, duration=.1, repeat=2, speed=.5)

# realDelayTime = 0

# uint64_t delta_us; // for periodic mode
# => valeur max = 18 446 744 073 709 551 615 (NO LIMIT !... mais à confirmer...)

def secToAll(secondes: int) -> tuple[int, int, int]:
    h = secondes // 3600
    m = (secondes % 3600) // 60
    s = secondes % 60
    return int(h), int(m), int(s)
"""
def decrementDelay(t):
    # global currentDelay
    global remainingTime
    # h, m, s = secToAll(realDelayTime / 1000)
    # delay = f"=> {h:02d}:{m:02d}:{s:02d}"
    # display(delay, 0, 0, clear=True)
    # lcd.clear()
    # lcd.putstr(delay)
    
    # print(f"{realDelayTime / 1000} secondes = {h} h {m} min {s} s")
    remainingTime -= 5000

# newDelayTime : miliseconds
def startDelay(newDelayTime):
    global remainingTime
    globalDelay = remainingTime
    # replace beepTest by the actual start procedure...
    # the charge will start when realDelayTime expires
    timerStartCharge = Timer(mode=Timer.ONE_SHOT, period=globalDelay, callback=beepTest2)
    sleep(.5)
    print(timerStartCharge)
    timerDecrementDelay = Timer(mode=Timer.PERIODIC, freq=5, callback=decrementDelay)
    # sleep(.5)
    # print(timerDisplayDelay)
    """ """
    timerStopDecrementDelay = Timer(mode=Timer.ONE_SHOT,\
                               period=globalDelay,\
                               # period=3000,\
                               callback=lambda t:timerDecrementDelay.deinit())
                            
"""
