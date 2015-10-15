#!/usr/bin/env python

# This program utilises the cwiid Python library in order to get input over 
# Bluetooth from a wiimote.

# The following lines of code demonstrate many of the features related to 
# wiimotes, such as capturing button presses and rumbling the controller.
# CPressing the Home button will start accelerometer reporting. Pressing it
# again will return to buttons
#
# Latest version by JGN. Thanks to The Raspberry Pi Guy and  Matt Hawkins.

import cwiid, time

button_delay = 0.3

button_bits = {
    cwiid.BTN_LEFT:     'Left',
    cwiid.BTN_RIGHT:    'Right',
    cwiid.BTN_UP:       'Up',
    cwiid.BTN_DOWN:     'Down',
    cwiid.BTN_A:        'Button A',
    cwiid.BTN_B:        'Button B',
    cwiid.BTN_1:        'Button 1',
    cwiid.BTN_2:        'Button 2',
    cwiid.BTN_MINUS:    'Minus Button',
    cwiid.BTN_PLUS:     'Plus Button',
    cwiid.BTN_HOME:     'Home',
}

exit_mask = cwiid.BTN_PLUS | cwiid.BTN_MINUS

def show_accelerometers():
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

    print 'Showing Accelerometer data, press HOME to exit'

    while((read_buttons() & cwiid.BTN_HOME) == 0):
        print "Accelerometers: ", read_accelerometers()
        time.sleep(0.1)     # Update about every 100ms

    time.sleep(button_delay)

    print 'Returning to buttons'
    wii.rpt_mode = cwiid.RPT_BTN
  
def read_buttons():
    return wii.state['buttons']

def read_accelerometers():
    return wii.state['acc']

def rumble_controller():
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0


print 'Please press buttons 1 + 2 on your Wiimote now...'
time.sleep(1)

# This code attempts to connect to your Wiimote and if it fails the program quits
try:
    wii = cwiid.Wiimote()
except RuntimeError:
    print "Cannot connect to your Wiimote. Run again and make sure you are holding buttons 1 + 2."
    quit()

print 'Wiimote connection established.\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

time.sleep(3)

wii.rpt_mode = cwiid.RPT_BTN

while True:
    buttons = read_buttons()

    if buttons == 0:
        continue

#    print "Buttons: ", buttons 
#    print "State:   ", wii.state    # Show the whole Wii state

    for btn in button_bits:
        if(buttons & btn):
            print button_bits[btn] + ' Pressed'
            time.sleep(button_delay)

    # If both + and - are held down, it rumbles and quits the program.
    if((buttons & exit_mask) == exit_mask):
        print '\nClosing connection ...'
        rumble_controller()
        exit(wii)
  
    # If HOME is pressed, switch to showing acceleometer data.
    if(buttons & cwiid.BTN_HOME):
        time.sleep(button_delay)
        show_accelerometers()

