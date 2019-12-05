from matplotlib import pyplot as plt
from pylab import *
import time

y_data = [5, 1, 2, 7, 8, 4, 5]
perf = 10

wday = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thr', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
xtick = []
for i in range(7):
    t = time.localtime(time.time() - 86400 * (7 - i))
    xtick.append("%s\n%s" % ('%02d/%02d' % (t.tm_mon, t.tm_mday), wday[t.tm_wday]))

fig = plt.bar(range(0, 7), y_data)
plt.title("Last 7 days (h)")
plt.xticks(range(0, 7), xtick)
plt.yticks([5])
# yticks(sort(y_data))
plt.savefig("../Web/images/overview.png")
plt.show()
plt.close()

# TODO 수면 시간 미리 입력받아서 그 라인 쭉 그어주기
