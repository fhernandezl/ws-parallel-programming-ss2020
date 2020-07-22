import sys
import math

assert len(sys.argv) > 1, "No max int provided, usage: python sum_roots.py [max int]"
assert int(sys.argv[1]), f"Value provided in not an integer, got {sys.argv[1]}"

total = 0
for i in range(1,int(sys.argv[1])+1):
    total += math.sqrt(i)

print(f"Final sum: {total}")