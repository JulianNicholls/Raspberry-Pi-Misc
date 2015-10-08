import RPi.GPIO as GPIO
import time

#############################################################################
#               Connections
#
# Pin numbers on the display that I have, which is mounted on a small PCB with
# a second display are in brackets below.
#
#        a(7)
#       ------
# (6)b |      | c(8)
#      | g(3) |
#       ------
# (4)d |      | e(1)
#      | f(2) |
#       ------
#
# Pin 9 is the common anode pin.
#
# Pin 5 is connected to segments c & e of a second display, giving a 1. The
# second display's common anode is also connected to pin 9.

# GPIO Pins
#          a   b   c   d   e   f   g   p5
pins    = [16, 22, 12, 18, 32, 38, 36, 35]

digits  = [
    0b1111110, 0b0010100, 0b1011011, 0b1010111, 0b0110101,  # 0-4
    0b1100111, 0b1101111, 0b1010100, 0b1111111, 0b1110111,  # 5-9
    0b1111101, 0b0101111, 0b1101010, 0b0011111, 0b1101011,  # A-E
    0b1101001                                               # F
]

letters = { # Included: ABCDEFGHIJ LNOP RS U YZ    Missing: KMQTVWX 
    'A': 0b1111101, 'a': 0b1011111, 'b': 0b0101111, 'C': 0b1101010, 
    'c': 0b0001011, 'd': 0b0011111, 'E': 0b1101011, 'F': 0b1101001, 
    'g': 0b1110111, 'H': 0b0111101, 'h': 0b0101101, 'I': 0b0010100, 
    'i': 0b0000100, 'J': 0b0010110, 'L': 0b0101010, 'n': 0b0001101, 
    'O': 0b1111110, 'o': 0b0001111, 'P': 0b1111001, 'r': 0b0001001, 
    'S': 0b1100111, 'U': 0b0111110, 'u': 0b0001110, 'y': 0b0110111, 
    'Z': 0b1011011
}

# The point are a combination of:
#   f   forward
#   s   straight
#   l   left
#   r   right
#   b   back

points = {
        'fs': 0b1110000, 'fl': 0b1100000, 'fr': 0b1010000,
        'bs': 0b0001110, 'bl': 0b0001010, 'br': 0b0000110
}

delay   = 0.4

# Set up pins for output

def setup_pins():
    GPIO.setmode(GPIO.BOARD)
    for p in pins:
        GPIO.setup(p, GPIO.OUT)

def count_to_15():
    for n in range(16):
        show_digit(n)
        time.sleep(delay)

def show_digit(n):
    d = digits[n]

    set_segments(d)

def set_segments(d):
    for i in range(7):
        if d & (64 >> i):
            segment_on(pins[i])
        else:
            segment_off(pins[i])

def segment_off(pin, delay = 0):
    GPIO.output(pin, GPIO.HIGH)
    if delay > 0:
        time.sleep(delay)

def segment_on(pin, delay = 0):
    GPIO.output(pin, GPIO.LOW)
    if delay > 0:
        time.sleep(delay)


if __name__ == '__main__':
    setup_pins()
    
    try:
        segment_off(pins[7])
        count_to_15()

        segment_on(pins[7])
        count_to_15()

        segment_off(pins[7])

        for l, v in points.iteritems():
            print l,
            set_segments(v)
            raw_input(" - Press Enter ")

        for l, v in letters.iteritems():
            print l,
            set_segments(v)
            raw_input(" - Press Enter ")
    
    except:
        pass
    
    GPIO.cleanup()

