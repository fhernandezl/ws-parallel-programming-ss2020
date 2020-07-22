#! /usr/bin/env python3

from mpi4py import MPI
import sys
import math

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    assert len(sys.argv) > 1, "No max int provided, usage: python sum_roots.py [max int]"
    assert int(sys.argv[-1]), "Value provided is not an integer, got {}".format(sys.argv[-1])

max_int = int(sys.argv[-1])+1
partial_sum = 0
for i in range(rank, max_int, size):
    partial_sum += math.sqrt(i)

all_sums = comm.gather(partial_sum, root=0)

if rank == 0:
    total = sum(all_sums)
    print("Total sum:",total)
