import matplotlib
from pylab import *

x_data = range(0, 7)
y_data = [1, 2, 3, 4, 5, 6, 7]
perf = 10

# plot(x_data, y_data)

title("Test")
bar(x_data, y_data)
yticks(y_data, ['a', 'b', 'c', 'd'])

show()

matplotlib.get_backend()
close()
input()
