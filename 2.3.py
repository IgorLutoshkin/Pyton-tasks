import matplotlib.pyplot as plt

# формируем линию

line = plt.plot([1, 5, -3, -0.5], [1, 25, 9, 0.25 ])

# задаем формат ее вывода

plt.setp(line, color="red", linewidth=2, marker="o" )

# устанавливаем две оси в положение zero

plt.gca().spines["left"].set_position("zero")

plt.gca().spines["bottom"].set_position("zero")

# скрываем остальные две

plt.gca().spines["top"].set_visible(False)

plt.gca().spines["right"].set_visible(False)

# отображаем область построения

plt.show()