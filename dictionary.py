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

#
#def createword():
#    form="%Y-%m-%d %X"
#    hr="========"
#    f=open("word.txt", 'a', encoding='utf-8')
#    f.write('\n' + word)
#    f.close()
#

print("===============================\n=Youdao Dictionary 「Command Line Version」=\n===============================\n")
print("输入'q'可退出程式\n")
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
            print("Spell wrong? Can not find it, please try agian")
