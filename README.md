# Raspberry Pi Miscellany

Files from my forays into programming for the [Raspberry Pi](http://raspberrypi.org).

Includes programs written in C, Python, Javascript, and a little Scratch.

Libraries used: RPi.GPIO, gpiozero, wiringPi, pygame, python-cwiid, and
soon Pygame Zero.


----
## c

Use `make` to build the programs in here.

### pwm

Uses the PWM pin, physical pin 12 (GPIO18). The clock divisor, range, and duty
cycle value can all be set from a menu. It has been tried with an LED, a
speaker, and a 6V motor connected to the collector side of a PN2222 transistor.

Presumably, with relevant values, it would drive a servo, requiring a transistor
for switching a higher voltage and current again.

The frequencies quoted in the program have now been checked with a multimeter that
has a frequency function.


----
## python

General python programs.

### test_sleep

Test the resolution of `time.sleep()`. It appears to be about 100us (microseconds),
which is an order of magnitude (or more) better than I expected. time.sleep(n)
ALWAYS sleeps for at least the time specified.


----
## python/gpio

A few programs to flash LEDs etc.

### flash18

Flashes an LED attached to Pin 12 (GPIO18).

### flash_12_26

Flashes two LEDs alternately, attached to pins 12 and 26 (GPIO18 & GPIO7).

### drive_speaker

Makes a 1kHz (ish) tone from a speaker attached to pin 12 (GPIO18).

### drive_lcd

A driver library for LCD displays attached to GPIO pins in a 4-bit configuration
The connections have been updated and the pin numbers changed to use BCM
numbering (see comments in the file for details).

When run directly, it starts by initializing the panel and writing 'SETUP'.
Then it waits for the user to hit enter between each of the next phases:
position the cursor to the beginning of the second line and write
'Second Line', then write 'End' at the end of the second line, after which
the cursor is shown, hidden, and set blinking before finally waiting for
the user to hit enter again and then disconnecting from GPIO.

### drive_lcd_20x4

An updated version of the drive_lcd program, specifically for a 20x4 display.
There is more cursor addressing in this one to reflect the extra lines.

### drive_12864

Drive a slightly strange 128x64 display. It seems that most either have an
I2C or SPI interface, or 8 data bits and 2 chip selects. The one I bought is
different, and has strange GDRAM addressing instead.

### lcd_clock

Displays a clock on the first line of a connected LCD display using the drive_lcd
library. See drive_lcd for the connection details. It ensures that it always
releases the GPIO pins by having a `try...except` round the main loop to trap Ctrl-C.

### delorean

Show the top line from the Delorean display, and the second line is the current
time.

### drive_7_segment

Drive a seven segment, common-anode, display. Connections can be seen inside
the file. Currently set up for B+, assuming a 40-pin GPIO.

First, it shows 0-F with a delay between each. Then, it shows 6 arrows pointing
forward and back, right and left. Finally, it shows each possible letter and waits
for the user to press enter.

The simplest way to change to a common-cathode display would be to swap the names
of `segment_on()` and `segment_off()`.

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
4K Ohm resistor to the Base of the transistor, I'm drawing less than 1mA from
the Pi. The motor is drawing around 180mA when running freely. I'm going to try
stalling the motor a little to test its maximum draw once I have some crocodile
clips.

### read_ldr

Read a Light Dependent Resistor using the RC charge time of a capacitor. See
comments inside for details.

### servo

Drive a servo connected to pin 25 using software PWM. I don't think it's very
practical, but that may be more to do with the low quality servo I'm using. The
software PCM is wavering betwqeen about 47Hz and 51Hz whereas the servo really
wants a steady 50Hz.

----
## python/gpiozero

Examples using the GPIO Zero library.

### button_led

Using gpiozero library, switch a LED connected to GPIO17 on and off with a
button connected to GPIO21 and a GND.

### puffin

Emulate a complete British Puffin crossing. It has Red, Amber, and Green LEDs
for the cars, obviously. It uses a Red and Green LED for walk / don't walk
for pedestrians. It also uses another Red LED to indicate that the crossing
request button has been acknowledged.

### rgd_led

Drive a common-cathode RGB LED.

### robot2

Run a [CamJam Edukit 3 Robot](http://camjam.me/?page_id=1035).
Takes input from the user:

```
f   <n>     Forward for n steps
f   d       Forward until less than 10cm from obstacle
b   <n>     Backward for n steps
l   <n>     Left for n steps
r   <n>     Right for n steps
q           Quit
```

### fairy-lights

Control the battery-powered fairy lights that I bought this year. It randomly 
fades in and out and fashes at a couple of different speeds.

----
## python/pygame

Adventures in game / UI programming.

### bounce1

Bounce a (square!) ball around in a window.

### bounce2

Bounce a ball around in a box with a bouncy sound on each bounce. Use the cursor
keys to expand and contract the square that the ball is bouncing in.


----
## python/pygame/led_ui

Display buttons that turn LEDs on and off. Five buttons turn directly connected
LEDs on and off. Another seven buttons turn the segments of a display on and off.
Ten more buttons display the digits 0-9 on the 7-segment display and a final 25
buttons allow for most of the alphabet in upper or lower case.

See `main.py` and `.../gpio/drive_7_segment.py` for full connection details.


----
## python/wiimote

Examples using the python-cwiid library.
[The main CWiiD library information](https://help.ubuntu.com/community/CWiiD).

### wiimote

An example of using a Wiimote on a Pi, displays the state of the buttons and
the accelerometer data. It's a bit flaky with the £3.99 Wiimote clone that I
bought from eBay, It's a lot more stable with a genuine Nintendo one, the
rather noisy library can be squelched by using

```
    wiimote.py 2>/dev/null
```

if necessary.

### attitude

The beginning of a program to show the values returned from the accelerometers
with the Wiimote in different orientations. I have abandoned it for now
because my Wiimote clone is so flaky that there's no point continuing.


----
## python/robot

These are programs to drive a robot based on the [CamJam Edukit 3](http://camjam.me/?page_id=1035).

### 2-motors

Turn on both motors in one direction for 2 seconds.

### 3-driving

Move forward for a second, right for a second, and then left for a second.

### 4-line

Read the line-following sensor. Returns low (0V) for Black, and high (3.3V)
for white. It works at a distance of ~2.5cm (~1").

### 5-distance

Read the ultrasonic distance sensor. This returns high for the echo flight time.
This is then turned into a distance in cm.

A voltage divider is necessary to connect this to a Raspberry Pi because it is a 5V
peripheral. A 470R and a 330R resistor (provided in the EduKit 3) gives about 3V.

### 6-pwm

Use the software PWM in the `Rpi.GPIO` library to drive forward, right, and left at
about 30% power.

### raise_7890

Turn on all 4 lines. I was having trouble with the supplied H-bridge driver board,
so I needed to turn on all 4 lines that the board uses so that I could connect my
multimeter and see if there was voltage, which there wasn't with even one motor
connected.

**NB**: This should not be run with motors connected.


----
## i2c

Use the Adafruit I2C library to drive a normal LED connected to the first pin,
an RGB LED connected to the second, third, and fourth pins on a MCP23017 chip,
changing its colour every time a button connected to the fifth I/O pin.


----
## node

A [Blynk library](http://www.blynk.cc) client program that updates Virtual Pin
9 with the seconds
from the current time, responds to a slider on V1, updating a graph attached
to V4, and has a terminal on V3 which feeds back and sends notifications.


----
## scratch

The beginnings of an alien game. N.B. I can't draw :-)
