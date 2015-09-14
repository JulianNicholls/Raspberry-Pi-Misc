import RPi.GPIO as GPIO
import time

rs_pin  = 26    # RS !INS/DATA
e_pin   = 24    # E

db4_pin = 12    # DB4
db5_pin = 16    # DB5
db6_pin = 18    # DB6
db7_pin = 22    # DB7

def setup_pins():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(rs_pin, GPIO.OUT)
    GPIO.setup(e_pin, GPIO.OUT)
    GPIO.setup(db4_pin, GPIO.OUT)
    GPIO.setup(db5_pin, GPIO.OUT)
    GPIO.setup(db6_pin, GPIO.OUT)
    GPIO.setup(db7_pin, GPIO.OUT)


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

def clear():
    write_8_ins(0x01)

def home():
    write_8_ins(0x02)

def set_position(y, x):
    set_address_raw(y * 0x40 + x)

def set_address_raw(addr):
    write_8_ins(0x80 + addr)

def say(text):
    for i in text:
        write_8_data(ord(i))

def write_8_ins(value):
    write_4_ins(value >> 4)
    write_4_ins(value & 0x0F)

def write_4_ins(value):
    write_4(value)
    GPIO.output(rs_pin, GPIO.LOW)
    strobe_e()


def write_8_data(value):
    write_4_data(value >> 4)
    write_4_data(value & 0x0F)

def write_4_data(value):
    write_4(value)
    GPIO.output(rs_pin, GPIO.HIGH)
    strobe_e()


def write_4(value):
    GPIO.output(db4_pin, GPIO.HIGH if ((value & 1) == 1) else GPIO.LOW)
    GPIO.output(db5_pin, GPIO.HIGH if ((value & 2) == 2) else GPIO.LOW)
    GPIO.output(db6_pin, GPIO.HIGH if ((value & 4) == 4) else GPIO.LOW)
    GPIO.output(db7_pin, GPIO.HIGH if ((value & 8) == 8) else GPIO.LOW)


def strobe_e():
    time.sleep(0.001)  # Limit is min 500ns, so this is plenty
    GPIO.output(e_pin, GPIO.HIGH)
    time.sleep(0.001)  # Limit is min 500ns, so this is plenty
    GPIO.output(e_pin, GPIO.LOW)
    time.sleep(0.001)  # Limit is min 500ns, so this is plenty


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

