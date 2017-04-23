"""
    Created by AMXPC on 2017/4/22.
"""
import numpy as np
import random

size = 141


class Tour:
    __tour = 0
    __distance1 = 0
    __distance2 = 0

    def __init__(self, randomly):
        self.__tour = np.linspace(1, size, size, dtype=int)
        # get a random start solution
        if randomly == 'random':
            for i in xrange(1, size):
                index = random.randint(1, size - 1)
                temp = self.__tour[index]
                self.__tour[index] = self.__tour[i]
                self.__tour[i] = temp

    def setdist(self, x):
        self.__distance1 = 0
        self.__distance2 = 0
        i = 1
        # from start point to virtual start point
        while self.__tour[i] != size:
            self.__distance1 += x.values[self.__tour[i - 1] - 1][self.__tour[i] - 1]
            i += 1
        self.__distance1 += x.values[self.__tour[i - 1] - 1][self.__tour[i] - 1]
        i += 1
        # from virtual start point to start point
        while i < size:
            self.__distance2 += x.values[self.__tour[i - 1] - 1][self.__tour[i] - 1]
            i += 1
        self.__distance2 += x.values[self.__tour[i - 1] - 1][self.__tour[0] - 1]
        return self

    def getdist(self):
        return self.__distance1, self.__distance2

    def settour(self, x):
        for i in xrange(size):
            self.__tour[i] = x[i]
        return self

    def gettour(self):
        return self.__tour

    def randomtour(self):
        index1 = random.randint(1, size - 1)
        index2 = random.randint(1, size - 1)
        temp = self.__tour[index1]
        self.__tour[index1] = self.__tour[index2]
        self.__tour[index2] = temp
