import RPi.GPIO as gpio

#----------------------------------------------------------------------------
# GPIO Pin class that holds a GPIO pin number, current state, and active
# low status.

class Pin(object):
    def __init__(self, number, active = False, active_low = False):
        """ Initialise with the pin number, start state, and active low status """
        self.number     = number
        self.active     = active
        self.active_low = active_low

        gpio.setup(self.number, gpio.OUT)

        self.set_state()

    def set_active(self, active = True):
        """ Can be called as set_active() or set_active(True / False) """
        self.active = active
        self.set_state()

    def set_inactive(self):
        """ Essentially syntactic sugar for set_active(False) """
        self.set_active(False)

    def set_state(self):
        """ Set the hardware pin based on state and active low """
        hilo = gpio.HIGH if self.active != self.active_low else gpio.LOW
        gpio.output(self.number, hilo)

    def toggle(self):
        """ Toggle the state and action it """
        self.active = not self.active
        self.set_state()

