# Raspberry Pi Miscellany

Files from my initial forays into programming for the [Raspberry Pi](http://raspberrypi.org).


## c

Use make to build the programs in here.

### pwm

Uses the PWM pin, physical pin 12 - GPIO18. The clock divisor, range, and duty
cycle value can all be set from a menu. Has been tried with an LED and a speaker,
presumably with relevant values it would drive a servo, although that would 
require some amplification.


## python

General python programs.

### test_sleep

Test the resolution of time.sleep(). It appears to be about 100us (microseconds),
which is an order of magnitude (or more) better than I expoected.

## python/gpio

A few programs to flash LEDs etc.

### flash12

Flashes an LED attached to Pin 12 (GPIO18).

### flash_12_26

Flashes two LEDs alternately, attached to pins 12 and 26 (GPIO18 & GPIO7).

### drive_speaker

Makes a 1kHz (ish) tone from a speaker attached to pin 12 (GPIO18).

### drive_lcd

A driver library for LCD displays attached to GPIO pins in a 4-bit configuration
(see comments in the file for connection details).

When run directly, it starts by initializing the panel and writing 'SETUP'.
Then it waits for the user to hit enter between each of the next phases:
position the cursor to the beginning of the second line and write 
'Second Line', then write 'End' at the end of the second line, after which
the cursor is shown, hidden, and set blinking before finally waiting for
the user to hit enter again and then disconnecting from GPIO.

### lcd_clock

Displays a clock on the first line of a connected LCD display using the drive_lcd
library. See drive_lcd for the connection details. It ensures that it always
releases the GPIO pins by having a try...except round the main loop to trap Ctrl-C

### drive_7_segment

Drive a seven segment, common-anode, display. Connections can be seen inside
the file. Currently set up for B+, assuming a 40-pin GPIO. Shows 0-9 with a 
delay between each, and then shows each letter and waits for the user to press 
enter.

The simplest way to change to a common-cathode display would be to swap the names
of segment_on() and segment_off().

### traffic_lights

Simulate a (British) set of traffic lights with a Red, Amber, and Green LED 
connected to pins 11, 13, and 15 respectively.


## python/pygame

Adventures in game programming.

### bounce1

Bounce a (square!) ball around in a window.

### bounce2

Bounce a ball around in a box with a bouncy sound on each bounce. Use the cursor
keys to expand and contract the square that the ball is bouncing in.


## scratch

The beginnings of an alien game. N.B. I can't draw :-)

