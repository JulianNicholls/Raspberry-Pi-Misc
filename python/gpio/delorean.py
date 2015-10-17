# Continuously show the time until interrupted, and then release the GPIO pins.

import drive_lcd as lcd
from datetime import datetime

lcd.setup()
lcd.clear()
lcd.set_cursor(lcd.OFF)

lcd.home()
lcd.say('OCT 26 1985 0900')
try:            # To catch Ctrl-C
    while(1):
        now = datetime.now()

        time_str = now.strftime("%b %d %Y %H%M").upper()

        lcd.set_position(1, 0)
        lcd.say(time_str)

        # Wait until the next second.

        second = now.second

        while(now.second == second):    
            now = datetime.now()
except:
    print("Releasing Pins")
    lcd.release_pins()

