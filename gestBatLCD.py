import utime
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd


I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

# i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)

# i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
i2c = I2C(0, sda=Pin(0), scl=Pin(1))

lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

# Bitmap 5x8 pour 'é' (accent aigu + forme de 'e')
e_acute = bytearray([
    0b00100,  # ´
    0b00000,
    0b01110,  # e
    0b10001,
    0b11111,
    0b10000,
    0b01110,
    0b00000,
])

# Selon la lib : create_char(...) ou custom_char(...)
try:
    lcd.create_char(0, e_acute)    # slot 0
except AttributeError:
    lcd.custom_char(0, e_acute)

def greeting():
    lcd.clear()
    lcd.move_to(5,0)
    lcd.putstr("Welcome")
    lcd.move_to(3,1)
    lcd.putstr("To gestBat")

def display(s, x, y, clear=False, clear0=False, clear1=False):
    # display the string s at positions x,y
    # clear or not the screen
    # clear0 : clear the first line, clear1 : clear the second line
    if clear:
        lcd.clear()
    if clear0:
        for i in range(0,16):
            lcd.move_to(i, 0)
            lcd.putchar(' ')
        lcd.move_to(0, 0)
    if clear1:
        for i in range(0,16):
            lcd.move_to(i, 1)
            lcd.putchar(' ')
        lcd.move_to(0, 0)
    lcd.move_to(x, y)
    lcd.putstr(s)


"""
greeting()    
utime.sleep(2)
lcd.clear()
"""
