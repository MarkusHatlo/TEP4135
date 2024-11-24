import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


def oppgave1():
    u, r, theta, b = sp.symbols("u r theta b")
    return -sp.diff(u*r*sp.sin(theta)-b/r*sp.sin(theta), r)

#print(oppgave1())

def oppgave1b():
    x, y, q, u, r, theta = sp.symbols("x y q u r theta")
    return sp.diff(q/(2*sp.pi)*sp.atan(y/x),y)

