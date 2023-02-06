import pyautogui

#스크린샷 찍기 
img = pyautogui.screenshot()
img.save("screenshot.png")

# pyautogui.mouseInfo()

# 877,258 255,255,255 #FFFFFF

pixel = pyautogui.pixel(877,258)
print(pixel)

print(pyautogui.pixelMatchesColor(877,258,(255,255,165)))

