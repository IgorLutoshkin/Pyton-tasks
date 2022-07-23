import math

def f_x(x):
    try:
        y = 1 / (x+1) + x / (x-3)
    except:
        y= math.inf
    return y
t = float(input("t = "))

y = f_x(t)

print("f(%1.2f)=%6.2f" %(t,y))
