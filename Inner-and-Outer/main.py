# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy

a = numpy.array(input().split(), dtype=int)
b = numpy.array(input().split(), dtype=int)

print(f"{numpy.inner(a, b)}")
print(f"{numpy.outer(a, b)}")
