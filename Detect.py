#pip install pyaudio
#pip install SpeechRecognition

import speech_recognition as sr

import csv

key="都你在講"
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
a=Text.split()
print(a)
#read from csv 因為如果重複出現 那一定是挺暈的對吧?


#get from csv
csv_path="store.csv"


def Scoring(text):
    filtered_keywords=list(filter(lambda text: any(text),a))
    if any(filtered_keywords):
        print("成功")
    
    
with open(csv_path, newline='', encoding='utf-8') as csvfile:
   # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)

  # 以迴圈輸出每一列
  for row in rows:
    for i in row:
        Scoring(i)

    
    
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