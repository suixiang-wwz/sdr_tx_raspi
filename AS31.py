# -*- coding: utf-8 -*-
'''
433M发射机驱动
引脚定义 MD0 29 MD1 31  AUX = 37

'''
import wiringpi as gpio
import my_serial
from wiringpi import GPIO

MD0 = 29
MD1 = 31
AUX = 37
	
def AS31_init():
	#休眠模式	
	gpio.wiringPiSetupPhys()
	gpio.pinMode(MD0,1)
	gpio.pinMode(MD1,1)
	gpio.pinMode(AUX,0)
	gpio.digitalWrite(MD0, GPIO.HIGH)
	gpio.digitalWrite(MD1, GPIO.HIGH)
	# 初始化串口
	my_serial.SoftSerial_init()
	# AS31配置
	data = [0xC0,0x12,0x34,0x18,0x50,0x40]
	#my_serial.SoftSerial_WriteAscii(data)
	# 广播模式
	gpio.digitalWrite(MD0, GPIO.LOW)
	gpio.digitalWrite(MD1, GPIO.LOW)
	while (gpio.digitalRead(AUX) == 0):
		gpio.delay(1)
		print "failure to init"
	gpio.delay(1)
	print "inited"
	return 0
	
def AS31_SendFrame(data):
	# AUX=1
	while (gpio.digitalRead(AUX) == 0):
		gpio.delay(1)
	gpio.delay(1)
	my_serial.SoftSerial_WriteBytes(data[:256])
	print "send a frame"
	
	return 0

	
	
	
	
	
