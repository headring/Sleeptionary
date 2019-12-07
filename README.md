# Sleeptionary
- Prototype product name: **Dormir**


### INFO :
> **PLEASE BE NOTIFY THAT THIS PROJECT WAS DONE FOR TEAM_HW AND IT IS ONLY PROTOTYPE**
- Team_project STSBS at SoongSill Univ 19-2nd semester (2019년 2학기 숭실대 의생명시스템특론 팀프로젝트)
- USED TOOLS AND LANGUAGE: Laspberry Pi 3 & Python
- IDEA: To Improve Sleeping envriornment and habit (아이디어: 수면 개선)
- **Contributors: Kwon, Kim, Jang**(참여자: 권혁민, 김상현, 장인애)

- Description of Each folders(각 폴더에 대한 설명)
  - Data_gathering
    - This folder contains switch, photosensor, DHT11 sensor, graph code,
    - todo.md contains what we discussed to do
  - LCD(NO_USE)
    - We tried to show status with panel but cancled due to I2C works
    - Problem: PANEL did not show char, try if anyone looks this README.md
  - Light
    - It's for autor light swith(ON/OFF)
    - Idea was to get info from Data_gaterhing/lux.py and if light in ON, the module will turn off the switch
      - BENCHMARKED IDEA: [Servo Motor Controlled Wireless Light Switch](https://www.deviceplus.com/how-tos/arduino-guide/servo-motor-controlled-wireless-light-switch/
)
  - Meeting log
    - It contains team's discussion notes and ppt that we presented during the class(IN KOREAN)
  - Sound
    - The idea was to get users' environment sounds and analyze noises and snoring
    - However, we only had time to build sound module to analyze whater it is noise or not
  - Video
    - Very Key module on this project, because it reads users' temperature and gives data to DB
    - Used Sparkfun IR camera
    - should_do_for_cam.md is how to use this folder(Written in Korean, if needed, translate using google) 
  - Web
    - It's done for users interface
    - User can see their data
    ![page](index_imgae.png)
  
