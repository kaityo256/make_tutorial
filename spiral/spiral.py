try:
    import matplotlib
    matplotlib.use('Agg')
finally:
    import matplotlib.pyplot as plt


from math import atan2, pi, sin, sqrt

import numpy as np

L = 32


def get_data(step):
    data = np.zeros((L, L))
    for ix in range(L):
        for iy in range(L):
            x = ix - L/2
            y = iy - L/2
            phase = atan2(y, x)
            r = sqrt(x**2 + y**2)
            data[ix][iy] = sin(r+phase+step)
    return data


plt.tick_params(labelbottom=False,
                labelleft=False,
                labelright=False,
                labeltop=False)

plt.tick_params(bottom=False,
                left=False,
                right=False,
                top=False)

N = 16
for i in range(N):
    filename = f"fig{i:02d}.png"
    print(filename)
    plt.imshow(get_data(2.0*pi*i/N))
    plt.savefig(filename)
