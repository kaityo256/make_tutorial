try:
    import matplotlib
    matplotlib.use('Agg')
finally:
    import matplotlib.pyplot as plt

import sys
import os
import numpy as np

L = 32

plt.tick_params(labelbottom=False,
                labelleft=False,
                labelright=False,
                labeltop=False)

plt.tick_params(bottom=False,
                left=False,
                right=False,
                top=False)


def convert(filename):
    (file, _) = os.path.splitext(filename)
    pngfile = file + ".png"
    print(pngfile)
    d = []
    with open(filename) as lines:
        for line in lines:
            d.append(float(line))
    d = np.array(d).reshape(L, L)
    plt.imshow(d)
    plt.savefig(pngfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert.py data.dat")
    else:
        convert(sys.argv[1])
