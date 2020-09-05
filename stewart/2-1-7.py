import matplotlib.pyplot as plt


def create_graph():
    x_numbers = [0, 1, 2, 3, 4, 5]
    y_numbers = [0, 1.4, 5.1, 10.7, 17.7, 25.8]
    plt.plot(x_numbers, y_numbers)
    plt.show()


if __name__ == '__main__':
    create_graph()
