#### 초기 설정

sudo raspi-config (완료)

select "interfacing options"

activate VNC (완료)

activate I2C (완료)

select <FINISH>

sudo reboot (완료)

#### Check to see if I2C is setup correctly

sudo i2cdetect -y 1 (You should see a 69 on column 9) (69보임)

#### Download and install packages outlined in Adafruit guide

sudo apt-get install -y build-essential python-pip python-dev python-smbus git
git clone https://github.com/adafruit/Adafruit_Python_GPIO....

cd Adafruit_Python_GPIO

sudo python setup.py install

여기까지도 완료

#### Install pygame and scipy

sudo apt-get install -y python-scipy python-pygame 
sudo pip install colour Adafruit_AMG88xx

python2로 사용?

- 아직 5번으로 넘어가지 말기
- 안되서 다른 코드로 가봄 [클릭](https://github.com/adafruit/Adafruit_CircuitPython_AMG88xx)
	- 총 3개의 dependecy 중에 circuit만 안됨 (register 아님)
- 위에 것도 안되면 [이쪽 코드로 가서 실행해보기](https://learn.adafruit.com/adafruit-amg8833-8x8-thermal-camera-sensor/raspberry-pi-thermal-camera)
- 이것도 안되면 공식사이트것을 실험해보기 [공식사이트](https://learn.sparkfun.com/tutorials/qwiic-grid-eye-infrared-array-amg88xx-hookup-guide/all)

#### Run example script

cd ~/
git clone https://github.com/adafruit/Adafruit_AMG88xx_python

cd Adafruit_AMG88xx_python/examples

sudo python thermal_cam.py
