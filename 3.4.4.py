"""Трое сотрудников получили премию в размере 2970 р., причем второй 
получил 1/3 того, что получил первый, и еще 180 р., а третий
 получил 1/3 денег второго и еще 130 р. Какую премию получил каждый?

Входные данные: нет

Выходные данные:

три числа, размер премии, которую получил каждый сотрудник.
Система уравнений для составления матрицы:
x1 + x2 + x3 = 2970
-1/3 * x1 + x2 = 180
-1/3 * x2 + x3 = 130"""

import numpy as np
import numpy.linalg as alg
a = np.array([[1,1,1],[-1/3,1,0], [0,-1/3,1]])
b = np.array([2970, 180, 130])
x = np.dot(alg.inv(a), b) # умножаем обратную матрицу на вектор
print("%4.0f р., %4.0f р., %4.0f р."% (x[0], x[1], x[2]) )



