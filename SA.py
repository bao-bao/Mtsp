"""
    Created by AMXPC on 2017/4/22.
"""
import numpy as np
import pandas as pd
import random
import math
import Tour

Temperature = 100000
Coolrate = 0.0003
Coefficient = 0.3


def acceptanceprob(energy, newenergy, temperature):
    if newenergy < energy:
        return 1.0
    return math.exp(100 * (energy - newenergy) / temperature)


def calenergy(x):
    d1, d2 = x.getdist()
    if d1 < d2:
        mindist = d1
    else:
        mindist = d2
    if mindist != 0:
        e = (abs(d1 - d2)/(Coefficient * mindist)) * (d1 + d2) + (d1 + d2)
        return e


def simulatedannealing(graph, initpath):
    global Temperature, Coolrate
    # currentsolution = Tour.Tour('random')
    currentsolution = Tour.Tour('null')
    currentsolution.settour(initpath)
    currentsolution.setdist(graph)
    best = Tour.Tour('null')
    best.settour(currentsolution.gettour())
    best.setdist(graph)

    while Temperature > 1:
        newsolution = Tour.Tour('null')
        newsolution.settour(currentsolution.gettour())
        newsolution.randomtour()
        newsolution.setdist(graph)

        currentenergy = calenergy(currentsolution)
        neighbourenergy = calenergy(newsolution)
        # print "CE = %.2f, NE = %.2f" % (currentenergy, neighbourenergy)

        if acceptanceprob(currentenergy, neighbourenergy, Temperature) > random.random() / 1.0:
            currentsolution.settour(newsolution.gettour())
            currentsolution.setdist(graph)

        if currentenergy < calenergy(best) or neighbourenergy < calenergy(best):
            best.settour(currentsolution.gettour())
            best.setdist(graph)
            # print best.gettour()

        Temperature *= (1 - Coolrate)
        # print Temperature

    return best

if __name__ == "__main__":
    data = pd.read_csv("finalUCG.csv")
    init = np.loadtxt(open("iniResult.csv", "rb"), delimiter=",", skiprows=1, dtype=int)
    besttour = simulatedannealing(data, init)

    bt1 = []
    dist1, dist2 = besttour.getdist()
    bt2 = [data.columns[0]]

    i = 0
    while besttour.gettour()[i] != Tour.size:
        bt1.append(data.columns[besttour.gettour()[i] - 1])
        i += 1
    bt1.append(data.columns[0])
    i += 1
    while i < Tour.size:
        bt2.append(data.columns[besttour.gettour()[i] - 1])
        i += 1
    bt2.append(data.columns[0])

    print bt1, dist1
    print bt2, dist2
