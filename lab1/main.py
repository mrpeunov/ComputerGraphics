"""
6 задание:

Поворот объемного тела относительно произвольной оси,
заданной в пространстве двумя точками, на заданный угол.
Необходимо предусмотреть возможность редактирования положения точек,
определяющих положение оси

Реализуем так:

Слева 80% окна - рабочая область, куда вставим matplotlib,
Справа 20% управление
"""

from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
import random


title = "1 лаба. 6 задание"
resolution = (1000, 600)
workspace = 0.75


class App(Tk):
    def __init__(self, parent=None):
        Tk.__init__(self, parent)
        self.parent = parent
        self._init_window()
        self.create_figure()

    def _init_window(self):
        """
        экран делим на две части:
        75% области отображения
        25% области настроек
        """
        width = resolution[0]
        height = resolution[1]
        self.title(title)
        self.geometry("{}x{}".format(width, height))
        self.resizable(0, 0)
        self._init_field()
        self._init_settings()


        """
        # Создание кнопки
        button = tk.Button(self, text="Выйти", command=self.on_click)
        button.grid(row=1, column=0)

        # Создание двигалки
        self.mu = tk.DoubleVar()
        self.mu.set(5.0)
        slider_mu = tk.Scale(self,
                             from_=7, to=0, resolution=0.1,
                             label='mu', variable=self.mu,
                             command=self.on_change
                             )
        slider_mu.grid(row=0, column=0)

        # Создание втрой двигалки
        self.n = tk.IntVar()
        self.n.set(512)  # default value for parameter "n"
        slider_n = tk.Scale(self,
                            from_=512, to=2,
                            label='n', variable=self.n, command=self.on_change
                            )
        slider_n.grid(row=0, column=1)
        """

    def _init_field(self):
        """
        создаем основное поле для рисования на нём
        """
        self.field = Canvas(self, bg="white")
        self.field.place(relx=0, rely=0, relwidth=workspace, relheight=1)

    def _init_settings(self):
        """
        создаем поле настроек

        тут необходимо управлять:
        тип фигуры (всегда 4 точки, рандомные) - обновляется кнопкой новая фигура
        углом поворота
        точки основнойо си
        """
        self.settings = Frame(self)
        self.settings.place(relx=workspace, rely=0, relwidth=1-workspace, relheight=1)

        self.set_count_point = Frame(self.settings)
        self.set_angle = Frame(self.settings)
        self.set_axis = Frame(self.settings)

        label_count_point = Label(self.set_count_point, text="Количество точек")
        label_count_point.grid(column=0, row=0)

        scale_count_point = Scale(self.set_count_point, from_=4, to=10, orient=HORIZONTAL, command=self.change_point_count)
        scale_count_point.grid(column=1, row=0)

        label_angle = Label(self.set_angle, text="Угол")
        scale_angle = Scale(self.set_angle, from_=0, to=360, resolution=10, orient=HORIZONTAL, command=self.change_point_count)

        label_angle.grid(column=0, row=0)
        scale_angle.grid(column=1, row=0)

        self.set_count_point.grid(column=0, row=0)
        self.set_angle.grid(column=0, row=1)


    def change_point_count(self, count):
        self.count = count
        print(count)

    def create_figure(self):
        # часть мат плот либ
        """
        fig = Figure(figsize=(6, 4), dpi=96)
        ax = fig.add_subplot(111)
        x, y = self.data(self.n.get(), self.mu.get())
        self.line1, = ax.plot(x, y)
        self.graph = FigureCanvasTkAgg(fig, master=self)
        canvas = self.graph.get_tk_widget()
        canvas.grid(row=0, column=2)
        """
        fig = plt.figure()
        ax = plt.axes(projection="3d")
        z_line = np.linspace(0, 15, 1000)
        x_line = np.cos(z_line)
        print(x_line)
        y_line = np.sin(z_line)
        ax.plot3D(x_line, y_line, z_line, 'gray')
        z_points = 15 * np.random.random(100)
        x_points = np.cos(z_points) + 0.1 * np.random.randn(100)
        y_points = np.sin(z_points) + 0.1 * np.random.randn(100)
        ax.scatter3D(x_points, y_points, z_points, c=z_points, cmap='hsv')



        # plt.show()
        self.graph = FigureCanvasTkAgg(fig, master=self)
        canvas = self.graph.get_tk_widget()
        canvas.grid(row=0, column=2)

    def on_click(self):
        self.quit()

    def on_change(self, value):
        x, y = self.data(self.n.get(), self.mu.get())
        self.line1.set_data(x, y)  # update data
        self.graph.draw()

    def data(self, n, mu):
        lst_y = []
        for i in range(n):
            lst_y.append(mu * random.random())
        return range(n), lst_y


if __name__ == "__main__":
    app = App()
    app.mainloop()

