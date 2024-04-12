import numpy as np
import speech_recognition as sr
import serial
import csv
import time

csv_path="store.csv"
store_text=[]

text=input("enter text")


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

def Scoring(text):
    index = binary_search(store_text, text)
    if index != -1:
        print("成功找到"+text)
    else:
        print("未找到")
        
        
        
with open(csv_path, newline='', encoding='utf-8') as csvfile:
   # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)

  # 以迴圈輸出每一列
  for row in rows:
    store_text.extend(row)
    store_text.sort()
    
    
Scoring(text)
print(store_text)