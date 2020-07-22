import numpy as np
import time
import matplotlib.pyplot as plt

# CONST
init_func = lambda x: 100
x_min = 0
x_max = 6
x_res = 16
pause = .05
epochs = 100
bound = 0
plot_min = 0

x_range = np.linspace(x_min,x_max,x_res)
array = np.array(list(map(init_func, x_range)))
plot_max = np.max(array)

for t in range(epochs):
    new_array = np.zeros(x_res)
    for i in range(x_res):
        left_val = bound if i == 0 else array[i-1]
        right_val = bound if i == x_res-1 else array[i+1]
        new_array[i] = np.average([left_val,right_val])
    array = new_array
    plt.pause(pause)
    plt.clf()
    plt.scatter(x_range, array)
    plt.ylim(plot_min,plot_max)
    plt.draw()

print("Done!")