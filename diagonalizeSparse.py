#!/usr/bin/python

import numpy as np
from scipy.sparse import csr_matrix, lil_matrix
from scipy.linalg import eigh

from scipy.sparse.linalg import eigsh
import sys

fileName = "matrix.dat"
if len(sys.argv) > 1:
    fileName = sys.argv[1]
matFile = open(fileName,"r")
# Read the file, dimension is expected in first line
line = matFile.readline()
dimension = int(line.split("dimension ")[1])
print int(dimension)
theMatrix = lil_matrix((dimension, dimension), dtype=np.complex_)
line = matFile.readline()
count = 0
while line:
 #   print line
    vals = line.split('  ')
 #   print vals
    row = int(vals[0])
    col = int(vals[1])
    # remove newline from string
    valMed = vals[2].replace(')','')
    valEnd = valMed.replace('(','');
    realPart = float(valEnd.split(',')[0])
    imagPart = float(valEnd.split(',')[1])
    value = np.complex(realPart,imagPart)
#    print row,col, realPart, imagPart, value
    theMatrix[row,col]=value
    theMatrix[col,row]=np.conj(value)
    line = matFile.readline()
    count = count +1
    if (count == 200000):
        print count
        count = 0
matFile.close()
# construct the matrix

# read the matrix line by line 
print ("Have Matrix, transforming...")
theMatrix.tocsr()
np.set_printoptions(suppress=True)


print ("Now for 30 eigenvalues")
evals_large, evecs_large = eigsh(theMatrix, 30, which='LM')


print(evals_large)

np.savetxt("Spectrum.dat", evals_large)
np.savetxt("Eignevectors.dat", evecs_large)

