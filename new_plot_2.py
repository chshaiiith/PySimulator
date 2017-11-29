import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

clear_bkgd = {'axes.facecolor':'none', 'figure.facecolor':'none'}
sns.set(style='ticks', context='notebook', palette="muted", rc=clear_bkgd)

x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

k = np.loadtxt("without_queueing_3_lambda")
d = np.sort(k)
t1 = []
for i in x:
    t1.append(np.percentile(d, i))
y = np.array(t1)

k1 = np.loadtxt("without_queueing_6_lambda")
d1 = np.sort(k1)
t2 = []
for i in x:
    t2.append(np.percentile(d1, i))
y1 = np.array(t2)

k2 = np.loadtxt("without_queueing_24_lambda")
d2 = np.sort(k2)
t3 = []
for i in x:
    t3.append(np.percentile(d2, i))
y2 = np.array(t3)

# k3 = np.loadtxt("result_sjf/without_queue_effect24_8_R")
# d3 = np.sort(k3)
# t4 = []
# for i in x:
#     t4.append(np.percentile(d3, i))
# y3 = np.array(t4)


# Number of intervals to display.
# Later calculations add 2 to this number to pad it to align with the reversed axis
num_intervals = 3
x_values = 1.0 - 1.0/10**np.arange(0,num_intervals+2)

# Start with hard-coded lengths for 0,90,99
# Rest of array generated to display correct number of decimal places as precision increases
lengths = [1,2,2] + [int(v)+1 for v in list(np.arange(3,num_intervals+2))]

# Build the label string by trimming on the calculated lengths and appending %
labels = [str(100*v)[0:l] + "%" for v,l in zip(x_values, lengths)]


fig, ax = plt.subplots(figsize=(8, 4))

ax.set_xscale('log')
plt.gca().invert_xaxis()
# Labels have to be reversed because axis is reversed
ax.xaxis.set_ticklabels( labels[::-1] )

ax.plot(y, [100.0 - v for v in x])
ax.plot(y, [100.0 - v for v in x])
ax.plot(y, [100.0 - v for v in x])
#ax.plot([100.0 - v for v in x], y3)

ax.grid(True, linewidth=0.5, zorder=5)
ax.grid(True, which='minor', linewidth=0.5, linestyle=':')

ax.set_ylabel("Percentile")
ax.set_xlabel("request service time (without queueing)")

sns.despine(fig=fig)
plt.tight_layout()
plt.legend(['(3,1)', '(6,2)', '(24,8)'], loc='upper left')

plt.savefig("new_graph_1.png", dpi=300, format='png')