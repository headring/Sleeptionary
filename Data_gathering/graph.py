from matplotlib import pyplot as plt
from pylab import *
import time
import sqlite3

y_data = []
wday = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thr', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
xtick = []

# Connect database
db_path = "./test.db"
try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # c.execute("쿼리문")
except sqlite3.OperationalError:
    print("There is no database in path.")

sleep_times = []
c2 = c.execute('''SELECT Date, (julianday(end)-julianday(start))*24 FROM Sleeptionary ORDER BY Date DESC LIMIT 7''')
for s in c2:
    sleep_times.append(list(s))

sleep_times_index = len(sleep_times) - 1
for i in range(7):
    # x축 라벨 만들기 (최근 7일의 날짜와 요일)
    t = time.localtime(time.time() - 86400 * (7 - i))
    xtick.append("%s\n%s" % ('%02d/%02d' % (t.tm_mon, t.tm_mday), wday[t.tm_wday]))

    # y축에 들어갈 수면 시간
    if not sleep_times_index < 0:
        if sleep_times[sleep_times_index][0] == "%04d-%02d-%02d" % (t.tm_year, t.tm_mon, t.tm_mday):
            y_data.append(float(sleep_times[sleep_times_index][1]))
            sleep_times_index -= 1
        else:
            y_data.append(0)

plt.bar(range(0, 7), y_data)
plt.title("Last 7 days (h)")
plt.xticks(range(0, 7), xtick)
plt.yticks([5])
# yticks(sort(y_data))
plt.savefig("../Web/images/overview.png")
plt.show()
plt.close()

# TODO 수면 시간 미리 입력받아서 그 라인 쭉 그어주기
