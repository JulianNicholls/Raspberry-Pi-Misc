from datetime import datetime
import time

def check_sleep(amount):
    start = datetime.now()
    time.sleep(amount)
    end = datetime.now()
    delta = end-start
    return delta.seconds + delta.microseconds/1000000.

value = 0.0005  # 500us

max = -1.0
min = 1.0
sum = 0.0

for i in xrange(1000):
    this = check_sleep(value)

    if this > max:
        max = this

    if this < min:
        min = this

    sum += abs(this - value)

error = sum # / 1000.0

print "Min: %.5f, Max: %.5f" % (min, max)
print "Average error is %0.3fms" % error

