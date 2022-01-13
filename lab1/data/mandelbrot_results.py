import os

from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d

machine_plots = dict()
for filename in os.listdir():
    if filename[-4:] == ".csv":
        file = open(filename, 'r')
        lines = file.readlines()
        data = [line.strip().split(',') for line in lines[1:]]
        data = [[int(d[0]), int(d[1]), float(d[2])] for d in data]
        data = list(zip(*data))
        machine_plots[filename[:-4]] = data

# 3d plots lol
for key, value in machine_plots.items():
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_trisurf(value[0], value[1], value[2])
    ax.set_xlabel('max_iter')
    ax.set_ylabel('im_width')
    ax.set_zlabel('time')
    ax.set_title(f"{key}")
    plt.savefig(f"{key}-times.png")
    plt.close()

# Bar charts for total runtime
fig, ax = plt.subplots()
ax.bar(machine_plots.keys(), machine_plots.values())
plt.savefig(f"{key}-total-times.png")
plt.close()
