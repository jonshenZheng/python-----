import urllib.request


#tool

import os,sys
import random
import time
import math


imgUrl = ['000.jpg','001.jpg','002.jpg','003.jpg','004.jpg']
baseUrl = 'http://localhost/testimg/'
saveUrl = 'images/'


#获取url的文件名
def getfileName(url):
    return os.path.basename(url)


#tool end

#保存路径


def downloadImg(imgList=[],pathUrl='',dirPath='',randomNane=False):

    i = 0
    imglen = len(imgList)

    for x in range(imglen):

        tname = imgList[x]

        rTime = int(time.time())

        rNumber = random.random()*100

        ranName = 'img'+ str(rNumber)+str(rTime)

        if(tname):
            imgNmame = tname
        else:
            imgNmame = ranName

        fullPath = pathUrl + imgNmame

        #如果你在C:\test目录下执行python getpath\getpath.py，那么os.getcwd()会输出“C:\test”，sys.path[0]会输出“C:\test\getpath”

        cwdPath = os.getcwd()

        #检测存储图片目录存不存在
        if not os.path.exists(dirPath):
            #0755是什么意思不知道？  十进制为777 第一个7是所有者的权限。第二个是文件所属组的权限，第三个是其他人的权限。 r=4, w=2, x=1 代表 读、写、执行    
            os.mkdir( dirPath )
            
        else:
            #判断有没有读写权限
            pass
            
        response = urllib.request.urlopen(fullPath)
        cat_img = response.read()

        saveimgName = getfileName(fullPath)

        saveName = dirPath + saveimgName
 
        with open(saveName,'wb') as f:
            f.write(cat_img)


downloadImg(imgUrl,baseUrl,saveUrl)
