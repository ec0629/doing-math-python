import math


def calculate_y(x):
    n = math.pow(math.e, 5*x) - 1
    d = x
    return n / d


x = [-0.5, -0.1, -0.01, -0.001, -0.0001, 0.0001, 0.001, 0.01, 0.1, 0.5]
y = []

for x_val in x:
    y.append(calculate_y(x_val))

for i in range(0, len(x)):
    print('x: ' + str(x[i]) + ' y: ' + str(y[i]))
