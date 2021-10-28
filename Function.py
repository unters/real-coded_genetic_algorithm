from abc import ABC, abstractmethod

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


class Function(ABC):
    @abstractmethod
    def function(self, x, y):
        pass

    def draw_plot(self, points_1=None, points_2=None):
        # 3D plot settings
        fig = plt.figure(figsize=[15, 10])
        ax = fig.add_subplot(projection='3d')

        # Setting view angle
        ax.view_init(45, 30)
        ax.set_xlabel('x label')
        ax.set_ylabel('y label')
        ax.set_zlabel('z label')

        alpha = 1  # Surface transparency
        if points_1 is not None or points_2 is not None:
            alpha = 0.7

        # Creating data for plot
        x = np.arange(-4, 4, 0.1)
        y = np.arange(-4, 4, 0.1)
        x, y = np.meshgrid(x, y)
        z = self.function(x, y)

        # Drawing surf
        surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm, alpha=alpha)

        # Drawing points
        if points_1 is not None:
            xs1 = list()
            ys1 = list()
            zs1 = list()

            for point in points_1:
                xs1.append(round(point[0]))
                ys1.append(round(point[1]))
                zs1.append(self.function(xs1[-1], ys1[-1]))

            ax.scatter(xs1, ys1, zs1, s=32, c='r')

        # Drawing points
        if points_2 is not None:
            xs2 = list()
            ys2 = list()
            zs2 = list()

            for point in points_2:
                xs2.append(round(point[0]))
                ys2.append(round(point[1]))
                zs2.append(self.function(xs2[-1], ys2[-1]))

            ax.scatter(xs2, ys2, zs2, s=32, c='g')

        plt.show()

