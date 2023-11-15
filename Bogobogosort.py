import random
import Generic_Methods as gen
import Bogosort as bogo

def Bogobogosort(array):
    step = 2
    finished = False
    while not finished:
        subArr = array[0:step]
        random.shuffle(subArr)
        array[0:step] = subArr
        if gen.checkSorted(subArr):
            step += 1
        else:
            step = 2
        if step > len(array):
            return array