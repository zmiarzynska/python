import math
from random import random


def calc_pi(n=100):
    k=0
    for i in range(n):
        x =random()
        y =random()
        if(x*x+y*y<=1):
            k+=1
    pi=4*k/n
    print(pi)

calc_pi()