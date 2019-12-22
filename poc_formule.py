#import math
import copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits import mplot3d


def data(i, ax, X, Y, Z, surface):
    print("i=", i)
    Z.append(X * 0)
    for j in range(len(Z[i])):
        for k in range(len(Z[i][j])):
            Z[i][j][k] = 1 if j in range (8, 12) and k in range(8, 12) else Z[i][j][k]
    for j in range(1, 18): # I don't manage the edge evolution
        for k in range(1, 18): # I don't manage the edge evolution
            Z[i + 1][j][k] = (Z[i][j + 1][k] +Z[i][j - 1][k] + Z[i][j][k + 1] + Z[i][j][k - 1]) / 4 
    ax.clear()
    ax.set_zlim(0, 1)
    surface = ax.plot_surface(X, Y, Z[i], rstride=1, cstride=1,
        cmap='viridis', edgecolor='none')
    return(surface)

def main():
    x = np.linspace(-10, 10, 20)
    y = np.linspace(-10, 10, 20)
    X, Y = np.meshgrid(x, y)
    Z = []
    Z.append(X * 0) 
    for j in range(len(Z[0])):
        for k in range(len(Z[0][j])):
            Z[0][j][k] = 1 if j in range (8, 12) and k in range(8, 12) else 0

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_zlim(0, 1)
    surface = ax.plot_surface(X, Y, Z[0], rstride=1, cstride=1,
        cmap='viridis', edgecolor='none')
    ani = animation.FuncAnimation(fig, data, fargs=(ax, X, Y, Z, surface), interval=10, blit=False)

    ax.view_init(30, 45)

    plt.show()

if __name__ == "__main__":
    main()