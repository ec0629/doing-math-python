import math


def calculate_y(x):
    n = math.sqrt(x+4) - 2
    d = x
    return n / d


x = []
y = []

for i in range(-100, 100):
    if i == 0:
        continue
    x.append(i / 100)

for x_val in x:
    y.append(calculate_y(x_val))

for i in range(0, len(x)):
    print('x: ' + str(x[i]) + ' y: ' + str(y[i]))
