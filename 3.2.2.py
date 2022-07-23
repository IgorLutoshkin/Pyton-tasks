import numpy as np

def polifit_1 (x,a):
    y1= a[0]*x+a[1]
    return y1
def polifit_2 (x,a):
    y2= a[0]*x**2+a[1]*x+ a[2]
    return y2

x_array = np.array(list(map(float, input().split())))
y_array = np.array(list(map(float, input().split())))

a1 = np.polyfit(x_array, y_array, 1)
a2 = np.polyfit(x_array, y_array, 2)

f1 = (polifit_1(x_array, a1))
f2 = (polifit_2(x_array, a2))

delta1 = np.abs((y_array - f1) / y_array) * 100
delta2 = np.abs((y_array - f2) / y_array) * 100

if delta1.mean() >= delta2.mean():
    print("%5.3f %5.3f %5.3f"% (a2[0],a2[1],a2[2]))
else:
    print("%5.3f %5.3f" % (a1[0],a1[1]))
