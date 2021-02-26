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

from Tools.scripts.make_ctype import method
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
import random

title = "1 лаба. 6 задание"
resolution = (1000, 600)
workspace = 0.75


class App(Tk):
    count: int  # количество точек
    field: Canvas  # место отображения действий
    settings: Frame  # найстройки

    def __init__(self):
        Tk.__init__(self)

        self._init_window()  # инициализация основного окна

        # установим дефолтные значения
        self.count = 4

        # создадим фигуру
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

    def _init_field(self):
        """
        создаем основное поле для рисования на нём
        """
        self.field = Canvas(self, bg="white")

        # установка окна для ресования
        self.field.place(relx=0, rely=0, relwidth=workspace, relheight=1)

    def _init_settings(self):
        """
        создаем поля настроек
        """
        self.settings = Frame(self)

        # установка местоположения окна настроек
        self.settings.place(relx=workspace, rely=0, relwidth=1 - workspace, relheight=1)

        # Две кнопки: обновить фигуру и повернуть
        self._init_one_column()

        # Две шкалы: количество точек от 4 до 10 и угол поворота от 0 до 360
        self._init_double_column()

        # Поля для ввода точек оси
        self._init_three_column()

    def _init_one_column(self):
        one_column = Frame(self.settings)

        self.create_button_field(frame=one_column, text="Создать новую фигуру", row=0, command=self.create_new_figure)
        self.create_button_field(frame=one_column, text="Повернуть фигуру", row=1, command=self.turn_figure)

        one_column.grid(column=0, row=1, padx=10)

    def _init_double_column(self):
        double_column = Frame(self.settings)

        self.create_scale_field(frame=double_column,
                                text="Количество точек",
                                row=0,
                                start=4,
                                finish=10,
                                step=1,
                                command=self.change_point_count)

        self.create_scale_field(frame=double_column,
                                text="Угол",
                                row=1,
                                start=10,
                                finish=360,
                                step=5,
                                command=self.change_point_count)

        double_column.grid(column=0, row=0, padx=10)

    def _init_three_column(self):
        three_column = Frame(self.settings)

        for i in range(6):
            self.create_point_field(frame=three_column,
                                    row=i // 3,
                                    column=i % 3,
                                    default=i // 3)

        three_column.grid(column=0, row=3, padx=10)

    @staticmethod
    def create_button_field(frame: Frame, text: str, row: int, command: method):
        button = Button(frame, text=text, command=command)
        button.grid(row=row, column=0, padx=5, pady=5)

    @staticmethod
    def create_scale_field(frame: Frame, text: str, row: int, start: int, finish: int, step: int, command: method):
        """создаёт надпись и scale поле"""
        print(type(command))
        label = Label(frame,
                      text=text)

        scale = Scale(frame,
                      from_=start,
                      to=finish,
                      resolution=step,
                      orient=HORIZONTAL,
                      command=command)

        label.grid(column=0, row=row)
        scale.grid(column=1, row=row)

    @staticmethod
    def create_point_field(frame: Frame, row: int, column: int, default: int):
        entry = Entry(frame, width=10)
        entry.insert(0, default)
        entry.grid(row=row, column=column, padx=5, pady=5)

    # далее обработки кнопок

    def change_point_count(self, count):
        """произошло изменение количества точек"""
        self.count = count
        self.create_new_figure()

    def update_figure(self):
        """обновить текущую фигуру"""
        # перерисовываем фигуру по точкам
        print(self.count)
        print("Доделать")

    def turn_figure(self):
        """повернуть текущую фигуру"""
        # turn
        print("Доделать")
        self.update_figure()

    def create_new_figure(self):
        """создадим новую фигуру"""
        # создаём фигуру
        print("Доделать")
        self.update_figure()

    # дальше не разобранная хуета

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
