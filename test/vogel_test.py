
import sys

sys.path.append("/Users/cjaas/PycharmProjects/PhyllotacticPatterns/src/")

import Vogel as vog
import PlotPattern as pl

c = 0.1
nFlorets = 1500

coord_array = vog.vogel_planar_pattern(c, nFlorets)

pl.plot_pattern_twoD(coord_array, 500*c)


