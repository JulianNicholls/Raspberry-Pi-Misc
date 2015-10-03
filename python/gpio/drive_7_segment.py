import RPi.GPIO as GPIO
import time

#        a(7)
#       ------
# (6)b | g(3) | c(8)
#       ------
# (4)d |      | e(1)
#       ------
#        f(2)
#
# Pin 5 is connected to segments c & e of another display, which has the same
# common anode.

#          a   b   c   d   e   f   g
pins    = [16, 22, 12, 18, 32, 38, 36 ]

digits  = [
    0b1111110, 0b0010100, 0b1011011, 0b1010111, 0b0110101,  # 0-4
    0b1100111, 0b1101111, 0b1010100, 0b1111111, 0b1110111   # 5-9
]

letters = { # Included: ABCDEFGHIJ LNOP RS U YZ    Missing: KMQTVWX 
    'A': 0b1111101, 'a': 0b1011111, 'b': 0b0101111, 'C': 0b1101010, 
    'c': 0b0001011, 'd': 0b0011111, 'E': 0b1101011, 'F': 0b1101001, 'g': 0b1110111, 
    'H': 0b0111101, 'h': 0b0101101, 'i': 0b0010100, 'J': 0b0010110, 'L': 0b0101010,
    'n': 0b0001101, 'O': 0b1111110, 'o': 0b0001111, 'P': 0b1111001,
    'r': 0b0001001, 'S': 0b1100111,
    'U': 0b0111110, 'u': 0b0001110, 'y': 0b0110111, 'Z': 0b1011011
}

delay   = 0.4

# Set up pins for output

def setup_pins():
    GPIO.setmode(GPIO.BOARD)
    for p in pins:
        GPIO.setup(p, GPIO.OUT)

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
    
    for n in range(10):
        show_digit(n)
        time.sleep(delay)
    
    for l, v in letters.iteritems():
        print l,
        set_segments(v)
        raw_input("- Press Enter ")

    GPIO.cleanup()

