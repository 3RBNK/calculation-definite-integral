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
    plt.plot([x1, x2], [y1, y2], color="black")
    plt.plot([x3, x4], [y3, y4], color="black")

    # горизонтальные прямые прямоугольника
    plt.plot([x1, x3], [y1, y3], color="black")
    plt.plot([x2, x4], [y2, y4], color="black")


n = 10
a = -5
b = 1

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


axis_min: int = int(0.8 * a if a > 0 else 1.5 * a)
axis_max: int = int(1.2 * b if b > 0 else 0.8 * b)

print(f"min: {axis_min}, max: {axis_max}")


# определяем значения на оси x и вычисляем значение y = f(x)
x_value = [x / 100.0 for x in range(axis_min * 100, axis_max * 100)]
y_value = [f(x) for x in x_value]


# пишет площадь
plt.text(axis_min + (axis_max - axis_min) * 0.001, axis_min + (axis_max - axis_min) * 0.99, f"S: {s:.3f} \nN: {n}", fontsize=16)

# рисуем график
plt.plot(x_value, y_value, color="red")

# пределы интегрирования
plt.axvline(a, 0, linestyle="-", color="blue")
plt.axvline(b, 0, linestyle="-", color="blue")

# оси координат
plt.axhline(0, linestyle="--", color="black")
plt.axvline(0, linestyle="--", color="black")

# сетка
plt.grid(True)

# плотность сетки
shift_to_print = (axis_max - axis_min) * (1.0 / 5.0)

plt.xticks(range(int(axis_min - shift_to_print), int(axis_max + shift_to_print)))
plt.yticks(range(int(axis_min - shift_to_print), int(axis_max + shift_to_print)))

# диапазон значений
plt.xlim(axis_min - shift_to_print, axis_max + shift_to_print)
plt.ylim(axis_min - shift_to_print, axis_max + shift_to_print)

plt.show()
