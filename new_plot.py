import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot(fileName):
    clear_bkgd = {'axes.facecolor':'none', 'figure.facecolor':'none'}
    sns.set(style='ticks', context='notebook', palette="muted", rc=clear_bkgd)

    x = [30, 60, 80, 90, 95, 97, 98, 98.5, 98.9, 99.1, 99.2, 99.3, 99.4, 100]

    k = np.loadtxt("6_2_1_4_R")
    d = np.sort(k)
    t1 = []
    for i in x:
        t1.append(np.percentile(d, i))
    y = np.array(t1)

    print np.mean(d)
    print np.percentile(y , 99)
    print np.mean(d)
    print np.percentile(y , 99)

    k = np.loadtxt("6_2_1_4_R")
    d = np.sort(k)





    # k3 = np.loadtxt("results/24_8_l_W")
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

    ax.plot([100.0 - v for v in x], y)
    # ax.plot([100.0 - v for v in x], y1)
    # ax.plot([100.0 - v for v in x], y2)
    #ax.plot([100.0 - v for v in x], y3)

    ax.grid(True, linewidth=0.5, zorder=5)
    ax.grid(True, which='minor', linewidth=0.5, linestyle=':')

    ax.set_xlabel("Percentile")
    ax.set_ylabel("request service time")

    sns.despine(fig=fig)
    plt.tight_layout()
#    plt.legend(['(3,1)', '(6,2)', '(12,4)', '(24,8)'], loc='upper left')

    plt.savefig("test.png", dpi=300, format='png')