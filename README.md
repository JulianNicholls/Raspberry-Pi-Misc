# Raspberry Pi Miscellany

Files from my forays into programming for the [Raspberry Pi](http://raspberrypi.org).

Includes programs written in C, Python, Javascript, and a little Scratch.

Libraries used: RPi.GPIO, gpiozero, wiringPi, pygame. and soon Pygame Zero.


## c

Use make to build the programs in here.

### pwm

Uses the PWM pin, physical pin 12 (GPIO18). The clock divisor, range, and duty
cycle value can all be set from a menu. It has been tried with an LED, a
speaker, and a 6V motor connected to the collector side of a PN2222 transistor.

Presumably, with relevant values, it would drive a servo, requiring a transistor
for switching a higher voltage and current again.


## python

General python programs.

### test_sleep

Test the resolution of time.sleep(). It appears to be about 100us (microseconds),
which is an order of magnitude (or more) better than I expected.


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
releases the GPIO pins by having a try...except round the main loop to trap Ctrl-C.

### delorean

Show the top line from the Delorean display, and the second line is the current
time.

### drive_7_segment

Drive a seven segment, common-anode, display. Connections can be seen inside
the file. Currently set up for B+, assuming a 40-pin GPIO.

First it shows 0-F with a delay between each. Then, it shows 6 arrows pointing
forward and back, right and left. Finally, it shows each possible letter and waits
for the user to press enter.

The simplest way to change to a common-cathode display would be to swap the names
of segment_on() and segment_off().

### traffic_lights

Simulate a (British) set of traffic lights with a Red, Amber, and Green LED
connected to pins 11, 13, and 15 respectively.

### motor

Turn a motor on and off connected to pin 12 via PN2222A transistor.

I wrote this so that I could turn the motor off quickly in case I'd made a bad
choice of transistor or another schoolboy error. The motor is connected to the
collector and powered by a wall-wart providing a range of voltages, I tried 6V
and 9V, but I initially tried it with the 5V line (pin 2) on the Pi GPIO and
that was fine too.

it turns out that my choice of transistor was OK. With pin 12 connected via a
400 Ohm resistor to the Base of the transistor, I'm drawing less than 9mA from
the Pi. The motor is drawing around 180mA when running freely. I'm going to try
stalling the motor a little to test its maximum draw once I have some crocodile
clips.


## python/gpiozero

Examples using the GPIO Zero library.

### button_led

Using gpiozero library, switch a LED connected to GPIO17 on and off with a button
connected to GPIO21 and a GND.


## python/pygame

Adventures in game / UI programming.

### bounce1

Bounce a (square!) ball around in a window.

### bounce2

Bounce a ball around in a box with a bouncy sound on each bounce. Use the cursor
keys to expand and contract the square that the ball is bouncing in.


## python/pygame/led_ui

Display buttons that turn LEDs on and off. Five buttons turn directly connected
LEDs on and off. Another seven buttons turn the segments of a display on and off.
Ten more buttons display the digits 0-9 on the 7-segment display and a final 25
buttons allow for most of the alphabet in upper or lower case.

See main.py and .../gpio/drive_7_segment for full connection details.


## python/wiimote

Examples using the python-cwiid library

### wiimote

An example of using a Wiimote on a Pi, displays the state of the buttons and
the accelerometer data. It's a bit flaky with the £3.99 Wiimote clone that I
bought from eBay, and I'm hoping to try it with a genuine Nintendo one.


## node

A Blynk library client program that updates Virtual Pin 9 with time seconds,
responds to a slider on V1, updating a graph attached to V4, and has a
terminal on V3 which feeds back and sends notifications.


## scratch

The beginnings of an alien game. N.B. I can't draw :-)

