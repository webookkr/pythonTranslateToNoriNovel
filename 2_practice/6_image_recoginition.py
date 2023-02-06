import pyautogui as pg

# file_menu = pyautogui.locateOnScreen("file_menu.png")

# print(file_menu)
# pyautogui.click(file_menu)

# 윈도우 시프트 s (캡처)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)
# pyautogui.click(screen)

# for i in pyautogui.locateAllOnScreen("checkbox.png") :
#     print(i)
#     pyautogui.click(i,duration=0.25)

# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)

# 속도개선 : 
# 1.Grayscale (색 무시 : 30퍼센트 정도 개선)

# for i in pyautogui.locateAllOnScreen("checkbox.png", grayscale=True) :
#     print(i)
#     pyautogui.click(i)

# # 2. 범위 한정 
# pg.mouseInfo()
# 1099,664 255,255,255 #FFFFFF
# 810,685 255,251,223 #FFFBDF
# ic_trash = pg.locateOnScreen("ic_trash.png", region=(1200,800, 1800,1000))
# pg.moveTo(ic_trash)

# 3. 정확도 조절 
# ic_trash = pg.locateOnScreen("ic_trash_", confidence=0.9) # 기본값 0.999 , 90%

# 자동화 대상이 바로 보여지지 않는 경우 

# file_menu = pg.locateOnScreen("file_menu_note.png")
# if file_menu : 
#     pg.click(file_menu)
# else :
#     print("발견실패")

# 계속 기다리기 
# while file_menu is None : 
#     file_menu = pg.locateOnScreen("file_menu_note.png")
#     print("발견실패")
# pg.click(file_menu)
# print("발견성공")

# timeout 설정 : time() : 현재 시간 -> while timeout 설정하여 그 시간동안 반복실행
import time
import sys

# timeout = 10 #10초
# start = time.time() # 시작 시간 설정 
# file_menu_notepad = None 
# while file_menu_notepad is None :
#     file_menu_notepad = pg.locateOnScreen("file_menu_note.png")
#     end = time.time() # 끝나는 시간 설정
#     if end - start > timeout : # 텀이 10초보다 크면 종료 
#         print("시간 종료")
#         sys.exit()  # 시스템 종료 
# pg.click(file_menu_notepad)


def find_target(img_file, timeOut=1):
    start = time.time() # 시작 시간 설정 
    target = None 
    while target is None :
        target = pg.locateOnScreen(img_file)
        end = time.time() # 끝나는 시간 설정
        if end - start > timeOut : # 텀이 10초보다 크면 종료 
            break
    return target     

def my_click(img_file, timeOut=1):
    target = find_target(img_file, timeOut)
    if target :
        pg.click(target)
    else :
        print(f"[Timeout {timeOut}s] Target is not found ({img_file})")
        sys.exit()   

my_click("ic_trash.png", timeOut=5)