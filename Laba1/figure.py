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
        rotation_matrix = [
            [m.cos(angle) + m.pow(x, x)*(1 - m.cos(angle)), (1 - m.cos(angle))*x*y - z*m.sin(angle), x*z*(1-m.cos(angle)) + y*m.sin(angle)],
            [(1-m.cos(angle))*x*y + m.sin(angle)*z, m.cos(angle) + m.pow(y, y)*(1 - m.cos(angle)), y*z*(1-m.cos(angle)) - x*m.sin(angle)],
            [(1-m.cos(angle))*x*z - m.sin(angle)*y, (1 - m.cos(angle))*z*y - x*m.sin(angle), m.cos(angle) + m.pow(z, z)*(1 - m.cos(angle))]
        ]

        new_points = list()

        for point in self.points:
            new_points.append(self.multiplication(rotation_matrix, point))

        self.points = new_points

    @staticmethod
    def get_vector(axis: List[List[float]]):
        vector = list()
        for i in range(3):
            vector.append(axis[0][i] - axis[1][i])
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
