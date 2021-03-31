from typing import List, Any
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

from Laba3.Point import Point
import numpy as np


class Surface:
    figure: Any
    points: List[Point]

    def __init__(self, points: List[Point]):
        if len(points) == 4:
            self.points = points
            self.draw_figure()
        else:
            pass

    def get_figure(self):
        return self.figure

    def draw_figure(self):
        plt.close()
        self.figure = plt.figure()
        n = 20  # количество точек

        # вычисляем минимальный - максимальные значения x, y
        min_x = self.points[0].x
        max_x = 0

        min_y = self.points[0].y
        max_y = 0

        for point in self.points:
            if point.x > max_x:
                max_x = point.x

            if point.x < min_x:
                min_x = point.x

            if point.y > max_y:
                max_y = point.y

            if point.y < min_y:
                min_y = point.y

        # создаем координаты по x и y
        x = np.linspace(min_x, max_x, n)
        y = np.linspace(min_y, max_y, n)
        x_list, y_list = np.meshgrid(x, y)

        # вычисляем z
        r = np.sqrt(x_list ** 2 + y_list ** 2)
        z = np.sin(r) / r

        z_list = self.calculate_z_list()

        fig = plt.figure()
        ax = Axes3D(fig)
        ax.plot_wireframe(x_list, y_list, z_list)
        self.figure = fig

        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        ax.set_zlim(-10, 10)

    def calculate_z_list(self):
        list_wu = np.linspace(0, 1, 20)

        x_list = list()
        y_list = list()
        z_list = list()

        for w in list_wu:
            z_line = list()
            for u in list_wu:
                z = self.points[0].z * (1 - w) * (1 - u) + \
                    self.points[1].z * (1 - u) * w + \
                    self.points[2].z * u * (1 - w) + \
                    self.points[3].z * u * w
                z_line.append(z)
            z_list.append(z_line)
            
        x_list = np.array(x_list)
        y_list = np.array(y_list)
        z_list = np.array(z_list)
        return x_list, y_list, z_list
