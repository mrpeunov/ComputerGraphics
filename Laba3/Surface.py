from typing import List, Any
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math as m

from Laba3.Point import Point
import numpy as np


def calc(p1, p2, p3, p4, u, w):
    return p1 * (1 - w) * (1 - u) + \
           p2 * (1 - u) * w + \
           p3 * u * (1 - w) + \
           p4 * u * w


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
        """
        x = np.linspace(min_x, max_x, n)
        y = np.linspace(min_y, max_y, n)
        x_list, y_list = np.meshgrid(x, y)
        """

        x_list, y_list, z_list = self.calculate_z_list()

        fig = plt.figure()

        ax = Axes3D(fig)
        ax.plot_wireframe(x_list, y_list, z_list)

        self.figure = fig

        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        ax.set_zlim(-10, 10)

        # ось X
        plt.plot([-10, 10], [0, 0], [0, 0], color='b')

        # ось Y
        plt.plot([0, -0], [-10, 10], [0, 0], color='b')

        # ось Y
        plt.plot([0, -0], [0, 0], [-10, 10], color='b')

        plt.xlabel("Ось X")
        plt.ylabel("Ось Y")
        ax.set_zlabel("Ось Z")

    def calculate_z_list(self):
        list_wu = np.linspace(0, 1, 20)

        x_list = list()
        y_list = list()
        z_list = list()

        for w in list_wu:
            x_line = list()
            y_line = list()
            z_line = list()

            for u in list_wu:
                x = calc(self.points[0].x, self.points[1].x, self.points[2].x, self.points[3].x, u, w)
                y = calc(self.points[0].y, self.points[1].y, self.points[2].y, self.points[3].y, u, w)
                z = calc(self.points[0].z, self.points[1].z, self.points[2].z, self.points[3].z, u, w)

                x_line.append(x)
                y_line.append(y)
                z_line.append(z)

            x_list.append(x_line)
            y_list.append(y_line)
            z_list.append(z_line)

        x_list = np.array(x_list)
        y_list = np.array(y_list)
        z_list = np.array(z_list)
        return x_list, y_list, z_list

    def turn_x(self):
        angle = 10
        x, y, z = 1, 0, 0
        self.turn(angle, x, y, z)

    def turn_y(self):
        angle = 10
        x, y, z = 0, 1, 0
        self.turn(angle, x, y, z)

    def turn(self, angle, x, y, z):
        cos = m.cos(m.radians(angle))
        sin = m.sin(m.radians(angle))

        a11 = cos + m.pow(x, 2) * (1 - cos)
        a12 = (1 - cos) * x * y - z * sin
        a13 = x * z * (1 - cos) + y * sin
        a21 = (1 - cos) * x * y + sin * z
        a22 = cos + m.pow(y, 2) * (1 - cos)
        a23 = y * z * (1 - cos) - x * sin
        a31 = (1 - cos) * x * z - sin * y
        a32 = (1 - cos) * z * y + x * sin
        a33 = cos + m.pow(z, 2) * (1 - cos)

        rotation_matrix = [[a11, a12, a13],
                           [a21, a22, a23],
                           [a31, a32, a33]]

        new_points = list()

        for point in self.points:
            vector = [point.x, point.y, point.z]
            mul_res = self.multiplication(rotation_matrix, vector)

            new_point = Point()
            new_point.x = mul_res[0]
            new_point.y = mul_res[1]
            new_point.z = mul_res[2]

            new_points.append(new_point)

        self.points = new_points

    @staticmethod
    def multiplication(matrix, vector):
        result_vector = list()
        for i in range(len(matrix)):
            sum = 0
            for j in range(len(vector)):
                sum += matrix[i][j] * vector[j]
            result_vector.append(sum)
        return result_vector
