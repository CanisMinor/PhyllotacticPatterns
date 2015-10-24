import numpy as np
import math

def simple_cylinder(n, alpha, r, h, phaseAngle):
    """Evaluate coordinate for a scale in a simple cylinder model.

    Keyword arguments:
    n -- scale index
    alpha -- divergence angle between two consecutive scales
    r -- radius of cylinder
    h -- vertical distance between two consecutive scales

    """

    phiRad = phaseAngle + (n * alpha)
    x = r * math.cos(phiRad)
    y = r * math.sin(phiRad)
    z = h * n

    return (x,y,z)


def cylinder_pattern(nCylinders, nScales, alpha, r, h):
    """Evaluate cylinder pattern.

    Keyword arguments:
    nScales -- number of scales
    alpha -- divergence angle between two consecutive scales
    r -- radius of cylinder
    h -- vertical distance between two consecutive scales
    typeCylinder -- pick simple (0) or conjugate (1) cylinder model

    """

    coords = []
    alphaRad = math.pi * alpha / 180.0
    dTheta = 2.0 * math.pi / nCylinders

    for iCylinder in range(0, nCylinders):
        phaseAngle = iCylinder * dTheta
        for iScale in range(0,nScales):
            (x,y,z) = simple_cylinder(iScale, alphaRad, r, h, phaseAngle)
            coords.append((x,y,z))

    return np.array(coords)
