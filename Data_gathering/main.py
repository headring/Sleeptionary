import sqlite3
import time
import Adafruit_DHT

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

while 1:
    # 온습도 저장
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')

    li = [temperature, humidity]
    sq = '''INSERT INTO tmhd(TM, HD) VALUES(?,?)'''
    value = tuple(li)
    rm = c.execute(sq, value)
    conn.commit()

#    # 조도 저장
#    # 조도 측정 코드
#    lx = 0 # 조도값
#    sq = '''INSERT INTO lux(LX) VALUES(?)'''
#    value = tuple(lx)
#    rm = c.execute(sq, value)
#    conn.commit()

    time.sleep(300)

conn.close()
