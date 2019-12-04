import matplotlib
from pylab import *

x_data = range(0, 7)
y_data = [5, 1, 2, 7, 8, 4, 5]
perf = 10

# plot(x_data, y_data)

title("Test")
bar(x_data, y_data)
# yticks(sort(y_data))
yticks([5])
xticks(x_data, ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"])

show()

matplotlib.get_backend()
close()
input()
