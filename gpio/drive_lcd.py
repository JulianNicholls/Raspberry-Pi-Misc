# Standard 16x2 / 16x4 / 20x4 LCD Pinout

# 1   GND       Ground
# 2   Vin       +2.7-5.5v apparently, but it seems to need +5v
# 3   Vss       LCD Power
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

#   GPIO Pins used

rs_pin  = 26    # RS !INS/DATA
e_pin   = 24    # E

db4_pin = 12    # DB4
db5_pin = 16    # DB5
db6_pin = 18    # DB6
db7_pin = 22    # DB7

# Set up all the above pins for output

def setup_pins():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(rs_pin, GPIO.OUT)
    GPIO.setup(e_pin, GPIO.OUT)
    GPIO.setup(db4_pin, GPIO.OUT)
    GPIO.setup(db5_pin, GPIO.OUT)
    GPIO.setup(db6_pin, GPIO.OUT)
    GPIO.setup(db7_pin, GPIO.OUT)

# Initialize the LCD for 4-bit operation

def setup_lcd():
    write_4_ins(2)
    write_4_ins(2)
    write_4_ins(8)      # 2-line, 5x7
    time.sleep(0.01)
    
    write_4_ins(0)
    write_4_ins(0xE)    # Display on, cursor on, blink off
    time.sleep(0.01)

    write_4_ins(0)      # Clear display
    write_4_ins(1)
    time.sleep(0.01)

    write_4_ins(0)
    write_4_ins(6)      # Increment on, shift off
    time.sleep(0.01)

# Clear the display and home the cursor to top-left

def clear():
    write_8_ins(0x01)

# Just home the cursor to the top-left without clearing the display

def home():
    write_8_ins(0x02)

# Set the cursor position by row and column, this only works for 16x2 and 20x2
# at the moment because I don't have a 16x4 or 20x4 LCD, or the docs. I recall 
# that line 2 runs on from line 0, and line 3 runs on from line 1, but I don't
# remember whether there is any gap in addressing.

def set_position(y, x):
    set_address_raw(y * 0x40 + x)

# Set the address in raw mode, line 0 starts at offset 0x00 and line 1 starts 
# at 0x40.

def set_address_raw(addr):
    write_8_ins(0x80 + addr)

# Output a piece of text, no note is taken about running off the right side.

def say(text):
    for i in text:
        write_8_data(ord(i))

# Write an 8-bit value as an instruction, just writes the top 4 bits followed 
# by the bottom 4 bits

def write_8_ins(value):
    write_4_ins(value >> 4)
    write_4_ins(value & 0x0F)

# Write a 4-bit value as an instruction.

def write_4_ins(value):
    write_4(value)
    GPIO.output(rs_pin, GPIO.LOW)
    strobe_e()


# Write an 8-bit value as a piece of data (text), just writes the top 4 bits 
# followed by the bottom 4 bits

def write_8_data(value):
    write_4_data(value >> 4)
    write_4_data(value & 0x0F)

# Write a 4-bit value as a piece of data (text).

def write_4_data(value):
    write_4(value)
    GPIO.output(rs_pin, GPIO.HIGH)
    strobe_e()

# Write a nybble to the 4 data lines

def write_4(value):
    GPIO.output(db4_pin, GPIO.HIGH if ((value & 1) == 1) else GPIO.LOW)
    GPIO.output(db5_pin, GPIO.HIGH if ((value & 2) == 2) else GPIO.LOW)
    GPIO.output(db6_pin, GPIO.HIGH if ((value & 4) == 4) else GPIO.LOW)
    GPIO.output(db7_pin, GPIO.HIGH if ((value & 8) == 8) else GPIO.LOW)

# Strobe the E lkine high for a minimum of 500ns. As can be seen, it is held
# high for 1ms.

def strobe_e():
    time.sleep(0.001)  # Limit is min 500ns, so this is plenty
    GPIO.output(e_pin, GPIO.HIGH)
    time.sleep(0.001)  # Limit is min 500ns, so this is plenty
    GPIO.output(e_pin, GPIO.LOW)
    time.sleep(0.001)  # Limit is min 500ns, so this is plenty

if __name__ == '__main__':
    setup_pins()
    setup_lcd()

    write_8_data(0x45)
    write_8_data(0x46)
    write_8_data(0x47)
    wait = raw_input()
    
    clear()
    say("Clear");
    wait = raw_input()
    
    home()
    say("Home...");
    wait = raw_input()
    
    set_address_raw(0x40)
    say("Second Line");
    wait = raw_input()
    
    set_position(1, 0xD)
    say("End");
    wait = raw_input()
    
    GPIO.cleanup()
    
