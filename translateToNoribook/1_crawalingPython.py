import os 
import requests 
from bs4 import BeautifulSoup as bs 
from nltk.tokenize import sent_tokenize
import pickle
from selenium import webdriver

url = "https://novelfull.com/super-gene/chapter-1-supergene.html"
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
with open("소설/supergeneEng/"+pathAndName2+".txt", 'w') as fp:
    for item in content:
        fp.write("%s\n" % item)
    print('Done')


#번역가 문장 삭제 후 문단 바꾸기
new_text_content = ''
with open("소설/supergeneEng/"+pathAndName2+".txt", "r") as f:
    lines = f.readlines()
    for i, l in enumerate(lines):
        new_string = l.strip().replace("Translator: Nyoi-Bo Studio  Editor: Nyoi-Bo Studio",".\n")
        if new_string:
            new_text_content += new_string + '\n'
        else:
            new_text_content += '\n'
                
with open("소설/supergeneEng/"+pathAndName2+".txt",'w') as fp:
    fp.write(new_text_content)

# os.system('cls')
