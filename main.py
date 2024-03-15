import math as mt
import matplotlib.pyplot as plt


def f(x: float) -> float:
    return x * mt.sin(x / 6.0) + 2


def print_square(x: float, a: float, b: float):
    x1, y1 = [x, 0]
    x2, y2 = [x, a]

    x3, y3 = [x + b, 0]
    x4, y4 = [x + b, a]

    # вертикальные прямые прямоугольника
    plt.plot([x1, x2], [y1, y2], color="grey")
    plt.plot([x3, x4], [y3, y4], color="grey")

    # горизонтальные прямые прямоугольника
    plt.plot([x1, x3], [y1, y3], color="grey")
    plt.plot([x2, x4], [y2, y4], color="grey")

    #заливка
    plt.fill_between([x1, x3], 0, a, color="grey", alpha=0.5)


def main():
    n = 16
    a = -10
    b = 19

    s = 0
    x_shift: float = (b - a) / n
    x_current: float = a + ((b - a) / n)
    x_last: float = a

    for i in range(n):
        height = f(x_current)
        weight = x_current - x_last

        s += height * weight

        print_square(x_last, height, weight)

        x_last = x_current
        x_current += x_shift

    axis_length = b - a

    axis_x_min = int(a - (axis_length * 0.2))
    axis_x_max = int(b + (axis_length * 0.2))

    axis_x_length = axis_x_max - axis_x_min

    # определяем значения на оси x и вычисляем значение y = f(x)
    x_value = [x / 100.0 for x in range(a * 100, b * 100)]
    y_value = [f(x) for x in x_value]

    axis_y_min = mt.floor(min(y_value))
    axis_y_max = mt.ceil(max(y_value))

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
    plt.grid(True)

    # границы графика
    border_const_1 = 0.17
    border_const_2 = 0.05

    x_left_border = axis_x_min - axis_x_length * border_const_1 if axis_x_min < 0 else 0 - axis_x_length * border_const_2
    x_right_border = axis_x_max + axis_x_length * border_const_1 if axis_x_max > 0 else 0 + axis_x_length * border_const_2

    y_back_border = axis_y_min - axis_y_length * border_const_1 if axis_y_min < 0 else 0 - axis_y_length * border_const_2
    y_top_border = axis_y_max + axis_y_length * border_const_1 if axis_y_max > 0 else 0 + axis_y_length * border_const_2

    # плотность сетки
    plt.xticks(range(int(x_left_border), int(x_right_border)))
    plt.yticks(range(int(y_back_border), int(y_top_border)))

    # диапазон значений
    plt.xlim(x_left_border, x_right_border)
    plt.ylim(y_back_border, y_top_border)

    plt.show()


main()
