import math
import copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits import mplot3d


def data(i, ax, X, Y, Z, V, surface):
    Z.append(X * 0)
    V.append(X * 0) 
    # center area where the water comes from
    for j in range(len(Z[i])):
        for k in range(len(Z[i][j])):
            if j == 0 or j == 19 or k == 0 or k == 19:
                Z[i][j][k] = 0
            elif j == 10 and k == 10:
                Z[i][j][k] = 1
            elif j == 15 and k == 10:
                Z[i][j][k] = 1 / 60
            elif j == 15 and k == 15:
                Z[i][j][k] = 4 / 6
    # water propagation formule 
    for j in range(20): 
        for k in range(20):
            # corner cases
            if j == 0 and k == 0:
                V[i + 1][j][k] = V[i][j][k] + (Z[i][j + 1][k] + Z[i][j][k + 1] + 2 * Z[i][j][k]) / 4 - Z[i][j][k]
            elif j == 0 and k == 19:
                V[i + 1][j][k] = V[i][j][k] + (Z[i][j + 1][k] + Z[i][j][k - 1] + 2 * Z[i][j][k]) / 4 - Z[i][j][k]
            elif j == 19 and k == 0:
                V[i + 1][j][k] = V[i][j][k] + (Z[i][j - 1][k] + Z[i][j][k + 1] + 2 * Z[i][j][k]) / 4 - Z[i][j][k]
            elif j == 19 and k == 19:
                V[i + 1][j][k] = V[i][j][k] + (Z[i][j - 1][k] + Z[i][j][k - 1] + 2 * Z[i][j][k]) / 4 - Z[i][j][k]
            # edge cases
            elif j == 0:
                V[i + 1][j][k] = V[i][j][k] + (Z[i][j + 1][k] + Z[i][j][k + 1] + Z[i][j][k - 1] + Z[i][j][k]) / 4 - Z[i][j][k]
            elif j == 19:
                V[i + 1][j][k] = V[i][j][k] + (Z[i][j - 1][k] + Z[i][j][k + 1] + Z[i][j][k - 1] + Z[i][j][k]) / 4 - Z[i][j][k]
            elif k == 0:
                V[i + 1][j][k] = V[i][j][k] + (Z[i][j + 1][k] + Z[i][j - 1][k] + Z[i][j][k + 1] + Z[i][j][k]) / 4 - Z[i][j][k]
            elif k == 19:
                V[i + 1][j][k] = V[i][j][k] + (Z[i][j + 1][k] + Z[i][j - 1][k] + Z[i][j][k - 1] + Z[i][j][k]) / 4 - Z[i][j][k]
            #general case
            else:
                V[i + 1][j][k] = V[i][j][k] + (Z[i][j + 1][k] + Z[i][j - 1][k] + Z[i][j][k + 1] + Z[i][j][k - 1]) / 4 - Z[i][j][k]
            V[i + 1][j][k] *= 0.1
            Z[i + 1][j][k] = Z[i][j][k] + V[i + 1][j][k]
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
    V = []
    V.append(X * 0) 
    #center area where the water comes from
    for j in range(len(Z[0])):
        for k in range(len(Z[0][j])):
            if j == 0 or j == 19 or k == 0 or k == 19:
                Z[0][j][k] = 0
            elif j == 10 and k == 10:
                Z[0][j][k] = 1
            elif j == 15 and k == 10:
                Z[0][j][k] = 1 / 60
            elif j == 15 and k == 15:
                Z[0][j][k] =  4 / 6
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_zlim(0, 1)
    surface = ax.plot_surface(X, Y, Z[0], rstride=1, cstride=1,
        cmap='viridis', edgecolor='none')
    ani = animation.FuncAnimation(fig, data, fargs=(ax, X, Y, Z, V, surface), interval=100, blit=False)

    ax.view_init(30, 45)

    plt.show()

if __name__ == "__main__":
    main()