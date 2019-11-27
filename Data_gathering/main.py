import sqlite3

db_path = ""
try:
    conn = sqlite3.connet(db_path)
    c = conn.cursor()
    c.execute("쿼리문")
except:
    print("경로 상에 DB 없음")

li = []
sq = '''INSERT INTO table_name VALUES(?,?,?)'''
value = tuple(li)
rm = c.execute(sq, value)
conn.commit()

conn.close()
