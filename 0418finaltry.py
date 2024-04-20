import serial
import speech_recognition as sr
import serial
import csv
import keyboard
import subprocess
import sys
import threading
import time

time.sleep(0.5)

recognizer = sr.Recognizer()
microphone = sr.Microphone()
print('啟動')





keyboard_switch=False
is_audio_detect_running = False
#get from csv
csv_path="store.csv"
store_text=[]
with open(csv_path, newline='', encoding='utf-8') as csvfile:
  rows = csv.reader(csvfile)
  for row in rows:
    store_text.extend(row)
    


def keyboard_detect():
    global keyboard_switch
    if keyboard.is_pressed('q'):
        if keyboard_switch is False:
            ser.write(b'go')
            keyboard_switch=not keyboard_switch
    elif keyboard.is_pressed('w'):
        if keyboard_switch is True:
            keyboard_switch=not keyboard_switch






def audio_detect(audio):
    global recognizer
    try:
        text = recognizer.recognize_google(audio, language='zh-TW')
        print(text)
        for keyword in store_text:
            if text=='重新啟動':
                python_path = sys.executable  
                subprocess.Popen([python_path] + sys.argv)
            if keyword in text:
                ser.write(b'go')
    except sr.UnknownValueError:
        print("UnknownValueError")

    finally:

        print("stop recognize")
        recognizer = sr.Recognizer()



ser = None 


if __name__ == '__main__':
    try:
        btnser=serial.Serial('COM4',9600)
        ser = serial.Serial('COM3', 9600)
    except serial.SerialException as e:
        print(f"串列通訊連接失敗: {e}")
        time.sleep(0.5)  

    while True:    
        if btnser.in_waiting>0:
            btnser.reset_input_buffer()
            print("別看了有收音")
            line = btnser.readline().decode('utf-8').rstrip()
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)  
                try:
                    audio = recognizer.listen(source, timeout=3)
                    audio_detect(audio)
                except sr.WaitTimeoutError:
                    print("Timeout occurred while listening for audio input")
                    recognizer = sr.Recognizer()  # Restart recognizer after a timeout
                    ser.write(b'go')
                    
                
                          



