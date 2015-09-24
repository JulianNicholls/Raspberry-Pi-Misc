# Raspberry Pi Miscellany

Files from my initial forays into programming for the [Raspberry Pi](http://raspberrypi.org).

## GPIO

A few programs to flash LEDs etc.

### flash12

Flashes an LED attached to Pin 12 (GPIO18).

### flash_12_26

Flashes two LEDs alternately, attached to pins 12 and 26 (GPIO18 & GPIO7).

### drive_speaker

Makes a 1kHz (ish) tone from a speaker attached to pin 12 (GPIO18). I'm not sure 
of the actual resolution of time.sleep() so I don't know if asking for a 1ms 
delay is sensible.

### drive_lcd

A driver library for LCD displays attached to GPIO pins in a 4-bit configuration
(see comments for connection details).
When run directly, it starts by initializing the panel and 
writing 'SETUP'. Then it waits for the user to hit enter between each of the 
next phases: position the cursor to the beginning of the second line and write 
'Second Line', then write 'End' at the end of the second line, then the cursor is 
shown, hidden, and set blinking before finally waiting for the user to hit enter 
again and then disconnecting from GPIO.

### lcd_clock

Displays a clock on the first line of a connected LCD display using the drive_lcd
library. See drive_lcd for the connection details. It ensures that it always
releases the GPIO pins by having a try...except round the main loop to trap Ctrl-C

## PYGAME

### bounce1

Bounce a (square!) ball around in a window.

### bounce2

Bounce a ball around in a box with a bouncy sound on each bounce.

