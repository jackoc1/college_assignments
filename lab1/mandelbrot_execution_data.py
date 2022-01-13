""" Run in the directory you want to get the running time data from """
import os

data = []
for filename in os.listdir(os.getcwd()):
    if filename[-4:] == ".png":
        temp = filename.replace("iter:", ' ')
        temp = temp.replace("-width:", ' ')
        temp = temp.replace("-time:", ' ')
        temp = temp.replace(".png", ' ')
        temp = temp.strip()
        data.append(temp.split(' '))

headers = [["iter", "width", "time"]]
data = [[int(d[0]), int(d[1]), float(d[2])] for d in data]
data.sort()
data = headers + data

cwd = os.getcwd().split('/')[-1]
csv = open(f"{cwd}.csv", 'w')
for triplet in data:
    csv.write(f"{triplet[0]},{triplet[1]},{triplet[2]}\n")
csv.close()
