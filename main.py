import pyautogui as pag
import time
import random

time.sleep(5)

def convert_random(center_x, center_y, offset=15):
    x_random = center_x + random.randint(-offset, offset)
    y_random = center_y + random.randint(-offset, offset)
    return x_random,y_random

def Check_MainLobby():
    try:
        MainStartImage = pag.locateOnScreen("MainStart.png", confidence=0.8)
        if MainStartImage:
            print(f"[ Check MainLobby ] : 메인 로비에 있습니다. 스크립트를 실행합니다. : {MainStartImage}")
            return True
        else:
            return False
    except Exception as e:
        print("[ Check MainLobby ] : 이미지를 찾을 수 없습니다.")
        return False

def Check_DoubleCoin():
    try:
        DoubleCoinImage = pag.locateOnScreen("DoubleCoin.png", confidence=0.8)
        if DoubleCoinImage:
            print(f"[ Check DoubleCoin ] : 이미지를 찾았습니다.: {DoubleCoinImage}")
            return True
        else:
            return False
    except Exception as e:
        print("[ Check DoubleCoin ] : 이미지를 찾을 수 없습니다.")
        return False

def Check_GameResult():
    try:
        GameResultImage = pag.locateOnScreen("GameResult.png", confidence=0.8)
        if GameResultImage:
            print(f"[ Check GameResult ] : 이미지를 찾았습니다.: {GameResultImage}")
            return True
        else:
            return False
    except Exception as e:
        return False

def Check_MysteryBox():
    try:
        MysteryBoxImage = pag.locateOnScreen("MysteryBox.png", confidence=0.7)
        if MysteryBoxImage:
            print(f"[ Check MysteryBox ] : 이미지를 찾았습니다.: {MysteryBoxImage}")
            return True
        else:
            return False
    except Exception as e:
        print(f"[ Check MysteryBox ] : 이미지를 찾을 수 없습니다.")
        return False

def LoopForDoubleCoin():
    while not Check_DoubleCoin():
        click_cool = 0.2
        pag.click(815, 875)
        time.sleep(click_cool)
        pag.click(1400, 430)
        time.sleep(click_cool)
        pag.click(1195, 680)
        time.sleep(0.5)
        if Check_DoubleCoin():
            break
        time.sleep(1) # 1초 대기 후 다시 시도

def Main():
    if Check_MainLobby():
        pag.click(1440, 960) # 메인 게임 시작 버튼
        LoopForDoubleCoin()
        pag.click(1330, 910) # 두번째 게임 시작 버튼
        print("----------\n게임이 시작되었습니다\n----------")
        time.sleep(2) # 게임 로딩 시간

        while not Check_GameResult(): # 게임 결과 화면 대기
            pag.click(convert_random(180,930))
            time.sleep(random.uniform(0.01, 0.5)) # 0.01 ~ 0.5 사이 숫자 딜레이
            if Check_GameResult():
                time.sleep(5)
                pag.click(679, 952)
                break

        time.sleep(3) # 미스테리 화면 보여지는 시간 틱

        if Check_MysteryBox(): # 미스테리 박스 화면 확인
            pag.click(955, 965)
            time.sleep(3)
            pag.click(955, 965)

        print("----------\n게임이 종료되었습니다.\n----------")
        time.sleep(5)

for _ in range(2):
    Main()

# 메인 "게임 시작" 버튼 위치 x=1440, y=960
# 두번째 "게임 시작" 버튼 위치 x=1330, y=910
# "부스트 뽑기" 버튼 위치 x=815, y=875
# 부스트 "구매" 버튼 위치 Point(x=1400, y=430
# 부스트 다시 뽑을때 "구매" 버튼 위치 x=1195, y=680
# 게임 결과창 "확인" 버튼 위치 x=679, y=952
# 미스테리 박스 "열기" , "확인" 버튼 위치 x=955, y=965)
# 인게임 점프 x=180, y=930)
