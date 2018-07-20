# -*- coding: utf-8 -*  
import serial  
import time  
# �򿪴���  
ser = serial.Serial("/dev/ttyAMA0", 115200)  
def main():  
    while True:  
        # ��ý��ջ������ַ�  
        count = ser.inWaiting()  
        if count != 0:  
            # ��ȡ���ݲ�����  
            recv = ser.read(count)+"....return\n\n" 
            ser.write(recv)  
        # ��ս��ջ�����  
        ser.flushInput()  
        # ��Ҫ�������ʱ  
        time.sleep(0.1)  
      
if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close() 