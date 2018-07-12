import requests
import bs4
import os
import time
import sys

def createlog():
    form="%Y-%m-%d %X"
    hr="========"
    f=open("log.txt", 'a', encoding='utf-8')
    f.write('\n'+hr+'\n'+time.strftime(form,time.localtime())+'\n'+hr)
    f.close()

def createword():
    form="%X"
    hr="========"
    f=open("word.txt", 'a', encoding='utf-8')
    f.write(word+'\n')
    f.close()

print("===============================\n=Youdao Dictionary 「Command Line Version」=\n===============================\n")
print("press'q'to quit.\n")
createlog()
while True:
    rooturl='http://www.youdao.com/w/'
    url=input("type your word：")
    f=open("log.txt", 'a', encoding='utf-8')
    if url=="q":
        print("log stored, see ya! ")
        f.close()
        sys.exit()
    else:
        finurl=rooturl+url
        headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36')
        res={}
        try:
            response = requests.get(finurl)
            soup = bs4.BeautifulSoup(response.text,'html.parser')
            word=soup.select('.keyword')[0].get_text()
            tran=soup.select('.trans-container > ul > li')[0].get_text()
            print('Translate:'+tran)
            res['word']=word
            res['Translation']=tran
            f.write('\n'+str(res))
            f.close()
        except IndexError:
            print("Spell wrong? Can not find it, please try again")

        print("Press 's' to store the word.\nor,press 'c' to start next inquiry.")
        url2=input("")
        if url2=="s":
            createword()
            f=open("word.txt", 'a', encoding='utf-8')
            print("word stored !")
            f.close()
            continue
        if url2=="c":
            continue
