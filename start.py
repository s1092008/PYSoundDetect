import serial
import subprocess

ser = serial.Serial('COM4', 9600)



def waitforsign():
            line = ser.readline().decode('utf-8').rstrip()
            if line == "start":
                subprocess.Popen(["python", "Detect.py"])
                print('ohoh')
                
try:
    if not ser.is_open:
        ser.open()  
    T=True
   
    while T:
        if ser.in_waiting > 0:
            ser.reset_input_buffer()
            waitforsign()

except KeyboardInterrupt:
    print("程式被使用者中斷...")
finally:
    ser.close()


