import matplotlib.pyplot as plt
import numpy as np

xpoints = np.arange(-3, 3, 1)
ypoints = -2 * xpoints + 5

xpoints = [-3, -1, 0, 1, 2, 3]

ypoints = [2*x  - 3 for x in xpoints]

plt.plot(xpoints, ypoints, c="r", marker="o", linestyle="--", label="-2 x + 5")
plt.grid()
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Hello Matplotlib")
plt.show()



x = np.random.rand(25)
y = np.random.rand(25)

plt.scatter(x, y)

plt.show()




rolls_count = []
dice_value = []
dice_rolls = np.array([np.random.randint(1, 7) for _ in range(20)])
print(dice_rolls)

for i in set(dice_rolls):
    dice_value.append(i)
    rolls_count.append(len(np.where(dice_rolls == i)[0]))
plt.bar(dice_value, rolls_count)

print(rolls_count)
print(dice_value)

plt.show()