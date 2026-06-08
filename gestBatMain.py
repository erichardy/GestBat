from machine import Pin, Timer, RTC, ADC
import time
from utime import sleep
from gestBatLED import *
from gestBatBeep import *
from gestBatRotary import *

mainRelay1 = Pin(18, Pin.OUT)
mainRelay2 = Pin(17, Pin.OUT)
chargerRelay = Pin(16, Pin.OUT)
currentProbe = ADC(26)
resetButton = Pin(27, Pin.OUT)

rtc = RTC()

def mainRelais(OnOff):
    # OnOff = 1 or ON : relais ON
    # OnOFF = 0 or OFF : relais OFF
    mainRelay1.value(OnOff)
    mainRelay2.value(OnOff)

"""
Delais and timers
"""
def secToAll(secondes: int) -> tuple[int, int, int]:
    h = secondes // 3600
    m = (secondes % 3600) // 60
    s = secondes % 60
    return int(h), int(m), int(s)

def decrementDelay(t):
    global remainingTime
    print("in decrementDelay : " + str(remainingTime))
    remainingTime -= 5000

# newDelayTime : miliseconds
def startDelay(newDelayTime):
    global remainingTime
    globalDelay = remainingTime
    # replace beepTest by the actual start procedure...
    # the charge will start when realDelayTime expires
    timerStartCharge = Timer(mode=Timer.ONE_SHOT, period=globalDelay, callback=beepTest2)
    sleep(.1)
    # freq = 0.2 Hz == 5 secondes
    timerDecrementDelay = Timer(mode=Timer.PERIODIC, freq=.2, callback=decrementDelay)
    sleep(.1)
    timerStopDecrementDelay = Timer(mode=Timer.ONE_SHOT,\
                               period=globalDelay,\
                               # period=3000,\
                               callback=lambda t:timerDecrementDelay.deinit())

def setDelayBeforeCharge():
    txt = "Delay : {t} => Use rotary to modify then clic..."
    print(txt.format(t = defaultDelayTime))
    display("Reglage delai :", 0, 0, clear=True)
    newDelayTime = setDelayTime() # from getsBatRotary
    print("MAIN : actualDelayTime = " + str(newDelayTime))
    utime.sleep(.2)
    return newDelayTime # minutes

def waitDelayExpire(newDelayTime):
    myTime = time.localtime()
    print(myTime)
    # tuple to list
    l_myTime = list(myTime)
    l_myTime[4] += newDelayTime
    # list to tuple
    t_myTime = tuple(l_myTime)
    delayExpire = time.mktime(t_myTime)
    date_delayExpire = time.localtime(delayExpire)

    sec_newDelayTime = newDelayTime * 60
    (h, m, s) = secToAll(sec_newDelayTime)

    LED_Y_BlinkStart(2)
    display('Debut dans :', 0, 0, clear=True)
    beforeLoop = time.ticks_ms()
    while myTime < date_delayExpire:
        sleep(.8)
        sec_newDelayTime -= 1
        h, m, s = secToAll(sec_newDelayTime)
        delay = f"=> {h:02d}:{m:02d}:{s:02d}"
        display(delay, 0, 1, clear1=True)
        myTime = time.localtime()
        
    endLoop = time.ticks_ms()
    loopTime = f"Loop Time = {endLoop} - {beforeLoop} = {endLoop-beforeLoop}"
    print(loopTime)
    LED_Y_BlinkStop()
    print(myTime)

"""
END Delais and timers
"""
def averageValues(l, newValue):
    l.pop(0)
    l.append(newValue)
    return sum(l) / len(l)

def startUP():
    # all procedures at startup...
    print("On Startup !")
    mainRelais(ON)
    LEDsAction(LEDsALL, OFF, 0)
    LEDsAction(LEDsALL, ON, .1)
    LEDsAction(LEDsALL, OFF, 0)
    GreenLed.value(ON)
    greeting()
    beep(5, 440, 65535, duration=.1, repeat=2, speed=.05)

def shutdown():
    # all procedures at shutdown
    beep(5, 440, 65535, duration=.2, repeat=5, speed=.05)
    LED_R_BlinkStop()
    LEDsAction(LEDsALL, OFF, 0)
    LEDsExamples()
    mainRelais(OFF)

def resetAction(p):
    display('Reset !!!', 0, 0, clear=True)
    beep(5, 440, 65535, duration=.2, repeat=3, speed=.05)
    sleep(.3)
    mainRelais(0)
    
# Configure reset function : hard shutdown
resetButton.value(1)
resetButton.irq(resetAction)
# resetButton.irq(lambda p:print('IIIIRRRQ'))
#

print('..............')
print(time.localtime())
print('..............')
startUP()
newDelayTime = setDelayBeforeCharge() # minutes
# print(newDelayTime)
waitDelayExpire(newDelayTime)

currentValues = [65535, 65535, 65535, 65535, 65535,\
                 65535, 65535, 65535, 65535, 65535]

LED_R_BlinkStart(2)
LED_Y_BlinkStop()
YellowLed.value(1)
beep(5, 440, 65535, duration=.1, repeat=2, speed=.05)

chargerRelay.value(1)
currentReading = currentProbe.read_u16()
nbLoops = 0
average = averageValues(currentValues, currentReading)
while average > 600:
    display(str(currentReading), 0, 0, clear=False, clear0=True)
    sleep(.2) # 5 mesures par secondes
    currentReading = currentProbe.read_u16()
    average = averageValues(currentValues, currentReading)
    nbLoops += 1
    if not nbLoops % 10: # un affichage de la moyenne toutes les 10 mesures
        display(str(nbLoops) + \
                " " + \
                str(average), 0, 1, clear=True)

print('..............')
print(time.localtime())
print('..............')
shutdown()


### => debut de la charge
# allumage du relai du chargeur
# clignotement des LED rouges
# boucle 
#    capture des données de courant
#    ajustement du clignotement des LED rouges en fonction du courant tiré
#    si courant < valeur min:
#         sortie de la boucle
# opération de shutdown : beep, LED, coupure des relais principaux => arrêt total

print('END')
beep(5, 440, 65535, duration=.1, repeat=2, speed=.1)


