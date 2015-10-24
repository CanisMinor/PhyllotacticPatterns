from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import math

def find_limits(c_array):
    #all pattern have at least three dimensions,
    #however some have three dimensions

    #evaluate limits in the xy plane
    maxX = max(c_array[:,0])
    maxY = max(c_array[:,1])
    minX = min(c_array[:,0])
    minY = min(c_array[:,1])
    xTopLim = maxX + 0.1 * math.fabs(maxX)
    xBotLim = minX - 0.1 * math.fabs(minX)
    yTopLim = maxY + 0.1 * math.fabs(maxY)
    yBotLim = minY - 0.1 * math.fabs(minY)

    #evaluate limits along the vertical axis only for three-dimensional patterns
    if c_array.shape[1] == 3:
        maxZ = max(c_array[:,2])
        minZ = min(c_array[:,2])
        zTopLim = maxX + 0.1 * math.fabs(maxZ)
        zBotLim = minX - 0.1 * math.fabs(minZ)
        return (xBotLim, xTopLim, yBotLim, yTopLim, zBotLim, zTopLim)
    else:
        return (xBotLim, xTopLim, yBotLim, yTopLim)


#plot a two-dimensional pattern
def plot_pattern_twoD(coords_array, c):
    (xTopLim, xBotLim, yTopLim, yBotLim) = find_limits(coords_array)
    plt.scatter(coords_array[:,0], coords_array[:,1], marker='o', s=c)
    plt.axis([xBotLim, xTopLim, yBotLim, yTopLim])
    plt.axes().set_aspect('equal', 'datalim')
    plt.show()

#plot a three-dimensional pattern
def plot_pattern_threeD(coords_array, c):
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    (xTopLim, xBotLim, yTopLim, yBotLim, zBotLim, zTopLim) = find_limits(coords_array)

    ax.scatter3D(coords_array[:,0], coords_array[:,1], coords_array[:,2], 'gray') # c=coords_array[:,2], cmap='Greens')
    ax.plot3D(coords_array[:,0], coords_array[:,1], coords_array[:,2], 'gray')
    #plt.axis([xBotLim, xTopLim, yBotLim, yTopLim, zBotLim, zTopLim])
    #plt.axes().set_aspect('equal', 'datalim')
    plt.show()
