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
from asyncio import sleep
from tkinter import *
from typing import List

from Tools.scripts.make_ctype import method
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Laba1.figure import Figure


title = "1 лаба. 6 задание"
resolution = (1000, 600)
workspace = 0.75
time = 20


class App(Tk):
    count: int  # количество точек
    field: Canvas  # место отображения действий
    settings: Frame  # найстройки
    axis: List[List[float]]  # данные основной оси
    figure: Figure  # фигура
    entries: List[List[Entry]]
    angle: int  # угол

    def __init__(self):
        Tk.__init__(self)

        # установим дефолтные значения
        self.count = 4
        self.angle = 90

        self._init_window()  # инициализация основного окна
        self.create_new_figure()  # создание фигуры

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
                                text="Угол",
                                row=1,
                                start=10,
                                finish=360,
                                step=5,
                                com=self.change_angle)

        double_column.grid(column=0, row=0, padx=10)

    def _init_three_column(self):
        three_column = Frame(self.settings)

        self.entries = list()
        item = list()

        for i in range(6):
            item.append(self.create_point_field(frame=three_column,
                                                row=i // 3,
                                                column=i % 3,
                                                default=i // 3))
            if i == 2:
                self.entries.append(item)
                item = list()

        self.entries.append(item)

        three_column.grid(column=0, row=3, padx=10)

    @staticmethod
    def create_button_field(frame: Frame, text: str, row: int, command: method):
        button = Button(frame, text=text, command=command)
        button.grid(row=row, column=0, padx=5, pady=5)

    def create_scale_field(self, frame: Frame, text: str, row: int, start: int, finish: int, step: int, com: method):
        """создаёт надпись и scale поле"""
        label = Label(frame, text=text)

        scale = Scale(frame,
                      from_=start,
                      to=finish,
                      resolution=step,
                      orient=HORIZONTAL,
                      command=com)

        scale.set(self.angle)

        label.grid(column=0, row=row)
        scale.grid(column=1, row=row)

    @staticmethod
    def create_point_field(frame: Frame, row: int, column: int, default: int) -> Entry:
        entry = Entry(frame, width=10)
        entry.insert(0, default)
        entry.grid(row=row, column=column, padx=5, pady=5)
        return entry

    def entries_to_axis(self):
        self.axis = list()
        column = list()

        for i in range(6):
            column.append(float(self.entries[i // 3][i % 3].get()))

            if i == 2:
                self.axis.append(column)
                column = list()

        self.axis.append(column)

    # далее обработки кнопок

    def change_angle(self, angle):
        self.angle = int(angle)

    def draw_figure(self):
        """рисуем фигуру"""
        self.figure.draw_figure()
        canvas = FigureCanvasTkAgg(self.figure.get_figure(), master=self).get_tk_widget()
        canvas.grid(row=0, column=0)

    def turn_figure(self):
        """повернуть текущую фигуру"""
        self.entries_to_axis()
        self.figure.turn(self.angle, self.axis)
        self.draw_figure()

    def create_new_figure(self):
        """создадим новую фигуру"""
        self.figure = Figure(self.count)  # создаём фигуру
        self.draw_figure()  # перерисовываем


if __name__ == "__main__":
    app = App()
    app.mainloop()
