#!/usr/bin/env python3

import spidev
import time

def read(adc_ch = 0, spi_ch = 0):
    conn = spidev.SpiDev(0, spi_ch)
    conn.max_speed_hz = 200000     # Constrain to 200kHz

    cmd_read = 0x80 if adc_ch == 0 else 0xA0

    reply_bytes = conn.xfer2([cmd_read, 0])

    print(reply_bytes, end=' ')
    print(256 * reply_bytes[0] + reply_bytes[1])

if __name__ == '__main__':
    while True:
        try:
            read()
            time.sleep(1);
        except KeyboardInterrupt:
            exit()

