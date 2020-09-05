import matplotlib.pyplot as plt


def map_range_to_x(x):
    return x / 100


def calculate_y(x):
    if x < -1:
        return 1 + x
    elif x >= -1 and x < 1:
        return x * x
    else:
        return 2 - x


x = []
y = []
for i in range(-200, 200):
    x_val = i / 100
    x.append(x_val)

for x_val in x:
    y.append(calculate_y(x_val))

plt.plot(x, y, marker='o')
plt.show()
