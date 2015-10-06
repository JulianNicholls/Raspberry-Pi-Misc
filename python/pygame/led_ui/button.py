import pygame

white   = (255, 255, 255)
black   = (0, 0, 0) 

#----------------------------------------------------------------------------
# Generic Button class that knows how to draw itself and returns true if it
# has been clicked.

class Button(object):
    def __init__(self, x, y, text, font, colour, width, height, x_offset, y_offset):
        self.x, self.y          = x, y
        self.width, self.height = width, height
        self.x_off, self.y_off  = x_offset, y_offset

        self.text   = text
        self.font   = font
        self.colour = colour

    def draw(self, screen):
        """ Draw the button rectangle and its text """
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))

        text_surface = self.font.render(self.text, 1, white) 
        screen.blit(text_surface, (self.x + self.x_off, self.y + self.y_off))

    def contains(self, pos):
        """ Return whether the passed position is part of the button """
        return pos[0] >= self.x and pos[0] < self.x + self.width and \
               pos[1] >= self.y and pos[1] < self.y + self.height

    def action(self):
        """ NULL Action """
        pass


#----------------------------------------------------------------------------
# PinButton Class that holds a Pin reference and draws based on it.

class PinButton(Button):
    def __init__(self, x, y, text, font, colour, off_colour, width, height, x_offset, y_offset, pin):
        super().__init__(x, y, text, font, colour, width, height, x_offset, y_offset) 

        self.pin        = pin
        self.off_colour = off_colour

    def draw(self, screen):
        """ Draw the button rectangle and its text sewnsitive to pin status """
        colour = self.colour if self.pin.active else self.off_colour
        pygame.draw.rect(screen, colour, (self.x, self.y, self.width, self.height))

        text_surface = self.font.render(self.text, 1, black if self.pin.active else white) 
        screen.blit(text_surface, (self.x + self.x_off, self.y + self.y_off))

    def action(self):
        """ Toggle the pin state """
        self.pin.toggle()


#----------------------------------------------------------------------------
# CharButton Class that allows for setting a whole raft of pins.

class CharButton(Button):
    def __init__(self, x, y, text, font, colour, width, height, x_offset, y_offset):
        super().__init__(x, y, text, font, colour, width, height, x_offset, y_offset) 

    def action(self):
        print("Pressed")

