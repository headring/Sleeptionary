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

plt.bar(xtick, y_data)
plt.title("Last 7 days (h)")
plt.yticks([1/6, 1/2], ["10min", "30min"])
# plt.savefig("../Web/images/overview.png")
plt.show()
plt.close()

xtick = []
seven_days_tm = []
seven_days_hd = []
c2 = c.execute('''SELECT Date, TM_avg, HD_avg FROM Sleeptionary ORDER BY Date DESC LIMIT 7''')
for s in c2:
    xtick.append(list(s)[0][5:])
    seven_days_tm.append(list(s)[1])
    seven_days_hd.append(list(s)[2])

# 최근 7일 간의 온도 그래프
plt.plot(xtick[::-1], seven_days_tm[::-1], marker="o", color="red")
plt.yticks([20, 23, 25, 28])
# plt.grid(True)
plt.title("Last 7 days' Average Temperature (Celsius)")
plt.savefig("../Web/images/overview_tm.png")
plt.show()
plt.close()

plt.plot(xtick[::-1], seven_days_hd[::-1], marker="o", color="blue")
plt.title("Last 7 days' Average Humidity (%)")
plt.savefig("../Web/images/overview_hd.png")
plt.show()
plt.close()