import serial
import speech_recognition as sr
import serial
import csv
import keyboard
import subprocess
import sys
import threading
import time
#大綱
#run時先把CSV中的目標物先都存好
#當麥克風收音的時候辨識 #linear search O(N^M^K) N為目標數 M為目標內容長度 K為輸入長度 #如果用Hash bucket去分.....
#如果有 就serial write 
#atleast Move
time.sleep(0.5)

recognizer = sr.Recognizer()
microphone = sr.Microphone()






keyboard_switch=False
is_audio_detect_running = False
#get from csv
csv_path="store.csv"
store_text=[]
with open(csv_path, newline='', encoding='utf-8') as csvfile:
  rows = csv.reader(csvfile)
  for row in rows:
    store_text.extend(row)
    
def restart_program():
    global ser
    python_path = sys.executable  
    timer.cancel()
    if ser:
        ser.close()
    subprocess.Popen([python_path] + sys.argv)
    print('RESTART')
    sys.exit()  


def timeout_callback():
    restart_program()

def restart_timer():
    global timer
    timer.cancel() 
    timer = threading.Timer(30, timeout_callback)  
    timer.start() 


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
    # global is_audio_detect_running
    # if is_audio_detect_running:
    #     return
    # is_audio_detect_running = True
    global recognizer
    restart_timer()
    try:
        text = recognizer.recognize_google(audio, language='zh-TW')
        print(text)
        
        for keyword in store_text:
            if text=='關閉':
                sys.exit() 
            if keyword in text:
                ser.write(b'go')
    except sr.UnknownValueError:
        print("UnknownValueError")
        restart_program()
    finally:
        # is_audio_detect_running = False\
        print("stop recognize")
        recognizer = sr.Recognizer()



ser = None 
timer = threading.Timer(15, timeout_callback)

if __name__ == '__main__':
    while True:
        try:
            ser = serial.Serial('COM3', 9600)
            break  
        except serial.SerialException as e:
            print(f"串列通訊連接失敗: {e}")
            time.sleep(0.5)  




    while True:
        # if ser.in_waiting > 0:
        #     ser.reset_input_buffer()
        #     input = ser.readline().decode().strip()
        #     keyboard_detect()
                    
        with microphone as source:
                recognizer.adjust_for_ambient_noise(source)  
                audio = recognizer.listen(source)
                audio_detect(audio)
                    
            



