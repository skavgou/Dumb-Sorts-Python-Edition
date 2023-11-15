import time
import threading
import Generic_Methods as gen

def SleepFor(val, arr):
    time.sleep(val/500)
    arr.append(val)

def Sleepsort(array):
    array_of_threads = []
    newArr = []
    for i in array:
        newThread = threading.Thread(target=SleepFor, args=(i, newArr))
        array_of_threads.append(newThread)
    for i in array_of_threads:
        i.start()
    for i in array_of_threads:
        i.join()
    return newArr