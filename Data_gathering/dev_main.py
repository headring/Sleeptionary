import sqlite3
import time
import Adafruit_DHT
from matplotlib import pyplot as plt
from pylab import *
from Adafruit_AMG88xx import Adafruit_AMG88xx
import RPi.GPIO as GPIO
import subprocess
from math import exp


def db_insert(li, qr):
    value = tuple(li)
    rm = c.execute(qr, value)
    conn.commit()
    print("Data inserted.")


def tmhd():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print("Temp = %.1f'C    Humidity = %.1f%%" % (temperature, humidity))
    else:
        print('Failed to get reading. Try again!')

    query = '''INSERT INTO tmhd(TM, HD) VALUES(?,?)'''

    return [[temperature, humidity], query]


def lux():
    count = 0

    # Output on the pin for
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    # Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)

    # Count until the pin goes high
    while GPIO.input(pin_to_circuit) == GPIO.LOW:
        count += 1

    # Convert to lux
    lx = 1285.5 * exp(-0.009 * count)  # 조도값
    print("%.0flux" % lx)
    query = '''INSERT INTO lux(LX) VALUES(?)'''

    return [[lx], query]


# Connect database
db_path = "./test.db"
try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    print("DB connected.")
except sqlite3.OperationalError:
    print("There is no database in path.")

# Initialize DHT sensor
sensor = Adafruit_DHT.DHT11
pin = 4
tmhd()  # Trash dummy values
print("Thermometer initialized.")

# Initialize lux sensor
GPIO.setmode(GPIO.BOARD)
pin_to_circuit = 8
print("Photo sensor initialized.")

# Initialize thermal camera
camera = Adafruit_AMG88xx()
print("Thermal camera initialized.")

# Initialize button
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
print("Buttons initialized.")

# Initialize mic
GPIO.setmode(GPIO.BOARD)
soundpin = 12
GPIO.setup(soundpin, GPIO.IN)

# Standard time
standard_time = time.time()
t1 = time.localtime(standard_time)
started = True  # Sleep started
starttime = '%04d-%02d-%02d %02d:%02d:%02d' % (t1.tm_year, t1.tm_mon, t1.tm_mday, t1.tm_hour, t1.tm_min, t1.tm_sec)
ts = []  # Save temperatures
got_avg = False  # if got average temperature
sound_detected = 0
while 1:
    t = time.time()

    # Check switches
    b1 = GPIO.input(15)
    b2 = GPIO.input(18)
    b3 = GPIO.input(16)
    if not b1:
        tag = 1
        print("Good sleep.")
        break
    elif not b2:
        tag = 0
        print("Slept soso.")
        break
    elif not b3:
        tag = -1
        print("Bad sleep.")
        break

    # 5초 간격
    if int(standard_time - t) % 5 == 0:
        # 온습도 저장
        tmhd_vq = tmhd()
        db_insert(tmhd_vq[0], tmhd_vq[1])

        # 조도 저장
        lx_vq = lux()
        db_insert(lx_vq[0], lx_vq[1])

    # 2초 간격
    if int(standard_time - t) % 2 == 0:
        temps = camera.readPixels()
        temp = max(temps)
        ts.append(temp)
        # 기준 온도 저장 (ts[0])
        if len(ts) == 3 and not got_avg:
            avg_tm = (ts[0] + ts[1] + ts[2]) / 3
            ts = []
            ts.append(avg_tm)
            got_avg = True
        # 5분 동인 기준 온도보다 1.5도 떨어진 상태로 유지되면 and !started
        if not started:
            i = 0
            for f in ts[-5:]:
                if abs(ts[0] - f) < 1:
                    i += 1
                    continue
                else:
                    break
            if i == 5:
                t = time.localtime()
                starttime = '%04d-%02d-%02d %02d:%02d:%02d'\
                            % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
                started = True
    # 상시
    if GPIO.input(soundpin) == 1:
        sound_detected += 1

t = time.localtime()
endtime = '%04d-%02d-%02d %02d:%02d:%02d' % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)

