import random

f = open("test_data.txt", 'w')
mon = int(input("Month : "))
day = int(input("Day : "))
h = int(input("Hour : ")) + 15
m = int(input("Minute : "))
tm = int(input("Temperature : "))
hd = int(input("Humidity : "))

date = "2019-%02d-%02d" % (mon, day)
hour = 22 - 9
min = 0
while 1:
    timestamp = "%s %02d:%02d:00" % (date, hour, min)
    t = random.uniform(tm, tm + 1)
    h2 = random.uniform(hd, hd + 5)

    f.write('''INSERT INTO tmhd VALUES("%s", %.2f, %.2f);\n''' % (timestamp, t, h2))

    min += 5
    if min >= 60:
        min -= 60
        hour += 1
        if hour == 24:
            hour = 0
    if hour * 60 + min >= h * 60 + m:
        break

f.write('''insert into Sleeptionary values("2019-12-04", "2019-12-03 22:00:10", "2019-12-04 06:23:12", 23.5, 33.5, 15, 124, 1)''')