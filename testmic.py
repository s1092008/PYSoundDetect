import pyaudio
import wave
import speech_recognition as sr
import serial
import os

chunk = 1024                     # 記錄聲音的樣本區塊大小
sample_format = pyaudio.paInt16  # 樣本格式，可使用 paFloat32、paInt32、paInt24、paInt16、paInt8、paUInt8、paCustomFormat
channels = 2                     # 聲道數量
fs = 44100                       # 取樣頻率，常見值為 44100 ( CD )、48000 ( DVD )、22050、24000、12000 和 11025。
seconds = 5                      # 錄音秒數
filename = "teststudio.wav"      # 錄音檔名
ser = serial.Serial('COM3', 9600)
# serLight=serial.Serial('COM4',12800)

p = pyaudio.PyAudio()            #      建立 pyaudio 物件

print("開始錄音...")

# 開啟錄音串流
stream = p.open(format=sample_format, channels=channels, rate=fs, frames_per_buffer=chunk, input=True)

frames = []                      # 建立聲音串列

for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)          # 將聲音記錄到串列中

stream.stop_stream()             # 停止錄音
stream.close()                   # 關閉串流
p.terminate()

print('錄音結束...')

# check if file exist
def save_wav_file(filename, channels, sample_format, fs, frames):
    if os.path.exists(filename):
        filename = filename.split('.')[0] + '1.' + filename.split('.')[1]
    # 將原始音訊資料儲存到 WAV 檔案中
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))       

save_wav_file(filename, channels, sample_format, fs, frames)


# 使用 SpeechRecognition 來辨識錄音中的文字
recognizer = sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data, language='zh-TW')

Text=text.split()
print(Text)
x='我'
if x in text:
    ser.write(b'go')
    print('go')
    # serLight.write(b'go')
else:
    ser.write(b'stop')
