import urllib.request


#tool

import os
import random
import time
import math


imgUrl = ['000.jpg','001.jpg','002.jpg','003.jpg','004.jpg']


#获取url的文件名
def getfileName(url):
    return os.path.basename(url)


#tool end

#保存路径


def downloadImg(imgList=[],pathUrl='',dirPath=''):

    i = 0
    imglen = len(imgList)

    for x in range(imglen):

        tname = imgList[x]

        rTime = int(time.time)

        rNumber = random.random()*100

        ranName = 'img'+ str(rNumber0)+str(rTime)

        if(tname):
            imgNmame = tname
        else:
            imgNmame = ranName

        fullPath = pathUrl + imgNmame

        response = urllib.request.urlopen(fullPath)
        cat_img = response.read()

        saveimgName = getfileName(fullPath)

        saveName = dirPath + saveimgName
 
        with open(saveName,'wb') as f:
            f.write(cat_img)


downloadImg(imgUrl,'http://localhost/testimg/','images')
