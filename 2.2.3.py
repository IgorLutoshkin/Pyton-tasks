import numpy as np
import matplotlib.pyplot as plt

def f(x):
    x = np.radians(x)
    return np.exp(np.cos(x)) + np.log(np.sin(0.8 * x) ** 2 + 1) * np.cos(x)

def y(x):
    x = np.radians(x)
    return -np.log((np.cos(x) + np.sin(x)) ** 2 + 1.7) + 2

x1, x2 = -240, 360
xsticks = np.arange(x1 - 10, x2, 50)
xsticks[0], xsticks[-1] = x1, x2
xsticks = sorted(np.append(xsticks, 71))
x = np.linspace(x1, x2, 10000)

print(f"В точке x = 71о значения функции: f(x) {['=','>','<'][int(np.sign(f(71)-y(71)))]} y(x)")
print(f"На интервале [{x1}, {x2}] мин.значение у функции: {['','y(x)','f(x)'][int(np.sign(min(f(x))-min(y(x))))]}")
print(f"На интервале [{x1}, {x2}] только отрицательные значения у функции: {['f(x)' if all(f(x)<0) else 'y(x)' if all(y(x)<0) else 'нет']}")
print(f"На интервале [{x1}, {x2}] функции f(x) и y(x) имеют точек пересечений: {len(np.argwhere(np.diff(np.sign(f(x) - y(x)))))}")

# отображаем графики
fig, ax = plt.subplots(figsize=(12, 6))
plt.title("Графики функций")
plt.plot(x, f(x), label='f(x)')
plt.plot(x, y(x), label='y(x)')
ax.axhline(y=0, color='k', lw=1)
ax.axvline(x=71, color='g', lw=1)
ax.set_xticks(xsticks)
plt.legend()
plt.grid()
plt.show()