# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 17:36:37 2021

@author: User
"""

from darkflow.net.build import TFNet
import cv2
import time
import pyautogui
import requests

def capturing(): #캡쳐구간 설정
    print("Current Mouse Position:",pyautogui.position()) #커서위치확인
    pyautogui.screenshot('./test.png',region=(30,180,500,300)) #region= 커서위치x,y& x,y길이

def testing():
    options = {"model": "cfg/yolo.cfg", "load": "bin/yolov2.weights", "threshold": 0.1}
    tfnet = TFNet(options)
    imgcv = cv2.imread("./test.png")
    result = tfnet.return_predict(imgcv)
    return result
    
def sendingToServer(results):
    #datas = {"results":"animal detected!!", "location":"[경부고속도로]부지", "Time":time.strftime('%y-%m-%d %H:%M:%S'),"longitude": "35.8046466536","latitude":"129.1867718281"}
    datas = {"results":"animal detected!!", "location":"가덕영업소", "Time":time.strftime('%y-%m-%d %H:%M:%S'),"longitude": "35.1881","latitude":"126.862893"}
    url="http://ec2-3-34-151-216.ap-northeast-2.compute.amazonaws.com:3000/update"
    requests.post(url, data=datas)

def parsing(results):
    a=0
    for i in range(len(results)):
        if results[i]=={'animal'}:
            print("animal detected")
            sendingToServer(results)
            print("sending detection complete")
            a=a+1
            break
    if a==0:
        print("no animal detected")


while True:
    print("========================start===============================")
    capturing()
    result=testing()
    print(result)
    parsing(result)
    print("=========================end================================")
    time.sleep(5)  #지연시간