from st7920   import ST7920 
from datetime import datetime

screen = ST7920()

previous = datetime.now()
delta    = datetime.now() - previous

while True:
    try:
        screen.clear()
        screen.rect(0, 0, 127, 63);
        screen.fill_rect(2, 22, 125, 61);
        screen.fill_rect(4, 24, 123, 59, False);

        screen.plot(50, 10)
        screen.plot(60, 10)
        screen.plot(70, 10)

        screen.put_text("Cycle: %.1f ms" % (delta.microseconds / 1000.0), 16, 36)

        screen.redraw()

        now      = datetime.now()
        delta    = now - previous
        previous = now

    except KeyboardInterrupt:
        exit()
