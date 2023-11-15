import Bogosort as bogo
import Bogobogosort as bogobogo
import Sleepsort as sleep
import time
import random

if __name__ == '__main__':
    start = time.perf_counter()
    arr = sleep.Sleepsort([1,6,8,13,12,5,3,9,2])
    clockTime = time.perf_counter() - start
    print("overall, " + str(clockTime))
    print(arr)