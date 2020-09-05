import math
import matplotlib.pyplot as plt


def calculate_y(x):
    d = 1 + math.pow(math.e, 1/x)
    return 1 / d


x = []
y = []
for i in range(-100, 100):
    if i == 0:
        continue
    x_val = i / 100
    x.append(x_val)

for x_val in x:
    y.append(calculate_y(x_val))

plt.plot(x, y, marker='o')
plt.show()
