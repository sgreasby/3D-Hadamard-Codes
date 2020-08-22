# 3D Hadamard Codes
Get more info about the theory at http://www.hadamardcodes.com

## Description
This repository contains algorithms for generating 3-Dimensional
Hadamard code cubes.

## Requirements
All scripts are compatible with both Python 2 and Python 3.
The plot_matrix.py script requires matplotlib.

## Usage
All scripts are executed from the command line as shown below.
It is recommended that users begin with order=1.
Then, increment the order and run the script(s) again.
The matrix size grow exponentially so large values of "order" will significantly impact processing time.

**print_matrix.py** - Prints the 3D Hadamard matrix to the screen.  
Usage: `print_matrix.py [order] {variant}`  
&nbsp;&nbsp;&nbsp;&nbsp;where order >= 1 and 1<=variant<=4

**plot_matrix.py** - Plots the 3D Hadamard matrix.  
Usage: `plot_matrix.py [order] {variant}`  
&nbsp;&nbsp;&nbsp;&nbsp;where order >= 1 and 1<=variant<=4 

