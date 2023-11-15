# This is a sample Python script.
import random
import Generic_Methods as generic
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def bogosort(array):
    finished = False
    while not finished:
        random.shuffle(array)
        if generic.checkSorted(array):
            return array


# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
