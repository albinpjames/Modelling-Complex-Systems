import matplotlib
matplotlib.use('TkAgg')
from pylab import *
import pycxsimulator

import random as rd
n =1000
sd = 0.1

def initialize():
    global xlist, ylist
    xlist = []
    ylist = []
    for i in range(n):
        xlist.append(rd.gauss(0,1))
        ylist.append(rd.gauss(0,1))

def observe():
    global xlist, ylist
    cla()
    plot(xlist, ylist, '.')

def update():
    global xlist, ylist
    for i in range(n):
        xlist[i] += rd.gauss(0,0.1)
        ylist[i] += rd.gauss(0,0.1)