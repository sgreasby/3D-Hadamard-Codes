#!/usr/bin/env python
###########################################################
"Plot a 3 dimensional code matrix of width 2**n"

__author__     = "Steven Greasby"
__copyright__  = "Copyright (C) 2020 Steven Greasby"
__license__    = "GPL 2.0"
__url__        = "http://github.com/sgreasby/3d-hadamard-codes"
__maintainer__ = "Steven Greasby"
###########################################################

import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

usage = ("Usage: %s [order] {variant}\n"
         "       where order >= 1 and 1<=variant<=3")

# Parse Arguments
if len( sys.argv ) != 2 and len( sys.argv ) != 3:
    print( usage % sys.argv[0] )
    sys.exit()

try:
    order = int( sys.argv[1] )
except ValueError:
    print( usage % sys.argv[0] )
    sys.exit()

if len( sys.argv ) == 3:
    try:
        variant = int(sys.argv[2])
    except ValueError:
        print( usage % sys.argv[0] )
        sys.exit()
else:
    variant = 1

if ( order < 1 ) or ( variant < 1) or ( variant > 4 ):
    print( usage % sys.argv[0] )
    sys.exit()

size = 2 ** order

# Only the outer edges of the cube will be drawn if the size is
# used for the cube dimensions. To work around this add gaps
# between each of the smaller cubes used to construct the larger
# cube. The number of gaps is equal to the size minus 1, so the
# dimensions of the large cube is twice size minus 1.
cube_dims = np.array([size,size,size])*2-1

draw = np.zeros(cube_dims, dtype=int)
facecolors = np.empty(cube_dims, dtype=object)
edgecolors = np.empty(cube_dims, dtype=object)

# Walk through every x,y,z coordinate to get the code character
for z in range( size ):
    for y in range( size ):
        for x in range( size ):
            character = 0
            if variant == 1:
                a = (x^z) & (y^z)
            elif variant == 2:
                a = (x^y) & (y^z)
            elif variant == 3:
                a = (x^y) & (x^z)
            elif variant == 4:
                a = (x&y) | (x&z) | (y&z)
            for n in range( order ):
                character ^= (a>>n) & 1
            # For all of the following, swap the y and z axis. This will place
            # x on horizontal, y on vertical, and z on depth axis.
            # Indicate that the face/edge at this coordinate is to be drawn
            draw[y*2, z*2,x*2] = 1
            if character == 1:
                # code character is set
                facecolors[y*2, z*2, x*2] = '#FF000080'
                edgecolors[y*2, z*2, x*2] = '#808080'
            else:
                # code character is cleared
                facecolors[y*2, z*2, x*2] = '#F0F0F080'
                edgecolors[y*2, z*2, x*2] = '#808080'

# Get the indices, scale back down to account for the gaps added earlier
z, y, x = np.indices(np.array(draw.shape) + 1).astype(int) // 2
x[1::2, :, :] += 1
y[:, 1::2, :] += 1
z[:, :, 1::2] += 1

# Create a figure and get axes
figure = plt.figure()
axes = figure.gca(projection='3d')
# Swap limit of vertical axis (remember y and z are swapped)
axes.set_xlim(0,size) # horizontal
axes.set_ylim(0,size) # depth
axes.set_zlim(size,0) # vertical

# Plot the voxels, turn off the axis, then show the plot
axes.voxels(x, y, z, draw, facecolors=facecolors, edgecolors=edgecolors)
plt.axis('off')
plt.show()


