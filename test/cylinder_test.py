import sys

sys.path.append("/Users/cjaas/PycharmProjects/PhyllotacticPatterns/src/")

import Cylinder as cyl
import PlotPattern as pl

c = 0.1
nScales = 50
nCylinders = 2
alpha = 110   #degrees
rad = 0.3
height_diff = 4

coord_array = cyl.cylinder_pattern(nCylinders, nScales, alpha, rad, height_diff)

pl.plot_pattern_threeD(coord_array, 500 * c)