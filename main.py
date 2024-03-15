import numpy as np
import matplotlib.pyplot as plt


def f(x: float) -> float:
    return np.sin(x) * np.sqrt(x)


def print_square(x: float, a: float, b: float):
    if a > 0:
        x1, y1 = [x, 0]
        x2, y2 = [x, a]

        x3, y3 = [x + b, 0]
        x4, y4 = [x + b, a]
    else:
        x1, y1 = [x, a]
        x2, y2 = [x, 0]

        x3, y3 = [x + b, a]
        x4, y4 = [x + b, 0]

    # вертикальные прямые прямоугольника
    plt.plot([x1, x2], [y1, y2], color="grey")
    plt.plot([x3, x4], [y3, y4], color="grey")

    # горизонтальные прямые прямоугольника
    plt.plot([x1, x3], [y1, y3], color="grey")
    plt.plot([x2, x4], [y2, y4], color="grey")

    # заливка
    plt.fill_between([x1, x3], 0, a, color="grey", alpha=0.5)


def main():
    n = 200
    a = 0
    b = 10

    s = 0
    x_shift: float = (b - a) / n
    x_current: float = a + ((b - a) / n)
    x_last: float = a

    for i in range(n):
        height = f(x_current)
        weight = x_current - x_last

        square = height * weight
        if square < 0:
            square *= -1

        s += square

        print_square(x_last, height, weight)

        x_last = x_current
        x_current += x_shift

    axis_length = b - a

    axis_x_min = int(a - (axis_length * 0.2))
    axis_x_max = int(b + (axis_length * 0.2))

    axis_x_length = axis_x_max - axis_x_min

    # определяем значения на оси x и вычисляем значение y = f(x)
    x_value = [x / 100.0 for x in range(int(a * 100), int(b * 100))]
    y_value = [f(x) for x in x_value]

    axis_y_min = np.floor(min(y_value))
    axis_y_max = np.ceil(max(y_value))

    axis_y_length = axis_y_max - axis_y_min

    # пишит площадь
    plt.text(axis_x_min + (axis_x_max - axis_x_min) * 0.001, axis_y_min + (axis_y_max - axis_y_min) * 0.8,
             f"S: {s:.3f} \nN: {n}",
             fontsize=16)

    # рисуем график
    plt.plot(x_value, y_value, color="black")

    # пределы интегрирования
    plt.axvline(a, 0, linestyle="-", color="blue")
    plt.axvline(b, 0, linestyle="-", color="blue")

    # оси координат
    plt.axhline(0, linestyle="--", color="black")
    plt.axvline(0, linestyle="--", color="black")

    # сетка
    plt.grid(True, color="black", alpha=0.15)

    # границы графика
    border_gain_1 = 0.05
    border_gain_2 = 0.002

    x_left_border = axis_x_min - axis_x_length * border_gain_1 if axis_x_min < 0 else 0 - axis_x_length * border_gain_2
    x_right_border = axis_x_max + axis_x_length * border_gain_1 if axis_x_max > 0 else 0 + axis_x_length * border_gain_2

    y_back_border = axis_y_min - axis_y_length * border_gain_1 if axis_y_min < 0 else 0 - axis_y_length * border_gain_2
    y_top_border = axis_y_max + axis_y_length * border_gain_1 if axis_y_max > 0 else 0 + axis_y_length * border_gain_2

    # плотность сетки
    plt.xticks(range(int(x_left_border), int(x_right_border), 1), fontsize="9")
    plt.yticks(range(int(y_back_border), int(y_top_border)), fontsize="9")

    # диапазон значений
    plt.xlim(x_left_border, x_right_border)
    plt.ylim(y_back_border, y_top_border)

    plt.show()


main()
