##############################################################################
# Driver library for an ST7920 128x64 LCD connected via SPI0.
#
# This is based on [Jamie Wood's ST7920 library](http://github.com/JMW95/pyST7920).
#
# Package Dependencies:
#
#   pypng   to decode the font png file.
#   spidev  to communicate via SPI.
#
# SPI needs to be enabled via raspi-config
#
##############################################################################

import spidev
import png

# Rotations
UPRIGHT     = 0
ROT_RIGHT   = 1
UPSIDE_DOWN = 2
ROT_LEFT    = 3

# Set or clear a pixel, line etc
SET         = True
CLEAR       = False

class ST7920:
    def __init__(self, rotation=UPRIGHT):
        """ Set up SPI and initialize the LCD. """
        # Set up SPI. The clock is upped to 1.2MHz, from the default 125kHz.
        #
        # The library on which this is based was setting the clock speed to 
        # 1.8MHz but that didn't work with my cheapo Chinese LCD.
        #
        # Empirically, 1.25MHz seems to work OK, but at 1.4MHz, the display
        # starts to break up, so I wound it back a little.
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.cshigh = True          # use inverted CS
        self.spi.max_speed_hz = 1200000 
        
        self.send(0, 0, 0x30)   # Basic instruction set
        self.send(0, 0, 0x30)   # Repeated
        self.send(0, 0, 0x0C)   # Display on
        
        self.send(0, 0, 0x34)   # Enable RE mode
        self.send(0, 0, 0x34)
        self.send(0, 0, 0x36)   # Enable graphics display
        
        self.set_rotation(0)    # rotate to 0 degrees
        
        self.fontsheet = self.load_font_sheet("fontsheet.png", 6, 8)
        
        self.clear()
        self.redraw()
    
    def set_rotation(self, rot):
        """ Set up the co-ordinate system, see definitions above """
        if rot == 0 or rot == 2:
            self.width  = 128
            self.height = 64
        elif rot == 1 or rot == 3:
            self.width  = 64
            self.height = 128

        self.rot = rot
    
    def load_font_sheet(self, filename, cw, ch):
        """ Load the text font. Initialized to a 6x8 font, by default """ 
        img    = png.Reader(filename).read()
        rows   = list(img[2])
        height = len(rows)
        width  = len(rows[0])
        sheet  = []

        for y in range(height / ch):
            for x in range(width / cw):
                char = []
                for sy in range(ch):
                    row = rows[(y * ch) + sy]
                    char.append(row[(x * cw):(x + 1) * cw])
                sheet.append(char)

        return (sheet, cw, ch)
    
    def send(self, rs, rw, cmds):
        """ Send a series of commands or data to the LCD """
        if type(cmds) is int:   # if a single arg, convert to a list
            cmds = [cmds]

        b1 = 0b11111000 | ((rw & 0x01) << 2) | ((rs & 0x01) << 1)
        bytes = []

        for cmd in cmds:
            bytes.append(cmd & 0xF0)
            bytes.append((cmd & 0x0F) << 4)
        return self.spi.xfer2([b1] + bytes)
    
    def clear(self):
        """
        Clear the LCD memory buffer. redraw() must be called subsequently
        to actually clear the display.
        """
        self.fbuff = [[0] * (128 / 8) for i in range(64)]
    
    def line(self, x1, y1, x2, y2, set=SET):
        """ Draw or clear a line between (x1, y1) and (x2, y2) """
        diffX = abs(x2 - x1)
        diffY = abs(y2 - y1)
        shiftX = 1 if (x1 < x2) else -1
        shiftY = 1 if (y1 < y2) else -1
        err = diffX - diffY
        drawn = False

        while not drawn:
            self.plot(x1, y1, set)
            if x1 == x2 and y1 == y2:
                drawn = True
                continue

            err2 = 2 * err

            if err2 > -diffY:
                err -= diffY
                x1  += shiftX

            if err2 < diffX:
                err += diffX
                y1  += shiftY
    
    def fill_rect(self, x1, y1, x2, y2, set=SET):
        """ 
        Draw or clear a solid rectangle.
        Corners: (x1, y1) and (x2, y2)
        """
        for y in range(y1, y2 + 1):
            self.line(x1, y, x2, y, set)
    
    def rect(self, x1, y1, x2, y2, set=SET):
        """ Draw or clear a rectangle outline """
        self.line(x1, y1, x2, y1, set)
        self.line(x2, y1, x2, y2, set)
        self.line(x2, y2, x1, y2, set)
        self.line(x1, y2, x1, y1, set)
    
    def plot(self, x, y, set=SET):
        """ 
        Set or clear a dot at (x, y). 
        This is where the co-ordinate rotation is taken care of
        """
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return

        if set:
            if self.rot == 0:
                self.fbuff[y][x / 8] |= 1 << (7 - (x % 8))
            elif self.rot == 1:
                self.fbuff[x][15 - (y / 8)] |= 1 << (y % 8)
            elif self.rot == 2:
                self.fbuff[63 - y][15 - (x / 8)] |= 1 << (x % 8)
            elif self.rot == 3:
                self.fbuff[63 - x][y / 8] |= 1 << (7 - (y % 8))
        else:
            if self.rot == 0:
                self.fbuff[y][x / 8] &= ~(1 << (7 - (x % 8)))
            elif self.rot == 1:
                self.fbuff[x][15 - (y / 8)] &= ~(1 << (y % 8))
            elif self.rot == 2:
                self.fbuff[63 - y][15 - (x / 8)] &= ~(1 << (x % 8))
            elif self.rot == 3:
                self.fbuff[63 - x][y / 8] &= ~(1 << (7 - (y % 8)))
    
    def put_text(self, s, x, y):
        """ Draw text string at (x, y) """
        for c in s:
            try:
                font, cw, ch = self.fontsheet
                char = font[ord(c)]
                sy = 0

                for row in char:
                    sx = 0

                    for px in row:
                        self.plot(x + sx, y + sy, px == 1)
                        sx += 1

                    sy += 1

            except KeyError:
                pass
            x += cw
    
    def redraw(self, dx1 = 0, dy1 = 0, dx2 = 127, dy2 = 63):
        """
        Redraw the screen.
        By default, the whole screen is redrawn.
        A bounding rectangle can be specified.
        """
        for i in range(dy1, dy2 + 1):
            self.send(0, 0, [0x80 + i % 32, 0x80 + ((dx1 / 16) + (8 if i >= 32 else 0))]) # set address
            self.send(1, 0, self.fbuff[i][dx1 / 16:(dx2 / 8) + 1])

