# Sleeptionary

- Prototype product name: **Dormir**

## INFO

> **PLEASE NOTE THAT THIS PROJECT WAS DONE FOR TEAM_HW AND IT IS ONLY PROTOTYPE**

- Team_project STSBS at Soongsill Univ. 19-2nd semester (2019년 2학기 숭실대 의생명시스템특론 팀프로젝트)
- USED TOOLS AND LANGUAGE: Raspberry Pi 3 & Python3
- IDEA: To improve sleeping environment and habit (아이디어: 수면 개선)
- **Contributors: Kwon, Kim, Jang**(참여자: 권혁민, 김상현, 장인애)

## Description

- Data_gathering
  - This folder contains switch, photosensor, DHT11 sensor, graph code.
  - `todo.md` contains what we discussed to do.
- Light
  - It's for auto light switch (ON/OFF).
  - Idea was to get info from `Data_gathering/lux.py` and if light in ON, the module will turn off the switch.
    - BENCHMARKED IDEA: [Servo Motor Controlled Wireless Light Switch](https://www.deviceplus.com/how-tos/arduino-guide/servo-motor-controlled-wireless-light-switch/
)
- Meeting log
  - It contains team's discussion notes and presentations that we presented during the class (IN KOREAN).
- Sound
  - The idea was to get users' environment sounds and analyze noises and snoring.
  - However, we only had time to build sound module to analyze whether it is noise or not.
- Video
  - It has files for cameras to read users' temperature and store data.
  - Used Sparkfun IR camera.
  - `should_do_for_cam.md` is how to use this folder.
- Web
  - User can see their data via browser.
  
