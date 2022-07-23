from math import atan, pi

def compute_population (t):
    
    population = (172/45) *( (pi/2) - atan((2000-t)/45))
    return population

a=int(input("a="))
b=int(input("b="))
n=int(input("n="))
h = (b-a)/(n-1)
import matplotlib.pyplot as plt
x_list= [a+h*i for i in range(n)]
f_list= [compute_population(x) for x in x_list]
line = plt.plot(x_list, f_list)

plt.setp(line, color="blue", linewidth=2)

plt.gca().spines["left"].set_position("center")

plt.gca().spines["bottom"].set_position("center")

plt.gca().spines["top"].set_visible("center")

plt.gca().spines["right"].set_visible("center")

plt.show()