# 평균 온습도, 조도 계산
avg_TM_HD = c.execute('''SELECT avg(TM), avg(HD) FROM tmhd WHERE Timestamp BETWEEN "%s" and "%s"'''\
                      % (starttime, endtime)).fetchone()
print("avg_TM_HD :", avg_TM_HD)
avg_LX = c.execute('''SELECT avg(LX) FROM lux WHERE Timestamp BETWEEN "%s" and "%s"'''\
                   % (starttime, endtime)).fetchone()
print("avg_LX :", avg_LX)

# 저장
date = '%04d-%02d-%02d' % (t.tm_year, t.tm_mon, time.localtime(time.time() - 86400).tm_mday)
db_insert([date, starttime, endtime, "%.2f" % avg_TM_HD[0], "%.2f" % avg_TM_HD[1],
           "%.0f" % avg_LX[0], sound_detected, tag], '''INSERT INTO Sleeptionary VALUES(?,?,?,?,?,?,?,?)''')

# 그래프 그리기
y_data = []
wday = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thr', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
xtick = []

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

plt.bar(xtick, y_data, color='#7B68EE')
plt.title("Last 7 days (h)")
plt.yticks([1/6, 1/2], ["10min", "30min"])
plt.savefig("../Web/images/overview.png")
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
plt.title("Last 7 days' Average Temperature (Celsius)")
plt.savefig("../Web/images/overview_tm.png")
plt.close()

# 최근 7일 간의 습도 그래프
plt.plot(xtick[::-1], seven_days_hd[::-1], marker="o", color="blue")
plt.title("Last 7 days' Average Humidity (%)")
plt.savefig("../Web/images/overview_hd.png")
plt.close()

# 페이지에 필요한 데이터 저장
f = open("../Web/data.txt", 'w')
for i in range(7):
    t = time.localtime(time.time() - 86400 * (7 - i))
    f.write("%04d/%02d/%02d\n" % (t.tm_year, t.tm_mon, t.tm_mday))
    # 일일 상세 페이지 그래프
    sleeping_tm = []
    sleeping_hd = []
    starttime, endtime = c.execute('''SELECT start, end FROM Sleeptionary WHERE Date = "%s"'''
                                   % "%04d-%02d-%02d" % (t.tm_year, t.tm_mon, t.tm_mday)).fetchone()
    c2 = c.execute('''SELECT TM, HD FROM tmhd WHERE Timestamp BETWEEN "%s" and "%s"'''
                   % (starttime, endtime))
    for s in c2:
        sleeping_tm.append(list(s)[0])
        sleeping_hd.append(list(s)[1])
    plt.plot(range(len(sleeping_tm)), sleeping_tm, color="red")
    plt.yticks([20, 23, 25, 28])
    plt.xticks([])
    plt.title("Temperature while sleeping (%s)" % ("%04d/%02d/%02d" % (t.tm_year, t.tm_mon, t.tm_mday)))
    plt.savefig("../Web/images/%dago_tm.png" % (7 - i))
    plt.close()
    plt.plot(range(len(sleeping_hd)), sleeping_hd, color="blue")
    plt.xticks([])
    plt.title("Humidity while sleeping (%s)" % ("%04d/%02d/%02d" % (t.tm_year, t.tm_mon, t.tm_mday)))
    plt.savefig("../Web/images/%dago_hd.png" % (7 - i))
    plt.close()

recommend_TM_HD = c.execute('''SELECT avg(TM_avg), avg(HD_avg) FROM Sleeptionary WHERE tag = 1''').fetchone()
f.write("%.0f\n" % recommend_TM_HD[0])
f.write("%.0f\n" % recommend_TM_HD[1])

f.close()
conn.close()
GPIO.cleanup()

# Git push
subprocess.call("git add %s" % db_path + " ../Web/images/*" + " ../Web/data.txt", shell=True)
subprocess.call("git commit -m 'Update DB, images'", shell=True)
subprocess.call("git push", shell=True)
