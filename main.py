import math as mt
import numpy as np
import matplotlib.pyplot as plt


def f(x: float) -> float:
    return (x ** 0.5) * mt.sin(x / 6.0) + 5


def print_square(x: float, a: float, b: float):
    x1, y1 = [x, 0]
    x2, y2 = [x, a]

    x3, y3 = [x + b, 0]
    x4, y4 = [x + b, a]

    # вертикальные прямые прямоугольника
    plt.plot([x1, x2], [y1, y2], color="black")
    plt.plot([x3, x4], [y3, y4], color="black")


n = 5
a = 5
b = 10


s = 0
x_shift: float = (b - a) / n
x_current: float = a + ((b - a) / n)
x_last = a

for i in range(n):
    print(f"x last: {x_last} x current: {x_current}")

    height = f(x_current)
    print(f"height: {height}")
    weight = x_current - x_last

    s += height + weight

    print_square(x_last, height, weight)

    x_last = x_current
    x_current += x_shift

    print()


print(f"S: {s:.3f}")

# определяем значения на оси x и вычисляем значение y = f(x)
x_value = [x // 1000.0 for x in range(0, 12000)]
y_value = [f(x) for x in x_value]

# рисуем график
plt.plot(x_value, y_value, color="red")

# пределы интегрирования
plt.axvline(5, -1, 12, linestyle="-", color="blue")
plt.axvline(10, -1, 12, linestyle="-", color="blue")

# оси координат
plt.axhline(0, -1, 12, linestyle="--", color="black")
plt.axvline(0, -1, 12, linestyle="--", color="black")

# диапазон значений
plt.xlim(-1, 12)
plt.ylim(-1, 12)

plt.show()
