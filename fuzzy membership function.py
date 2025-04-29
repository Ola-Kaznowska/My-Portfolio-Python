import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 50, 500)


def warm(x):
    return np.maximum(np.minimum((x - 10) / 20, (40 - x) / 10), 0)


mi_warm = warm(x)


points_x = [10, 30, 40]
points_y = warm(np.array(points_x))
labels = ['a (10°C)', 'b (30°C)', 'c (40°C)']


plt.figure(figsize=(10, 5))
plt.plot(x, mi_warm, label="Warm", color="blue")
plt.scatter(points_x, points_y, label="Points", color="red")

plt.grid(True)
plt.legend()
plt.title("Membership Function")
plt.show()