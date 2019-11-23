import zipfile
from threading import Thread

def crackFile(zFile,word):
    try:
        zFile.extractall(pwd=word)
        print('Cracked:'+word)
    except Error as e:
        print(e)

def main():
    zFile=zipfile.zipfile('pass.zip')
    wordlist=open('usr/share/wordlists.txt','r')
    for word in wordlist.readlines:
        t=Thread(target=crackFile,args=(zFile,word))
        t.start()


if __name__=='__main__':
    main()

