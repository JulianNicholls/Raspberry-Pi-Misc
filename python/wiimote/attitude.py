#!/usr/bin/env python

# Show the values coming back from the accelerometers with the Wiimote in 
# different orientations.

# Thanks to The Raspberry Pi Guy and Matt Hawkins.

import cwiid, time

NUM_READINGS = 10

def read_accelerometers():
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

    print "Reading... ",

    readings = []

    for i in range(NUM_READINGS):
        readings.append(wii.state['acc'])
        time.sleep(0.2)

    wii.rpt_mode = cwiid.RPT_BTN
    print 'Done'

    return readings
  
def print_results(readings):
    sum = [0, 0, 0]
    min = [300, 300, 300]
    max = [-1, -1, -1]

    for i in range(NUM_READINGS):
        for j in range(3):
            r = readings[i][j]
            sum[j] += r

            if r > max[j]:
                max[j] = r

            if r < min[j]:
                min[j] = r

    print 'Average: ', sum
    print 'Minima:  ', min
    print 'Maxima:  ', max

print 'Please press buttons 1 + 2 on your Wiimote now...'
time.sleep(1)

# This code attempts to connect to your Wiimote and if it fails the program quits
try:
    wii = cwiid.Wiimote()
except RuntimeError:
    print "Cannot connect to your Wiimote. Run again and make sure you are holding buttons 1 + 2."
    quit()

print 'Wiimote connection established.\n'

time.sleep(3)

wii.rpt_mode = cwiid.RPT_BTN

raw_input('Place the Wiimote flat on a level surface and press enter')
readings = read_accelerometers()
print_results(readings)

