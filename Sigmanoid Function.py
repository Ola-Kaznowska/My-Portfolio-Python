import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 1 / (1 + np.exp(x))

x = np.linspace(- 10, 10, 100)
x_values = f(x)

plt.figure(figsize = (8, 5))
plt.plot(x, x_values, color="orange")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Sigmanoid Function")
plt.grid()
plt.show()