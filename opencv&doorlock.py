import cv2
import numpy as np
import os
import sys
import RPi.GPIO as GPIO
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# 서보모터 및 부저 핀 설정
servopin = 17
piezo = 16

# 멜로디 주파수 리스트
melody = [783, 880, 987, 1046]
error = [130, 130, 130, 130]

#GPIO핀 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(servopin, GPIO.OUT)
GPIO.setup(piezo, GPIO.OUT)

#서보모터 주파수 주기 설정
servo = GPIO.PWM(servopin, 50)
servo.start(0)

#부저 주파수 주기 설정
buzz = GPIO.PWM(piezo, 1440)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX

#ID 카운터 시작
id = 0

# 실시간 비디오 캡처 초기화 및 시작
cap = cv2.VideoCapture(-1)
cap.set(3, 640) # set video widht
cap.set(4, 480) # set video height

# 얼굴로 인식 할 최소 창 크기 정의
minW = 0.1*cap.get(3)
minH = 0.1*cap.get(4)

while True:
	ret, img =cap.read()
	img = cv2.flip(img, -1) # 수직으로 뒤집기
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(gray,
		scaleFactor = 1.2,
		minNeighbors = 5,
		minSize = (int(minW), int(minH)),
		)
	for(x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
		id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
		# 신뢰도가 100보다 낮거나 ==> "0"이면 완벽하게 일치 함
		if (confidence < 100):
			id = "Collect"
			confidence = "  {0}%".format(round(100 - confidence))
		else:
			id = "unknown"
			confidence = "  {0}%".format(round(100 - confidence))

		cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
		cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  

	cv2.imshow('camera',img) 
	cv2.waitKey(1) & 0xff 
	if (id == "Collect"):
		break

# cap 및 cv2 종료
print("\n [INFO] Exiting Program and cleanup stuff")
cap.release()
cv2.destroyAllWindows()

class Myapp(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	passwd = [1,2,3,4]
	save = []
    
    # 비밀번호 및 서보보터 제어 함수
	def print_num(self, vbutton):
    
        #'*'를 클릭시 시 작동 함수
		if (vbutton.text() == '*'):
			if (self.save == self.passwd):
				self.info.setText("Open Door")
				self.info.show()
				buzz.start(5)
				for i in range (0, len(melody)):
					buzz.ChangeFrequency(melody[i])
					time.sleep(0.5)
					buzz.stop()
				servo.ChangeDutyCycle(7)
				time.sleep(0.5)
				servo.ChangeDutyCycle(12)
				time.sleep(0.3)
				servo.ChangeDutyCycle(7)
				time.sleep(1)
				servo.ChangeDutyCycle(2.3)
				time.sleep(1.5)
				servo.ChangeDutyCycle(7)

				self.save = []

			else:
				self.info.setText("Not collected")
				self.info.show()
				buzz.start(5)
				for i in range(0, len(error)):
					buzz.ChangeFrequency(error[i])
					time.sleep(0.5)
				servo.ChangeDutyCycle(7)
				buzz.stop()
				self.save = []
        
        # '#'을 클릭시 작동 함수
		elif (vbutton.text() == '#'):
			if(len(self.save) == 4):
				self.passwd = self.save
				self.info.setText("Change Password")
				self.info.show()
				self.save = []


		else:
			self.save.append(int(vbutton.text()))

	def initUI(self):
		self.setWindowTitle("DoorLock")
		self.resize(400, 300)
        
        # Label 생성
		self.info = QLabel("",self)
		self.info.move(120,10)
		self.info.resize(160,25)
        
        # 버튼 생성
		num1 = QPushButton("1",self)
		num2 = QPushButton("2",self)
		num3 = QPushButton("3",self)
		num4 = QPushButton("4",self)
		num5 = QPushButton("5",self)
		num6 = QPushButton("6",self)
		num7 = QPushButton("7",self)
		num8 = QPushButton("8",self)
		num9 = QPushButton("9",self)
		num10 =QPushButton("*",self)
		num11 =QPushButton("0",self)
		num12 =QPushButton("#",self)

        #버튼 위치
		num1.move(120,60)
		num2.move(170,60)
		num3.move(220,60)
		num4.move(120,110)
		num5.move(170,110)
		num6.move(220,110)
		num7.move(120,160)
		num8.move(170,160)
		num9.move(220,160)
		num10.move(120,210)
		num11.move(170,210)
		num12.move(220,210)

        #버튼 사이즈
		num1.resize(50,50)
		num2.resize(50,50)
		num3.resize(50,50)
		num4.resize(50,50)
		num5.resize(50,50)
		num6.resize(50,50)
		num7.resize(50,50)
		num8.resize(50,50)
		num9.resize(50,50)
		num10.resize(50,50)
		num11.resize(50,50)
		num12.resize(50,50)
        
        #버튼 클릭시 발생하는 이벤트 함수 호출
		num1.clicked.connect(lambda: self.print_num(num1))
		num2.clicked.connect(lambda: self.print_num(num2))
		num3.clicked.connect(lambda: self.print_num(num3))
		num4.clicked.connect(lambda: self.print_num(num4))
		num5.clicked.connect(lambda: self.print_num(num5))
		num6.clicked.connect(lambda: self.print_num(num6))
		num7.clicked.connect(lambda: self.print_num(num7))
		num8.clicked.connect(lambda: self.print_num(num8))
		num9.clicked.connect(lambda: self.print_num(num9))
		num10.clicked.connect(lambda: self.print_num(num10))
		num11.clicked.connect(lambda: self.print_num(num11))
		num12.clicked.connect(lambda: self.print_num(num12))


if __name__ == "__main__":
	app = QApplication(sys.argv)
	opencv_keypad = Myapp()
	opencv_keypad.show()
	sys.exit(app.exec_())
