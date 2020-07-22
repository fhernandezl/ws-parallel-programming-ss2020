#! /usr/bin/env python3

from mpi4py import MPI
import numpy as np
import matplotlib.pyplot as plt

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# CONST
x_min = 0
x_max = 6
x_res = 16
x_res_sub = int(x_res/size)
epochs = 101
plot_min = 0
save_epoch = [0,25,50,75,100]

array = None
if rank == 0:
    x_range = np.linspace(x_min,x_max,x_res)
    array = np.zeros([size,x_res_sub])
    array += 100
    plot_max = np.max(array)

sub_array = np.zeros(x_res_sub)
comm.Scatter(array, sub_array, root=0)

for t in range(epochs):
    new_sub_array = np.zeros(x_res_sub)

    reqs = []
    out_left = np.zeros(1)
    out_right = np.zeros(1)
    if rank != 0:
        reqs.append( comm.Isend(sub_array[0], dest=rank-1, tag=11) )
        reqs.append( comm.Irecv(out_left, source=rank-1, tag=12) )
    if rank != size-1:
        reqs.append( comm.Isend(sub_array[-1], dest=rank+1, tag=12) )
        reqs.append( comm.Irecv(out_right, source=rank+1, tag=11) )
    MPI.Request.waitall(reqs)

    for i in range(x_res_sub):
        left_val = out_left[0] if i == 0 else sub_array[i-1]
        right_val = out_right[0] if i == x_res_sub-1 else sub_array[i+1]
        new_sub_array[i] = np.average([left_val,right_val])

    sub_array = new_sub_array

    if t in save_epoch:
        full_array = None
        if rank == 0:
            full_array = np.zeros(x_res)
        comm.Gather(sub_array, full_array, root=0)
        if rank == 0:
            plt.clf()
            plt.scatter(x_range, full_array)
            plt.ylim(plot_min,plot_max)
            plt.savefig("epoch_{}".format(t))
