import pyautogui

# pyautogui.mouseInfo()
pyautogui.PAUSE = 1 # 모든 동작에 1초 
# 마우스 정보

for i in range(10):
    pyautogui.move(100,100)

# failsafe : 네귀퉁이에 마우스를 가져다놓으면 동작 멈춤
