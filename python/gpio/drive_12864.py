# 128x64 

# 1   Vss       Ground
# 2   Vdd       +2.7-5.5v apparently, but it seems to need +5v
# 3   VO        LCD Power
# 4   RS        _Instruction / Data
# 5   R/_W      Tie low for writing
# 6   E         Strobe High to set written data
# 7   DB0       Data Bus bit 0 - Not Connected
# 8   DB1       Data Bus bit 1 - Not Connected
# 9   DB2       Data Bus bit 2 - Not Connected
#10   DB3       Data Bus bit 3 - Not Connected
#11   DB4       Data Bus bit 4
#12   DB5       Data Bus bit 5
#13   DB6       Data Bus bit 6
#14   DB7       Data Bus bit 7

import RPi.GPIO as GPIO
import time

#   GPIO BCM Pins used

rs_pin  = 16          # RS _INS/DATA
e_pin   = 12          # E Strobe

db4_pin = 25        # DB4
db5_pin = 24        # DB5
db6_pin = 23        # DB6
db7_pin = 18        # DB7


# Cursor settings

OFF         = 0x04
ON          = 0x06
BLINKING    = 0x07

# Set up all the above pins for output and initialise the display for
# 4-bit operation

def setup():
    # Initialise GPIO Pins.

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(rs_pin, GPIO.OUT)
    GPIO.setup(e_pin, GPIO.OUT)
    GPIO.setup(db4_pin, GPIO.OUT)
    GPIO.setup(db5_pin, GPIO.OUT)
    GPIO.setup(db6_pin, GPIO.OUT)
    GPIO.setup(db7_pin, GPIO.OUT)

    # Set up LCD interface

    write_4_ins(2)
    write_4_ins(0)
    time.sleep(0.0005)

    write_4_ins(2)
    write_4_ins(0)
    time.sleep(0.0005)

    write_4_ins(0)
    write_4_ins(0xE)    # Display on, cursor on, blink off
    time.sleep(0.0005)

    write_4_ins(0)      # Clear display
    write_4_ins(1)
    time.sleep(0.012)

    write_4_ins(0)
    write_4_ins(6)      # Increment on, shift off

def release_pins():
    GPIO.cleanup()

# Clear the display and home the cursor to top-left

def clear():
    write_8_ins(0x01)

# Just home the cursor to the top-left without clearing the display

def home():
    write_8_ins(0x02)

def set_cursor(setting):
    write_8_ins(0x08 + setting)

# Set the cursor position by row and then column, sort of.
# Actually only every other pair of cells can be addressed, i.e.
#   line 0:
#   00: XX   01: XX   02: XX   03: XX   04: XX   05: XX   06: XX   07: XX

def set_position(y, x):
    lines = (0x00, 0x10, 0x08, 0x18)
    set_DDRAM_address(lines[y] + x)

# Set the address in raw mode.., The addressing is 16-bit word wise and each
# line contains 16 characters in 8 words.
# line 0 starts at 0x00 and line 2 is contiguous with it, starting at 0x08.
# line 2 starts at 0x10 and line 4 is contiguous with it, starting at 0x18.

def set_DDRAM_address(addr):
    write_8_ins(0x80 + addr)

# Enter and leave graphics mode

def set_graphics_mode():
    write_8_ins(0x24)
    write_8_ins(0x26)

def clear_graphics_mode():
    write_8_ins(0x24)
    write_8_ins(0x20)

# Set the GDRAM address

def set_GDRAM_address(row, col):
    write_8_ins(0x80 + row)
    write_8_ins(0x80 + col)

# Output a piece of text, no note is taken about running off the right side.

def say(text):
    for i in text:
        write_8_data(ord(i))

# Write an 8-bit value as an instruction, just writes the top 4 bits followed
# by the bottom 4 bits

def write_8_ins(value):
    write_4_ins(value >> 4)
    write_4_ins(value & 0x0F)

# Write a 4-bit value as an instruction (RS low).

def write_4_ins(value):
    GPIO.output(rs_pin, GPIO.LOW)
    write_4(value)
    strobe_e()


# Write an 8-bit value as a piece of data (text), just writes the top 4 bits
# followed by the bottom 4 bits

def write_8_data(value):
    write_4_data(value >> 4)
    write_4_data(value & 0x0F)

# Write a 4-bit value as a piece of data (text) (RS high).

def write_4_data(value):
    GPIO.output(rs_pin, GPIO.HIGH)
    write_4(value)
    strobe_e()

# Write a nybble to the 4 data lines

def write_4(value):
    GPIO.output(db4_pin, GPIO.HIGH if ((value & 1) == 1) else GPIO.LOW)
    GPIO.output(db5_pin, GPIO.HIGH if ((value & 2) == 2) else GPIO.LOW)
    GPIO.output(db6_pin, GPIO.HIGH if ((value & 4) == 4) else GPIO.LOW)
    GPIO.output(db7_pin, GPIO.HIGH if ((value & 8) == 8) else GPIO.LOW)

# Strobe the E line high for a minimum of 500ns. As can be seen, it is held
# high for 500us. It seems that asking for 500us from time.sleep() is fairly
# reasonable (see test_sleep.py for testing).

def strobe_e():
    time.sleep(0.0005)  # Limit is min 500ns, so this (500us) is plenty
    GPIO.output(e_pin, GPIO.HIGH)
    time.sleep(0.0005)
    GPIO.output(e_pin, GPIO.LOW)
    time.sleep(0.0005)



if __name__ == '__main__':
    setup()

    write_8_data(0x53)  # 'S'
    write_8_data(0x45)  # 'E'
    write_8_data(0x54)  # 'T'
    write_8_data(0x55)  # 'U'
    write_8_data(0x50)  # 'P'
    write_8_data(0x20)  # ' '
    set_cursor(OFF)
    wait = raw_input('SETUP ')

    clear()
    set_graphics_mode()
    wait = raw_input('Graphics Mode ')

    set_graphics_mode()
    set_GDRAM_address(0, 0)
    write_8_data(0x55)
    write_8_data(0x55)
    set_GDRAM_address(2, 0)
    write_8_data(0xaa)
    write_8_data(0xaa)

    wait = raw_input('Checkerboard ')

    clear_graphics_mode()
    set_DDRAM_address(0)
    say("Out ")
    wait = raw_input('Out of Graphics Mode ')

    release_pins()

