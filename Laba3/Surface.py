from typing import List, Any
import matplotlib.pyplot as plt
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

        print(min_x, max_x, min_y, max_y)

        x_list = list()
        y_list = list()
        z_list = list()

        for i in range(1000):
            x_list.append(min_x + i * (max_x - min_x)/1000)
            y_list.append(min_y + i * (max_y - min_y)/1000)

        for w in x_list:
            zz = list()
            for u in y_list:
                z = self.calculate_z(w, u)
                zz.append(z)
            z_list.append(zz)

        x_list = np.array(x_list)
        y_list = np.array(y_list)
        z_list = np.array(z_list)

        ax = self.figure.add_subplot(111, projection='3d')
        ax.plot_surface(x_list, y_list, z_list, cmap='inferno')

        plt.xlim(-20, 20)
        plt.ylim(-20, 20)
        ax.set_zlim(-20, 20)

    def calculate_z(self, x, y):
        return 0
