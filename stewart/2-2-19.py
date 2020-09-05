def calculate_y(x):
    n = x**2 - (2*x)
    d = x**2 - x - 2
    return n / d


x = [2.5, 2.1, 2.05, 2.01, 2.005, 2.001, 1.999, 1.995, 1.99, 1.95, 1.9]
y = []

for x_val in x:
    y.append(calculate_y(x_val))

for i in range(0, len(x)):
    print('x: ' + str(x[i]) + ' y: ' + str(y[i]))
