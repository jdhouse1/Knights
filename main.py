# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 00:48:46 2019

@author: Owner
"""
from itertools import product
import numpy as np

class position(tuple):
    def __add__(self,other):
        return (self[0]+other[0],self[1]+other[1])

def square(x,y):
    n = max(abs(x),abs(y))
    s = (2*n+1)**2
    if y==n:
        return s + x - n
    elif x==-n:
        return s - 3*n + y
    elif y==-n:
        return s - 5*n - x
    elif x==n:
        return s - 7*n - y

class Knight:
    def __init__(self):
        self.pos=position((0,0))
        self.hist = []
    def move(self):
        minimum = np.inf
        delta = None
        for d in product((-1,1),(2,-2)):
            newPosition = self.pos + position(d)
            if newPosition not in self.hist:
                if square(*newPosition)<minimum:
                    delta = position(d)
                    minimum = square(*newPosition)
        for d in product((-2,2),(1,-1)):
            newPosition = self.pos + position(d)
            if newPosition not in self.hist:
                if square(*newPosition)<minimum:
                    delta = position(d)
                    minimum = square(*newPosition)
        if delta:
            self.hist.append(self.pos)
            self.pos = position(self.pos+ delta)
            return self.pos
        else:
            return None
