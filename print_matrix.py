#!/usr/bin/env python
###########################################################
"Print a 3 dimensional code matrix of width 2**n"

__author__     = "Steven Greasby"
__copyright__  = "Copyright (C) 2020 Steven Greasby"
__license__    = "GPL 2.0"
__url__        = "http://github.com/sgreasby/3d-hadamard-codes"
__maintainer__ = "Steven Greasby"
###########################################################

import sys
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

cube_dims = np.array([size,size,size])
matrix = np.zeros(cube_dims, dtype=int)

# Walk through every x,y,z coordinate to get the code character
for z in range( size ):
    for y in range( size ):
        for x in range( size ):
            if variant == 1:
               a = (x^z) & (y^z)
            elif variant == 2:
                a = (x^y) & (y^z)
            elif variant == 3:
                a = (x^y) & (x^z)
            elif variant == 4:
                a = (x&y) | (x&z) | (y&z)
            for n in range( order ):
                matrix[z, y, x] ^= (a>>n) & 1
                
print( matrix )


