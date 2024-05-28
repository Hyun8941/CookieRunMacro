# CookieRun Macro v1

모바일 에뮬레이터로 (Nox BlueStack .. ETC) 쿠키런을 실행하여 **바나나맛 쿠키**와 **코인 2배** 부스트를 이용한 반복 매크로 입니다.

효율은 **2분15초 ~ 2분 40초** 사이 약 **17,000 ~ 25,000** 코인입니다.

*아직 수정할 부분도 많고 가끔 쿠키런 봇 감지에 걸려 퍼즐을 풀어야 할 수 있습니다.*



# 설치해야하는 라이브러리

해당 코드를 작동하기 위해서 필수로 필요한 몇 가지 라이브러리가 있습니다.

## opencv-python

    pip install opencv-python

## PyAutoGUI 

    pip install PyAutoGUI

## numpy

    pip install numpy

# 스크립트 간단한 요약

 1. Main() 함수가 시작되면서 화면이 메인 로비인지 MainStart.png로 확인을 합니다. 메인 로비가 확인되면 진행되고 메인 로비가 아닐 시 종료됩니다.
 2. 부스트 뽑기를 통해서 코인 2배가 나올 때까지 반복합니다. 확인은 DoubleCoin.png 사진을 통해 확인됩니다.
 3. 게임 결과 화면 GameResult.png 가 보일 때까지 0.1초 ~ 0.5초 사이의 값으로 점프를 클릭합니다.

 4. 게임 결과 화면이 인식되면 확인 버튼을 누르고 MysteryBox.png 를 통해 미스테리 박스를 얻었는지를 확인합니다.
