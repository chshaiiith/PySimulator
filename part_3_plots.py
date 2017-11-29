import numpy as np


x_axis = []
y_axis = []
x1 = []
x2 = []


file_names = ["11", "21", "41", "81", "121", "141", "161"]
x_axiz = [1,2,4,8,12,14,16]

file_data = ["3","6","24", "48"]


for d1 in file_data:

    for f1 in file_names:
        k = np.loadtxt(d1 + "_" + f1)
        d = np.sort(k)

        np.percentile(d, 90)


for i in range(1, 100):
    x_axis.append(np.percentile(d, i))
    y_axis.append((i*1.0)/100)


for i in range(1, 100):
    x1.append(np.percentile(d1, i))
    x2.append((i*1.0)/100)

plt.plot(x_axis, y_axis)
plt.plot(x1, y_axis)
plt.show()