from abc import ABC, abstractmethod

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


class Function(ABC):
    @abstractmethod
    def function(self, x, y):
        pass

    def draw_plot(self, x_limits, y_limits):
        # 3D plot settings
        fig = plt.figure(figsize=[15, 10])
        ax = fig.add_subplot(projection='3d')

        # Setting view angle
        ax.view_init(45, 30)

        # Creating data for plot
        x = np.arange(x_limits[0], x_limits[1], 0.1)
        y = np.arange(y_limits[0], y_limits[1], 0.1)
        x, y = np.meshgrid(x, y)
        z = self.function(x, y)

        # Drawing surf
        surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm)
        plt.show()
