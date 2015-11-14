#!/usr/bin/env python3

from Adafruit_MCP230xx import Adafruit_MCP230XX

red_led = 0     # Single Red LED
red     = 1     # Parts of an RGB LED
green   = 2
blue    = 3

button  = 4     # Button input

mcp = Adafruit_MCP230XX(address = 0x20, num_gpios = 16) # MCP23017

bit_led = 1

bit0 = 0;
bit1 = 0;
bit2 = 0;

# Set pins 0-3 to output
mcp.config(red_led, mcp.OUTPUT)
mcp.config(red, mcp.OUTPUT)
mcp.config(green, mcp.OUTPUT)
mcp.config(blue, mcp.OUTPUT)

# Set pin 4 to input with the pullup resistor enabled
mcp.config(button, mcp.INPUT)
mcp.pullup(button, 1)

mcp.output(red_led, 1)
mcp.output(red, 1)
mcp.output(green, 1)
mcp.output(blue, 1)

while True:
    while mcp.input_01(button) == 1:
        pass

    bit0 = 1 - bit0
    bit_led = 1 - bit_led

    if bit0 == 0:
        bit1 = 1 - bit1

        if bit1 == 0:
            bit2 = 1 - bit2

    mcp.output(red_led, bit_led)
    mcp.output(red, bit0)
    mcp.output(green, bit1)
    mcp.output(blue, bit2)

    while mcp.input_01(button) == 0:
        pass

