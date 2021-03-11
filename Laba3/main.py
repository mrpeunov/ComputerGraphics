# Сформировать билинейную поверхность на основе
# произвольного задания ее четерех угловых точек.
# Обеспечить ее поворот относительно осей X и Y

from tkinter import *
from typing import List
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Laba3.Point import Point
from Laba3.Surface import Surface

title = "3 лаба. 1 задание"
resolution = (1000, 600)
workspace = 0.75


# time = 20


class App(Tk):
    count: int  # количество точек
    field: Canvas  # место отображения действий
    settings: Frame  # найстройки
    points: List[Point]  # точки поверхность
    surface: Surface  # фигура
    entries: List[Entry]
    angle: int  # угол

    def __init__(self):
        Tk.__init__(self)

        self._init_window()  # инициализация основного окна
        self.create_figure()  # создание фигуры

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

        # Две кнопки: повернуть вокруг x и повернуть вокруг y
        self._init_one_column()

        # Поля для ввода точек поверхности
        self._init_three_column()

    def _init_one_column(self):
        one_column = Frame(self.settings)

        self.create_button_field(frame=one_column, text="Сформировать поверхность", row=0, command=self.create_figure)
        self.create_button_field(frame=one_column, text="Повернуть вокруг оси X", row=1, command=self.turn_figure_x)
        self.create_button_field(frame=one_column, text="Повернуть вокруг оси Y", row=2, command=self.turn_figure_y)

        one_column.grid(column=0, row=1, padx=10)

    def _init_three_column(self):
        three_column = Frame(self.settings)

        self.entries = list()

        for i in range(12):
            self.entries.append(self.create_point_field(frame=three_column,
                                                        row=i // 3,
                                                        column=i % 3,
                                                        default=i // 3))

        three_column.grid(column=0, row=3, padx=10)

    @staticmethod
    def create_button_field(frame: Frame, text: str, row: int, command):
        button = Button(frame, text=text, command=command)
        button.grid(row=row, column=0, padx=5, pady=5)

    @staticmethod
    def create_point_field(frame: Frame, row: int, column: int, default: int) -> Entry:
        entry = Entry(frame, width=10)
        entry.insert(0, default)
        entry.grid(row=row, column=column, padx=5, pady=5)
        return entry

    def entries_to_points(self):
        """Получить сведения из точек"""
        self.points = list()
        for i in range(4):
            point = Point()
            point.x = float(self.entries[i*3+0].get())
            point.y = float(self.entries[i*3+1].get())
            point.z = float(self.entries[i*3+2].get())
            self.points.append(point)

    # далее обработки кнопок

    def draw_figure(self):
        """рисуем фигуру"""
        self.surface.draw_figure()
        canvas = FigureCanvasTkAgg(self.surface.get_figure(), master=self).get_tk_widget()
        canvas.grid(row=0, column=0)

    def turn_figure_x(self):
        pass

    def turn_figure_y(self):
        pass

    def create_figure(self):
        """создадим новую фигуру"""
        self.entries_to_points()
        self.surface = Surface(self.points)  # создаём фигуру
        self.draw_figure()  # перерисовываем


if __name__ == "__main__":
    app = App()
    app.mainloop()
