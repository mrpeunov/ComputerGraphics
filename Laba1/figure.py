from random import random
from typing import List, Any
import numpy as np
import matplotlib.pyplot as plt
import math as m


class Figure:
    figure: Any
    points: List[List[float]]

    def __init__(self, count_points):
        self.points = list()
        self.points_generate(count_points)
        self.draw_figure()

    def draw_figure(self):
        plt.close()
        self.figure = plt.figure()
        ax = self.figure.add_subplot(111, projection='3d')

        x = list()
        y = list()
        z = list()

        for point in range(4):
            x += self.get_list_axis(number_axis=0, without_points_number=point)
            y += self.get_list_axis(number_axis=1, without_points_number=point)
            z += self.get_list_axis(number_axis=2, without_points_number=point)

        ax.plot_wireframe(np.array(x), np.array(y), np.array(z))
        # ax.legend()
        plt.xlim(-20, 20)
        plt.ylim(-20, 20)
        ax.set_zlim(-20, 20)

    def points_generate(self, count_points):
        for i in range(count_points):
            x = random() * 10
            y = random() * 10
            z = random() * 10
            point = [x, y, z]
            self.points.append(point)

    def get_list_axis(self, number_axis, without_points_number):
        axis = list()
        for i in range(4):
            if i != without_points_number:
                number = self.points[i][number_axis]
                axis.append([number, number])

        axis.append(axis[0])
        return axis

    def get_figure(self):
        return self.figure

    def turn(self, angle: int, axis: List[List[float]]):
        axis = self.get_vector(axis)
        x = axis[0]
        y = axis[1]
        z = axis[2]

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
            new_points.append(self.multiplication(rotation_matrix, point))

        self.points = new_points

    @staticmethod
    def get_vector(axis: List[List[float]]):
        # найдем вектор
        vector = list()
        for i in range(3):
            vector.append(axis[1][i] - axis[0][i])

        # найдём норму вектора
        norm = 0
        for item in vector:
            norm += m.pow(m.fabs(item), 2)
        norm = m.sqrt(norm)

        # отнормируем
        for i in range(len(vector)):
            vector[i] = vector[i]/norm
        return vector

    @staticmethod
    def multiplication(matrix, vector):
        result_vector = list()
        for i in range(len(matrix)):
            sum = 0
            for j in range(len(vector)):
                sum += matrix[i][j] * vector[j]
            result_vector.append(sum)
        return result_vector
