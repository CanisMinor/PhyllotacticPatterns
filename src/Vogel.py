import math
import numpy as np

def vogel(n,c):
    alphaRad = 3.14159265358979 * 137.508 / 180.0
    phiRad = n * alphaRad
    r = c * math.sqrt(n)
    x = r * math.cos(phiRad)
    y = r * math.sin(phiRad)

    return (x,y)

def vogel_planar_pattern(c, nFlorets):
    coords = []

    for floret in range(0,nFlorets):
        (x,y) = vogel(floret, c)
        coords.append((x,y))

    return np.array(coords)

