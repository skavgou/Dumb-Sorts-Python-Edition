import Bogosort as bogo
import Bogobogosort as bogobogo
import time
import random

if __name__ == '__main__':
    start = time.perf_counter()
    arr = bogobogo.Bogobogosort([2,6,13,1,5,4])
    clockTime = time.perf_counter() - start
    print("overall, " + str(clockTime))
    print(arr)