"""Дан многоугольник на плоскости, заданный  координатами своих вершин.
 Найти координаты вершин многоугольника, полученные поворотом каждой точки 
 на заданный угол вокруг начала координат. Вычислить средние значения
 координат по оси ОХ и ОУ повернутого многоугольника.
 Входные данные:

 количество вершин многоугольника (целое число);
список вершин многоугольника, каждая вершина на отдельной строке, строка
 состоит из двух чисел через пробел, определяющие координаты вершины по
 оси ОХ и OY (целые числа);
угол поворота в градусах (целое число).
Выходные данные:

среднее значение абсцисс (координат x) и ординат(координат y) точек
 повернутого многоугольника."""
 
import numpy as np
from math import cos, sin, radians
n = int(input())
array_list = []
for i in range(n):
    line = input()
    array_str = line.split()
    array_list.append(array_str)
a = np.array(array_list, dtype= int)
#print (a)
u = radians(int(input()))
rotate = np.array ([[cos(u), sin(u)], [-sin(u), cos(u)]])
#print(rotate)
c = np.dot(a, rotate)
#print(c)
avg_x = np.mean(c[:,0],0)
avg_y = np.mean(c[:,1],0)
print("avg_x = %6.2f, avg_y = %6.2f" % (avg_x, avg_y ))
