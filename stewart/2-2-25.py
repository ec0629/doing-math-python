import math


def calculate_y(x):
    n = math.pow(x, 6) - 1
    d = math.pow(x, 10) - 1
    return n / d


x = []
y = []

for i in range(900, 1100):
    x_val = i / 1000
    if x_val == 1:
        continue
    x.append(x_val)

for x_val in x:
    y.append(calculate_y(x_val))

for i in range(0, len(x)):
    print('x: ' + str(x[i]) + ' y: ' + str(y[i]))
