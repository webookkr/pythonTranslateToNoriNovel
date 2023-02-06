import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화 윈도우
# print(fw.title)
# print(fw.size) # 창의 크기 
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보
# pyautogui.click(fw.left+35, fw.top+20) # 좌표 기반 클릭

# for w in pyautogui.getAllWindows():
#     print(w)

# for w in pyautogui.getWindowsWithTitle("제목 없음")[0]:
#     print(w)
# if w.isActive == False :
#     w.activate()
#     w.maximize()

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

pyautogui.write("12345", interval=1)

pyautogui.sleep(1) 

w.restore()
    
# w.close() # 닫기

