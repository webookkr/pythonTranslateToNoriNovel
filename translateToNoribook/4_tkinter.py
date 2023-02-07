import os
import tkinter.ttk as ttk
from tkinter import *
from classTrans import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import requests 
from bs4 import BeautifulSoup as bs 
from nltk.tokenize import sent_tokenize
from webdriver_manager.chrome import ChromeDriverManager
import keyboard


root = Tk()
root.title("노리 번역")
root.geometry("1840x1280+50+50") # 가로 * 세로
root.resizable(True, True) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)


def getChrome(): 
    # 현재 url 얻기 -> chrome driver
    global driver
    driver = webdriver.Chrome()
    # 크롬 드라이버 자동 업데이트

        # 브라우저 꺼짐 방지
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
        # 불필요한 에러 메시지 없애기
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
        # 웹페이지 해당 주소 이동
    driver.get("https://www.naver.com")
    print("크롬 로딩")
    




main_frame = Frame(root)
main_frame.pack(fill="both", padx=5, pady=5)

# 번역 창
trans_frame = Frame(main_frame)
trans_frame.pack(side="left")

# 한글 문단 나눠서
correct_frame = (main_frame)
correct_frame.pack(side="right")

# 번역 창 : 영어 _ 버튼(번역, 폴더리스트, 불러오기:기본은 자식(eng))_ 한글 _ 버튼(폴더리스트, 저장하기 :기본은 자식(kor))
eng_frame = Frame(trans_frame)
eng_frame.pack()

scrollbar1 = Scrollbar(eng_frame)
scrollbar1.pack(side="right", fill="y")

eng_txt = Text(eng_frame, font=("Arial", 10), yscrollcommand=scrollbar1.set, width=130, height=30)
eng_txt.pack(side="left",padx=5, pady=10)
scrollbar1.config(command=eng_txt.yview)

# 버튼창
path_frame1 = LabelFrame(trans_frame, text="저장경로")
path_frame1.pack(fill="x", padx=5, pady=5, ipady=5)

btn_trans = Button(path_frame1, text="번역", width=10)
btn_trans.pack(side="left", padx=5, pady=5)

txt_dest_path1 = Entry(path_frame1)
txt_dest_path1.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경

btn_scan1 = Button(path_frame1, text="소설찾기", width=10, command=getChrome) # 콜백시 인자x, ()x : 함수 가질시 바로 실행됨
btn_scan1.pack(side="right", padx=5, pady=5)

btn_scan2 = Button(path_frame1, text="스캔하기", width=10, command="1") # 콜백시 인자x, ()x : 함수 가질시 바로 실행됨
btn_scan2.pack(side="right", padx=5, pady=5)

btn_save1 = Button(path_frame1, text="저장하기", width=10)
btn_save1.pack(side="right", padx=5, pady=5)

btn_dest_path1 = Button(path_frame1, text="찾아보기", width=10)
btn_dest_path1.pack(side="right", padx=5, pady=5)

# 한국어
kor_frame = Frame(trans_frame)
kor_frame.pack()

scrollbar2 = Scrollbar(kor_frame)
scrollbar2.pack(side="right", fill="y")

kor_txt = Text(kor_frame, font=("Arial", 10), yscrollcommand=scrollbar2.set, width=130, height=30)
kor_txt.pack(side="left",padx=5, pady=10)
scrollbar2.config(command=kor_txt.yview)

# 버튼창
path_frame2 = LabelFrame(trans_frame, text="저장경로")
path_frame2.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path2 = Entry(path_frame2)
txt_dest_path2.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경

btn_save2 = Button(path_frame2, text="저장하기", width=10)
btn_save2.pack(side="right", padx=5, pady=5)

btn_dest_path2 = Button(path_frame2, text="찾아보기", width=10)
btn_dest_path2.pack(side="right", padx=5, pady=5)

# 오른쪽 한글 번역 교정을 위한 창
cor1_frame = LabelFrame(correct_frame, text="교정1")
cor1_frame.pack()

cor1_txt = Text(cor1_frame, font=("Arial", 10), width=130, height=5)
cor1_txt.pack(padx=5, pady=10)

btn_frame1 = Frame(cor1_frame)
btn_frame1.pack()

btn_copy1 = Button(btn_frame1, text="복사", width=6)
btn_copy1.pack(side='left', padx=5, pady=3)

