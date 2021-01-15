import RPi.GPIO as GPIO
import time

# piezo, 초음파센서 핀설정
Trig = 0
Echo = 1
piezo = 17

# piezo 멜로디 설정
melody = [500, 510, 520]

# piezo 및 초음파센서 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)
GPIO.setup(piezo, GPIO.OUT)

# piezo 주파수 설정
buzz = GPIO.PWM(piezo, 1000)

def measure():
	GPIO.output(Trig, True)
	time.sleep(0.00001)
	GPIO.output(Trig, False)
	start = time.time() #현재시간을 start 변수에 저장
	while GPIO.input(Echo) == False: # Echo가 없을 때
		start = time.time()
	while GPIO.input(Echo) == True: # Echo가 있을 때
		stop = time.time() # 현재시간을 stop 변수에 저장
	elapsed = stop - start
	distance = (elapsed * 19000) / 2
	return distance

try:
	while True:
		distance = measure()
		print("Distance : %.2f cm" % distance)
		time.sleep(0.01)
		buzz.start(50)

		if distance < 5: # 5cm 미만일 때 경고음 작동
			buzz.ChangeFrequency(melody[0])
			time.sleep(0.02)
			buzz.stop()

		elif distance < 15: # 15cm 미만일 때 경고음 작동
			buzz.ChangeFrequency(melody[1])
			time.sleep(0.5)
			buzz.stop()

		elif distance <30: # 30cm 미만일 때 경고음 작동
			buzz.ChangeFrequency(melody[2])
			time.sleep(1)
			buzz.stop()
		else:
			buzz.stop()

except KeyboardInterrupt:
	GPIO.cleanup()
