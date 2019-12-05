from matplotlib import pyplot as plt
from pylab import *
import time

x_data = range(0, 7)
y_data = [5, 1, 2, 7, 8, 4, 5]
perf = 10

wday = {0:'월', 1:'화', 2:'수', 3:'목', 4:'금', 5:'토', 6:'일'}
t = time.localtime()
starttime = '%04d-%02d-%02d %02d:%02d:%02d' % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)

fig = plt.bar(x_data, y_data)
plt.title("Last 7 days (h)")
plt.xticks(x_data, ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"])
plt.yticks([5])
# yticks(sort(y_data))
plt.savefig("../Web/images/overview.png")
plt.show()
plt.close()
