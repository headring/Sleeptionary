import sqlite3
import time
import Adafruit_DHT
import matplotlib as mpl
import pylab as plb
from Adafruit_AMG88xx import Adafruit_AMG88xx


def db_insert(li, qr):
    value = tuple(li)
    rm = c.execute(qr, value)
    conn.commit()


def tmhd():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}'C  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')

    query = '''INSERT INTO tmhd(TM, HD) VALUES(?,?)'''

    return [[temperature, humidity], query]


def lux():
    # 조도 측정 코드
    lx = 0 # 조도값
    query = '''INSERT INTO lux(LX) VALUES(?)'''

    return [[lx], query]


# Connect database
db_path = "./test.db"
try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # c.execute("쿼리문")
except sqlite3.OperationalError:
    print("There is no database in path.")

# Initialize DHT sensor
sensor = Adafruit_DHT.DHT11
pin = 4

# Initialize thermal camera
camera = Adafruit_AMG88xx()

# Time iterator
T = 0

started = False
while 1:
    # 5분 간격
    if T % 300 == 0:
        # 온습도 저장
        tmhd_vq = tmhd()
        db_insert(tmhd_vq[0], tmhd_vq[1])

        # 조도 저장
        lx_vq = lux()
        db_insert(lx_vq[0], lx_vq[1])

    # 1분 간격
    if T % 100 == 0:
        # 최빈 온도값 저장
        ts = []
        temps = camera.readPixels()
        temp = max(temps, key=temps.count)
        ts.append(temp)
        # 5분 이상 떨어진 상태로 유지되면 and !started
        if ts[-5:] == [temp] * 5:
            t = time.localtime()
            starttime = '%04d-%02d-%02d %02d:%02d:%02d' % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
            started = True

    # if 스위치가 눌려지면
    # break

    T += 1
    time.sleep(1)

t = time.localtime()
endtime = '%04d-%02d-%02d %02d:%02d:%02d' % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)

# tag 따기
tag = 0

# 평균 온습도, 조도 계산
avg_TM_HD = c.execute('''SELECT avg(TM), avg(HD) FROM tmhd WHERE Timestamp BETWEEN "%s" and "%s"''' % (starttime, endtime))
avg_LX = c.execute('''SELECT avg(LX) FROM lux WHERE Timestamp BETWEEN "%s" and "%s"''' % (starttime, endtime))

# 저장
db_insert(['%04d-%02d-%02d' % (t.tm_year, t.tm_mon, t.tm_mday), starttime, endtime, avg_TM_HD[0], avg_TM_HD[1],
           avg_LX[0], tag], '''INSERT INTO Sleeptionary VALUES(?,?,?,?,?,?,?)''')

# 그래프 그리기


conn.close()
