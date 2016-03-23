import scrollphat as hat
import time

str = 'Merry Christmas   '
hat.set_brightness(2)
hat.write_string(str)

# for i in range(len(str) * 5):
#     hat.scroll()
#     time.sleep(0.150)

hat.graph([2, 4, 6, 8, 10, 8, 6, 4, 2, 0, 3])
hat.update()

