- [x] 쌓은 데이터 내보내기
- [ ] 웹에 들어가는 그래프
- [ ] 조도 센서 결과 쌓기





### SQLite3 CLI

- `sqlite3 test` : DB 접속
- `.tables` : 테이블 목록
- `.quit`, `.exit` : 나가기
- 나머진 비슷함
- 트리거 목록 보기
  - `SEELCT * FROM sqlite_master WHERE type = 'trigger';`
- 모든 table의 row에는 64-bit signed integer key가 있다. (`rowid`)
  - 혹은 `old`, `_rowid_`
  - Foreign key의 reference로는 사용할 수 없다.

### DHT 센서

```shell
$ git clone https://github.com/adafruit/Adafruit_Python_DHT.git
$ cd Adafruit_Python_DHT
$ sudo apt-get update
$ sudo apt-get install build-essential python-dev python-openssl
$ sudo python setup.py install

출처: https://gorakgarak.tistory.com/686
```

