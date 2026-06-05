# coding=windows-1251
import numpy as np

def function(x, y, z):
    return 1

def tx(y, z):
    return (1-y**2)**(1/2)
def bx(y, z):
    return y**2

def ty(x, z):
    return 1
def by(x, z):
    return 0

def tz(x, y):
    return 15*x
def bz(x, y):
    return 0

def order():
    return['y', 'x', 'z']