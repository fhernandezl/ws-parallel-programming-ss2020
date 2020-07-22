import sys
import math

assert len(sys.argv) > 1, "No max int provided, usage: python sum_roots.py [max int]"
assert int(sys.argv[-1]), "Value provided is not an integer, got {}".format(sys.argv[-1])

total = 0
for i in range(1,int(sys.argv[-1])+1):
    total += math.sqrt(i)

print("Final sum:",total)
