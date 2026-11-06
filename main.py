import numpy as np
import matplotlib.pyplot as plt

# Descenso de gradiente para f(x) = x**4 - 4*(x**2) + x
# Función de descenso: x0 = x0 - a*df(x0)

def f(x):
    return x**4 - 4*(x**2) + x

def df(x):
    return 4*x**3 - 8*x + 1

def gradient_descent(starting_point, learning_rate, iterations):
    x = starting_point
    for i in range(iterations):
        x = x -learning_rate*df(x)
        print(f'Iteration {i+1}, x = {x:.2f}, f(x) = {f(x):.2f}')
    return x

x_vals = np.linspace(-3, 3, 400)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label="f(x) = x^4 - 4(x^2) + x")

starting_points = [-2.5, 0, 2.5]
minimums = [gradient_descent(p, 0.1, 10) for p in starting_points]

global_minimum = min(minimums, key=f)
locales = [m for m in minimums if not np.isclose(m, global_minimum, atol=0.1)]

if locales:
    plt.scatter(locales, f(np.array(locales)), color="red", label="Mínimo local")

plt.scatter(global_minimum, f(global_minimum), color="green", s=100, zorder=3, label="Mínimo global")

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Descenso de graidente")
plt.legend()
plt.show()