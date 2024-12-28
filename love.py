import math
from turtle import *

def hearth(k):
    return 15*math.sin(k)**3

def hearth1 (k):
    return 12*math.cos(i)-5*\
        math.cos(2*k)-2*\
        math.cos(3*k)-\
        math.cos(4*k)

speed(1000)
bgcolor('black')
for i in range(6000):
    goto(hearth(i)*20,hearth1(i)*20)
    for j in range(5):
        color('pink')

done()