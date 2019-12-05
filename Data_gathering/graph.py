from matplotlib import pyplot as plt
from pylab import *

x_data = range(0, 7)
y_data = [5, 1, 2, 7, 8, 4, 5]
perf = 10

# plot(x_data, y_data)

fig = plt.bar(x_data, y_data)
plt.savefig("ggg.png")

# plt.title("Test")
# bar(x_data, y_data)
# yticks(sort(y_data))
# plt.yticks([5])
# plt.xticks(x_data, ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"])

# plt.show()

# fig = plt.gcf()
# fig.savefig("image.png")
# close()
