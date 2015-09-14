# Raspberry Pi Miscellany

Files from my initial forays into programming for the [Raspberry Pi](http://raspberrypi.org).

## GPIO

A few programs to flash LEDs etc.

### flash12

Flash an LED attached to Pin 12 (GPIO18).

### flash_12_26

Flash two LEDs alternately, attached to pins 12 and 26 (GPIO18 & GPIO7).

### drive_speaker

Make a 1kHz (ish) tone from a speaker attached to pin 12 (GPIO18). I'm not sure 
of the actual resolution of time.sleep() so I don't know if asking for a 1ms 
delay is sensible.

### drive_lcd

Drive a 16x2 LCD display in a 4-bit configuration, attached to GPIO pins (See
inside for the data pins).  The program starts by initializing the panel and 
writing 'EFG'. Then it waits for the user to hit enter between each of the 
next phases: clear the display and write 'Clear', home the cursor and write 
'Home...', position the cursor to the beginning of the second line and write 
'Second Line', then finally write 'End' at the end of the second line, before 
finally waiting for the user to hit enter again and then disconnecting from
GPIO.

## PYGAME

### bounce1

Bounce a (square!) ball around in a window.

### bounce2

Bounce a ball around in a box with a bouncy sound on each bounce.