btn_paste1 =  Button(btn_frame1, text="붙여넣기", width=6)
btn_paste1.pack(side='right', padx=5, pady=3)

# 교정2
cor2_frame = LabelFrame(correct_frame, text="교정2")
cor2_frame.pack()

cor2_txt = Text(cor2_frame, font=("Arial", 10), width=130, height=5)
cor2_txt.pack(padx=5, pady=10)

btn_frame2 = Frame(cor2_frame)
btn_frame2.pack()

btn_copy2 = Button(btn_frame2, text="복사", width=6)
btn_copy2.pack(side='left', padx=5, pady=3)

btn_paste2 =  Button(btn_frame2, text="붙여넣기", width=6)
btn_paste2.pack(side='right', padx=5, pady=3)

# 교3
cor3_frame = LabelFrame(correct_frame, text="교정3")
cor3_frame.pack()

cor3_txt = Text(cor3_frame, font=("Arial", 10), width=130, height=5)
cor3_txt.pack(padx=5, pady=10)

btn_frame3 = Frame(cor3_frame)
btn_frame3.pack()

btn_copy3 = Button(btn_frame3, text="복사", width=6)
btn_copy3.pack(side='left', padx=5, pady=3)

btn_paste3 =  Button(btn_frame3, text="붙여넣기", width=6)
btn_paste3.pack(side='right', padx=5, pady=3)


# 교정4
cor4_frame = LabelFrame(correct_frame, text="교정4")
cor4_frame.pack()

cor4_txt = Text(cor4_frame, font=("Arial", 10), width=130, height=5)
cor4_txt.pack(padx=5, pady=10)

btn_frame4 = Frame(cor4_frame)
btn_frame4.pack()

btn_copy4 = Button(btn_frame4, text="복사", width=6)
btn_copy4.pack(side='left', padx=5, pady=3)

btn_paste4 =  Button(btn_frame4, text="붙여넣기", width=6)
btn_paste4.pack(side='right', padx=5, pady=3)


# 교정5
cor5_frame = LabelFrame(correct_frame, text="교정5")
cor5_frame.pack()

cor5_txt = Text(cor5_frame, font=("Arial", 10), width=130, height=5)
cor5_txt.pack(padx=5, pady=10)

btn_frame5 = Frame(cor5_frame)
btn_frame5.pack()

btn_copy5 = Button(btn_frame5, text="복사", width=6)
btn_copy5.pack(side='left', padx=5, pady=3)

btn_paste5 =  Button(btn_frame5, text="붙여넣기", width=6)
btn_paste5.pack(side='right', padx=5, pady=3)


# 교정6
cor6_frame = LabelFrame(correct_frame, text="교정6")
cor6_frame.pack()

cor6_txt = Text(cor6_frame, font=("Arial", 10), width=130, height=5)
cor6_txt.pack(padx=5, pady=10)

btn_frame6 = Frame(cor6_frame)
btn_frame6.pack()

btn_copy6 = Button(btn_frame6, text="복사", width=6)
btn_copy6.pack(side='left', padx=5, pady=3)

btn_paste6 =  Button(btn_frame6, text="붙여넣기", width=6)
btn_paste6.pack(side='right', padx=5, pady=3)

# 교정7
cor7_frame = LabelFrame(correct_frame, text="교정7")
cor7_frame.pack()

cor7_txt = Text(cor7_frame, font=("Arial", 10), width=130, height=5)
cor7_txt.pack(padx=5, pady=10)

btn_frame7 = Frame(cor7_frame)
btn_frame7.pack()

btn_copy7 = Button(btn_frame7, text="복사", width=6)
btn_copy7.pack(side='left', padx=5, pady=3)

btn_paste7 =  Button(btn_frame7, text="붙여넣기", width=6)
btn_paste7.pack(side='right', padx=5, pady=3)


# 버튼창
file_frame = LabelFrame(correct_frame, text="파일저장")
file_frame.pack(fill="x", padx=5, pady=5, ipady=5)

btn_correct = Button(file_frame, text="가져오기", width=10)
btn_correct.pack(side="left", padx=5, pady=5)

txt_dest_path3 = Entry(file_frame)
txt_dest_path3.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경

btn_scan3 = Button(file_frame, text="끌어오기", width=10)
btn_scan3.pack(side="right", padx=5, pady=5)

btn_dest_path3 = Button(file_frame, text="찾아보기", width=10)
btn_dest_path3.pack(side="right", padx=5, pady=5)



root.mainloop()