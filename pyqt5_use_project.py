import RPi.GPIO as GPIO
import sys
import serial
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#시리얼 통신 설정
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=5)

#서보 모터 핀 설정
servopin = 17

#LED 핀 설정
Red = 13
Green = 19
Blue = 26

# Piezo 핀 설정
piezo = 22

# melody 주파수 설정 list
melody = [262, 294, 330, 349, 392, 440, 494]

#GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(Red, GPIO.OUT)
GPIO.setup(Green, GPIO.OUT)
GPIO.setup(Blue, GPIO.OUT)
GPIO.setup(servopin, GPIO.OUT)
GPIO.setup(piezo, GPIO.OUT)

# 서보모터 주기 설정
servo = GPIO.PWM(servopin, 50)
servo.start(0)

# 주파수 주기 설정
buzz = GPIO.PWM(piezo, 1000)
 
# LED 주기 설정
pwm = GPIO.PWM(Blue, 1000)
pwm.start(0)

class MyApp(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle("Mini_Project")
		self.move(300, 300)
		self.resize(720, 480)

        # 아두이노 데이터 값 표시 라벨 설정
		self.Data = QLabel("",self)
		self.Data.move(250,200)
		self.Data.resize(350,30)
		self.Data.setStyleSheet("color: #000000; border-style: solid; border-width: 2px; border-color: #D3D3D3; border-radius: 5px; ")

        # 타임 설정
 		self.time = QTimer(self)
		self.time.timeout.connect(self.show_view)
        
        # 음계 버튼 설정
 		button_do = QPushButton("도", self)
		button_re = QPushButton("레", self)
		button_mi = QPushButton("미", self)
		button_fa = QPushButton("파", self)
		button_sol = QPushButton("솔", self)
		button_la = QPushButton("라", self)
		button_si = QPushButton("시", self)

        # 버튼 크기 설정
		button_do.move(10, 10)
		button_re.move(110, 10)
		button_mi.move(210, 10)
		button_fa.move(310, 10)
		button_sol.move(410, 10)
		button_la.move(510, 10)
		button_si.move(610, 10)

        # 서보모터 버튼 설정 및 버튼 크기 설정
		button_servo1 = QPushButton("서보모터_90도", self)
		button_servo1.move(10,100)

		button_servo2 = QPushButton("서보모터_0도", self)
		button_servo2.move(10,200)

		button_servo3 = QPushButton("서보모터_-90", self)
		button_servo3.move(10,300)

        # 음계 버튼 인터럽트 처리 함수 선언
		button_do.clicked.connect(self.button1_clicked)
		button_re.clicked.connect(self.button2_clicked)
		button_mi.clicked.connect(self.button3_clicked)
		button_fa.clicked.connect(self.button4_clicked)
		button_sol.clicked.connect(self.button5_clicked)
		button_la.clicked.connect(self.button6_clicked)
		button_si.clicked.connect(self.button7_clicked)
        
        # 서보모터 버튼 인터럽트 처리 함수 선언
		button_servo1.clicked.connect(self.button_servo_clicked)
		button_servo2.clicked.connect(self.button_servo2_clicked)
		button_servo3.clicked.connect(self.button_servo3_clicked)

        # 아두이노 데이터 값 버튼 설정 및 크기 설정
		button_ctr = QPushButton("CTH_DATA", self)
		button_ctr.move(300,300)
		button_stop = QPushButton("STOP", self)
		button_stop.move(400, 300)
        
        # 아두이노 데이터 값 버튼 인터럽트 처리 함수 선언
		button_ctr.clicked.connect(self.button_ctr_clicked)
		button_stop.clicked.connect(self.button_stop_clicked)


    # 음계 버튼 인터럽스 함수 정의
	def button1_clicked(self):
		buzz.start(50)
		pwm.ChangeDutyCycle(5)
		buzz.ChangeFrequency(melody[0])
		time.sleep(0.5)
		buzz.stop()

	def button2_clicked(self):
		buzz.start(50)
		pwm.ChangeDutyCycle(15)
		buzz.ChangeFrequency(melody[1])
		time.sleep(0.5)
		buzz.stop()

	def button3_clicked(self):
		buzz.start(50)
		pwm.ChangeDutyCycle(30)
		buzz.ChangeFrequency(melody[2])
		time.sleep(0.5)
		buzz.stop()

	def button4_clicked(self):
		buzz.start(50)
		pwm.ChangeDutyCycle(45)
		buzz.ChangeFrequency(melody[3])
		time.sleep(0.5)
		buzz.stop()

	def button5_clicked(self):
		buzz.start(50)
		pwm.ChangeDutyCycle(60)
		buzz.ChangeFrequency(melody[4])
		time.sleep(0.5)
		buzz.stop()

	def button6_clicked(self):
		buzz.start(50)
		pwm.ChangeDutyCycle(75)
		buzz.ChangeFrequency(melody[5])
		time.sleep(0.5)
		buzz.stop()

	def button7_clicked(self):
		buzz.start(50)
		pwm.ChangeDutyCycle(100)
		buzz.ChangeFrequency(melody[6])
		time.sleep(0.5)
		buzz.stop()

    # 서보모터 버튼 인터럽스 함수 정의
	def button_servo_clicked(self):
		servo.ChangeDutyCycle(2.3)

	def button_servo2_clicked(self):
		servo.ChangeDutyCycle(7)

	def button_servo3_clicked(self):
		servo.ChangeDutyCycle(12)

    # 아두이노 데이터 값 버튼 인터럽스 함수 정의
	def button_ctr_clicked(self):
		self.time.start()
		self.Data.show()

	def button_stop_clicked(self):
		self.time.stop()
		self.Data.setText("STOPPED!!")
		self.Data.show()

    # QLabel에 보여질 데이터 값 함수 정의
	def show_view(self):
		read_ser = ser.readline().decode()[:-2]
		cds = str(read_ser[6:9])
		temp = str(read_ser[16:24])
		humi = str(read_ser[31:39])
		self.Data.setText("CDS : " + cds + " TEMP : " + temp + "HUMI : " + humi)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	mypiano = MyApp()
	mypiano.show()
	sys.exit(app.exec_())