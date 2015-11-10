from datetime import datetime
import time

def check_sleep(amount):
    start = datetime.now()
    time.sleep(amount)
    end = datetime.now()
    delta = end-start
    return delta.seconds + delta.microseconds/1000000.

for value in [20, 10, 5, 2, 1, 0.5, 0.2, 0.1]:
    print("\nTesting %.1f ms" % value)

    max = -1.0
    min = 1.0
    sum = 0.0
    
    for i in range(1000):
        this = check_sleep(value / 1000.0)
    
        if this > max:
            max = this
    
        if this < min:
            min = this
    
        sum += abs(this - value / 1000.0)
    
    error = sum # / 1000.0
    
    print("  Min: %.3fms, Max: %.3fms" % (min * 1000, max * 1000))
    print("  Average error is %.3fms" % error)
    
