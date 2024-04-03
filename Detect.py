#pip install pyaudio
#pip install SpeechRecognition

import speech_recognition as sr
import serial
import csv
import time


# ser=serial.Serial('COM3',9600)
try:
    ser = serial.Serial('COM3', 9600)
except serial.SerialException as e:
    print(f"串列通訊連接失敗: {e}")
    exit()

def Voice_To_Text(duration=10): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print(type(source))
        print("請開始說話:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=duration)
    try:
        Text = r.recognize_google(audio, language="zh-TW")
    
    except sr.UnknownValueError:
        Text = "無法翻譯"
    except sr.RequestError as e:
        Text = "無法翻譯{0}".format(e)
    return Text


#get from csv
csv_path="store.csv"
store_text=[]

def Scoring(text):
    # filtered_keywords=list(filter(lambda text: any(text),a))
    # if text in store_text:
    #     print(text)
    #     ser.write(b'go')
    # else:
    #     ser.write(b'stop')
    for keyword in store_text:
        if keyword in text:
            print("成功")
            ser.write(b'go')
            return
    return


with open(csv_path, newline='', encoding='utf-8') as csvfile:
   # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)

  # 以迴圈輸出每一列
  for row in rows:
    store_text.extend(row)
    # for i in row:
    #     Scoring(i)  


Text=Voice_To_Text(10)
# words=Text.split()
# for word in words:
#     Scoring(word)
Scoring(Text)



ser.close()