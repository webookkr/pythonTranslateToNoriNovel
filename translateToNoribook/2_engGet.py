import os 
import requests 
from bs4 import BeautifulSoup as bs 
from nltk.tokenize import sent_tokenize
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import classTrans.chromeCall
import keyboard


# 현재 url 얻기 -> chrome driver
driver = webdriver.Chrome()
# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager
# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
# 웹페이지 해당 주소 이동

# print(driver.current_url)


def getNovel():
    url = newUrl
    response = requests.get(url)
    response.raise_for_status()

    soup = bs(response.text, "html.parser")
    content_text = soup.find("div", id="chapter-content")
    content = sent_tokenize(content_text.text)


    # nltk 생성시 리스트 마지막에 나오는 문장 삭제 
    r = "If you find any errors ( broken links, non-standard content, etc.. ), Please let us know < report chapter > so we can fix it as soon as possible."

    content.remove(r)

    #  1: Supergene
    pathAndName = content[0][8:content[0].find("T")]
    pathAndName2 = pathAndName.replace(': ', ".")
    print(pathAndName2)


    # nltk 리스트 형태를 text라인 형태로 저장하기
    with open("소설/supergeneEng/"+pathAndName2+".txt", 'w', encoding='utf-8') as fp:
        for item in content:
            fp.write("%s\n" % item)
        print('Done')


    #번역가 문장 삭제 후 문단 바꾸기
    new_text_content = ''
    with open("소설/supergeneEng/"+pathAndName2+".txt", "r", encoding='utf-8') as f:
        lines = f.readlines()
        for i, l in enumerate(lines):
            new_string = l.strip().replace("Translator: Nyoi-Bo Studio  Editor: Nyoi-Bo Studio",".\n")
            if new_string:
                new_text_content += new_string + '\n'
            else:
                new_text_content += '\n'
                    
    with open("소설/supergeneEng/"+pathAndName2+".txt",'w', encoding='utf-8') as fp:
        fp.write(new_text_content)

    # os.system('cls')

#  키보드 클릭시 소설 가져오기 메소드 -> 버튼 클릭시 메소드로 변경 예정 
while True: 
    if keyboard.is_pressed("1"):
        print(driver.current_url)
        newUrl = driver.current_url
        getNovel()
        



# url = newUrl
# response = requests.get(url)
# response.raise_for_status()

# soup = bs(response.text, "html.parser")
# content_text = soup.find("div", id="chapter-content")
# content = sent_tokenize(content_text.text)


# # nltk 생성시 리스트 마지막에 나오는 문장 삭제 
# r = "If you find any errors ( broken links, non-standard content, etc.. ), Please let us know < report chapter > so we can fix it as soon as possible."

# content.remove(r)

# #  1: Supergene
# pathAndName = content[0][8:content[0].find("T")]
# pathAndName2 = pathAndName.replace(': ', ".")
# print(pathAndName2)


# # nltk 리스트 형태를 text라인 형태로 저장하기
# with open("소설/supergeneEng/"+pathAndName2+".txt", 'w') as fp:
#     for item in content:
#         fp.write("%s\n" % item)
#     print('Done')


# #번역가 문장 삭제 후 문단 바꾸기
# new_text_content = ''
# with open("소설/supergeneEng/"+pathAndName2+".txt", "r") as f:
#     lines = f.readlines()
#     for i, l in enumerate(lines):
#         new_string = l.strip().replace("Translator: Nyoi-Bo Studio  Editor: Nyoi-Bo Studio",".\n")
#         if new_string:
#             new_text_content += new_string + '\n'
#         else:
#             new_text_content += '\n'
                
# with open("소설/supergeneEng/"+pathAndName2+".txt",'w') as fp:
#     fp.write(new_text_content)

# # os.system('cls')

# class chromeDriver : 
#     def getChrome (self): 
#         # 현재 url 얻기 -> chrome driver
#         driver = webdriver.Chrome()
#         # 크롬 드라이버 자동 업데이트
#         from webdriver_manager.chrome import ChromeDriverManager
#         # 브라우저 꺼짐 방지
#         chrome_options = Options()
#         chrome_options.add_experimental_option("detach", True)
#         # 불필요한 에러 메시지 없애기
#         chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
#         service = Service(executable_path=ChromeDriverManager().install())
#         driver = webdriver.Chrome(service=service, options=chrome_options)
#         # 웹페이지 해당 주소 이동
#         # driver.get("https://www.naver.com")