from math import atan2, pi, sin, sqrt

import numpy as np

L = 32


def get_data(step):
    data = np.zeros((L, L))
    for ix in range(L):
        for iy in range(L):
            x = ix - L / 2
            y = iy - L / 2
            phase = atan2(y, x)
            r = sqrt(x**2 + y**2)
            data[ix][iy] = sin(r + phase + step)
    return data


N = 16
for i in range(N):
    filename = f"spiral{i:02d}.dat"
    d = get_data(2.0 * pi * i / N).reshape(L * L)
    text = "\n".join([str(v) for v in d])
    print(filename)
    with open(filename, "w") as f:
        f.write(text)
