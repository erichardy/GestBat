from machine import Pin, Timer
import utime

GreenLed = Pin(10, Pin.OUT)
TimG = Timer()
YellowLed = Pin(11, Pin.OUT)
TimY = Timer()
Red1Led = Pin(12, Pin.OUT)
TimR1 = Timer()
Red2Led = Pin(13, Pin.OUT)
TimR2 = Timer()

GreenLed = Pin(10, Pin.OUT)
YellowLed = Pin(11, Pin.OUT)
Red1Led = Pin(12, Pin.OUT)
Red2Led = Pin(13, Pin.OUT)
LEDs = {}
LEDs['G'] = GreenLed
LEDs['Y'] = YellowLed
LEDs['R1'] = Red1Led
LEDs['R2'] = Red2Led
LEDsALL = ['G', 'Y', 'R1', 'R2']
LEDsALL_Reverse = LEDsALL.copy()
LEDsALL_Reverse.reverse()

ON = 1
OFF = 0

def LEDsAction(Led_List, value, delay=0):
    global LEDs
    for l in Led_List:
        LEDs[l].value(value)
        if delay:
            utime.sleep(delay)

def LED_Y_Blink(timer):
    global YellowLed
    YellowLed.toggle()

def LED_Y_BlinkStart(freq):
    TimY.init(freq=freq, mode=Timer.PERIODIC, callback=LED_Y_Blink)

def LED_Y_BlinkStop():
    TimY.deinit()

def LED_R1_Blink(timer):
    global Red1Led
    Red1Led.toggle()

def LED_R2_Blink(timer):
    global Red2Led
    Red2Led.toggle()

def LED_R_BlinkStart(freq):
    global Red1Led
    global Red2Led
    Red1Led.value(1)
    Red2Led.value(0)
    TimR1.deinit()
    TimR2.deinit()
    TimR1.init(freq=freq, mode=Timer.PERIODIC, callback=LED_R1_Blink)
    TimR2.init(freq=freq, mode=Timer.PERIODIC, callback=LED_R2_Blink)

def LED_R_BlinkStop():
    TimR1.deinit()
    TimR2.deinit()
    Red1Led.value(0)
    Red2Led.value(0)

def LEDsExamples():
    
    LED_Y_BlinkStart(3)
    for x in [10, 5, 1]:
        LED_R_BlinkStart(x)
        utime.sleep(5)
        LED_R_BlinkStop()
        # LED_Y_BlinkStop()
        LEDsAction(['R1', 'R2'], OFF, 0)
    LED_Y_BlinkStop()
    utime.sleep(1)
    LEDsAction(LEDsALL, OFF, 0)
    """
    LEDsAction('Y', ON, 0)
    utime.sleep(1)
    LEDsAction('Y', OFF, 0)
    utime.sleep(1)
    LEDsAction(['R1'], ON, 0)
    utime.sleep(1)
    LEDsAction(['R1'], OFF, 0)
    """
    #
    delay = .06
    for t in range(5):
        LEDsAction(LEDsALL, ON, delay)
        LEDsAction(LEDsALL, OFF, delay)
        LEDsAction(LEDsALL_Reverse, ON, delay)
        LEDsAction(LEDsALL_Reverse, OFF, delay)
        # LEDsAction(LEDsALL, ON, delay)
        # LEDsAction(LEDsALL_Reverse, OFF, delay)
    LEDsAction(LEDsALL, OFF, 0)

