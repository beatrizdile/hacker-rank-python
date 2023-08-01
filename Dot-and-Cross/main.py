# Enter your code here. Read input from STDIN. Print output to STDOUT
# A = numpy.array([ 1, 2 ])
# B = numpy.array([ 3, 4 ])
# dot(A, B): (A[0] * B[0]) + (A[1] * B[1])
# (1 * 3) + (2 * 4) = 11
# cross(A, B): (A[0] * B[1]) - (A[1] * B[0])
# (1 * 4) - (2 * 3) = -2

import numpy

size = int(input().strip())
a = numpy.array([input().split() for i in range(size)], dtype=int)
b = numpy.array([input().split() for i in range(size)], dtype=int)

print(f"{a.dot(b)}")
