# импортируем модуль numpy
import numpy as np
# cоздадим функцию для вычисления значений полинома второй степени в точке x
def get_trend(x, a):
    y = a[0] * x **2 + a[1]* x + a[2]
    return y

x_array= np.array(list(map(float, input().split()))) #координаты движения снаряда по оси OX (вещественные числа)
h_array= np.array(list(map(float, input().split()))) #координаты движения снаряда по оси OY (вещественные числа)
x_target = float(input()) #координаты мишени по оси ОХ
y_target = float(input()) #координаты мишени по оси ОY
a = np.polyfit(x_array, h_array, 2)

# высота на которой стоит пушка
h_zero = get_trend(0, a)

# высота снаряда в точке ОХ
h_target = get_trend(x_target, a)

# определим, попадет ли снаряд в цель, сравнив модуль разности с радиусом мишени
delta_h = abs(y_target - h_target)
if delta_h <= 0.5:
    print("h0 = %6.2f, yes" % h_zero)
else:
    print("h0 = %6.2f, no" % h_zero)

























