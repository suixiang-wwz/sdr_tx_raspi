# -*- coding: utf-8 -*-
'''
GPIO模拟串口
引脚定义 RXD 35 TXD 33
baud：9600 1N8
'''
import wiringpi as gpio
from wiringpi import GPIO

RXD = 35
TXD = 33

def SoftSerial_init():
	gpio.wiringPiSetupPhys()
	gpio.pinMode(RXD,0)  #rxd in
	gpio.pinMode(TXD,1) #txd out
	gpio.digitalWrite(TXD, GPIO.HIGH)
	
	return 0
	
def SoftSerial_WriteByte(data):
	gpio.digitalWrite(TXD, GPIO.LOW)
	
	for ii in range(8):
		if (data>>ii & 0x01)==0:
			gpio.digitalWrite(TXD, GPIO.LOW)
		else:
			gpio.digitalWrite(TXD, GPIO.HIGH)
		gpio.delayMicroseconds(104)
		
	gpio.digitalWrite(TXD, GPIO.HIGH)
	gpio.delayMicroseconds(104)
	
	return 0
		
def SoftSerial_WriteBytes(data):
	asciistream = [ord(temp) for temp in data]
	for ii in range(len(asciistream)):
		SoftSerial_WriteByte(asciistream[ii])
		
	return 0
		
def SoftSerial_WriteAscii(asciistream):
	for ii in range(len(asciistream)):
		SoftSerial_WriteByte(asciistream[ii])
	
	return 0

	
	
