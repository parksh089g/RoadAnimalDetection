## 출처
https://github.com/thtrieu/darkflow
를 수정하였습니다.

## Dependencies

Python3.7 이하, tensorflow 1.15, numpy, opencv 3.
추가 사용 모듈: time, pyautogui, requests

### 사용방법

darkflow의 기본 설치 및 사용방법은 https://github.com/thtrieu/darkflow 에서 참고하시면 됩니다.

1. 원하는 위치에 cctv스트리밍창을 띄우고, capture.py 에서 캡쳐구간을 확인합니다.
    ```
    python capture.py
    ```

2. test.py에서 원하는 cctv 구간을 설정합니다.
    ```
    pyautogui.screenshot('test이미지',region=(x,y,lengthX,lengthY)) #region= 커서위치x,y& x,y길이
    ```

3. sendingToServer()함수에서 cctv위치(위도,경도)를 수정합니다. 서버의 url도 원하는 url로 수정합니다.
    ```
     datas = {"results":"animal detected!!", "location":"가덕영업소", "Time":time.strftime('%y-%m-%d %H:%M:%S'),"longitude": "35.1881","latitude":"126.862893"}
    ```

4. 모델을 변경하고 싶다면 testing() 함수에서 options 부분을 수정하면 됩니다.
    ```
     options = {"model": "cfg/yolo.cfg", "load": "bin/yolov2.weights", "threshold": 0.1}
    ```

5. test.py을 실행시키면 5초(지연시간/설정가능)에 한번씩 cctv의 이미지를 가져와 동물이 있는지 없는지 확인합니다. 있다면 설정한 서버의 url로 datas가 보내집니다.
   ```
     python test.py
   ```
