#!/usr/bin/env python3

from gpiozero import MCP3204 
import time

atod = MCP3204(0, 0)    # Channel 0 on Device 0

def read():
    global atod

    value = atod.value

#    print(value)
    print("Raw: %.5f, @5: %4.2fV, @3.3: %4.2fV" % (value, value * 5.0, value * 3.3));

if __name__ == '__main__':
    while True:
        try:
            read()
            time.sleep(1);
        except KeyboardInterrupt:
            exit()

