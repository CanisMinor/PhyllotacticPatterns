import argparse
import Vogel as vog
import Cylinder as cyl
import PlotPattern as pl

parser = argparse.ArgumentParser(description='Tool for generating phyllotactic patterns.')
parser.add_argument('pattern', type=int, help='pattern type:\n 0 (planar Fermat spiral)\n 1 (cylindrical model)')

parser.add_argument("-n", "--npoints", type=int, help="number of points per spiral")

#parser.add_argument('--npoints', action='store_const', type=int, required=True, help='')
parser.add_argument('--nspiral', default=1, help='number of spirals')
parser.add_argument('--scale', type=float, help='scaling parameter')
parser.add_argument('--radius', type=float, help='radius of cylinder')
parser.add_argument('--alpha', type=float, help='angular separation of consecutive points (in degrees)')
parser.add_argument('--height', type=float, help='height separation of consecutive points')



args = parser.parse_args()


#check arguments make sense
if args.pattern == 0:
    if args.height is not None:
        print("Height parameter not required for Fermi spiral; ignoring height parameter.")
    if args.alpha is not None:
        print("Angular separation parameter not required for Fermi spiral; ignoring angular separation parameter.")
    if args.radius is not None:
        print("Radius parameter not required for Fermi spiral; ignoring radius parameter.")
elif args.pattern == 1:
    if args.scale is not None:
        print("Scaling parameter not required for cylindrical phyllotactic; ignoring scaling parameter.p")
else:
    print("Error: invalid choice of pattern; must be 0 (planar Fermi spiral) or 1 (cylindrical model).")

#run appropriate pattern
if args.pattern == 1:
    coord_array = cyl.cylinder_pattern(args.nspiral, args.npoints, args.alpha, args.radius, args.height)
    pl.plot_pattern_threeD(coord_array, 500 * args.scale)
else:
    coord_array = vog.vogel_planar_pattern(args.scale, args.npoints)
    pl.plot_pattern_twoD(coord_array, 500*args.scale)


