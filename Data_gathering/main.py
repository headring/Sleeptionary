import sqlite3
import time
import Adafruit_DHT


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

    return [lx, query]


# Connect database
db_path = "./test"
try:
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # c.execute("쿼리문")
except sqlite3.OperationalError:
    print("There is no database in path.")

# Initialize DHT sensor
sensor = Adafruit_DHT.DHT11
pin = 4

# Time iterator
T = 0

while 1:
    # 5분 간격
    if T % 300 == 0:
        # 온습도 저장
        tmhd_vq = tmhd()
        db_insert(tmhd_vq[0], tmhd_vq[1])

        # 조도 저장
        lx_vq = lux()
        db_insert(lx_vq[0], lx_vq[1])
    # if T % 100 == 0:
    #     # 최빈 온도값 저장

    T += 1
    time.sleep(1)

conn.close()
