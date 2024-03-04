#pip install pyaudio
#pip install SpeechRecognition

import speech_recognition as sr

import csv

key=[]
def Voice_To_Text(duration=7): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
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
#while click
Text=Voice_To_Text(10)
key[0]=Text
a=key.split()

# csv_path = "output.csv"
# header = ["Text"]
# with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(header)
#     for i in range(3):
#         Text = Voice_To_Text(10)
#         csv_writer.writerow([Text])
#         print(Text)
# print("已將語音轉換結果寫入 output.csv 文件")