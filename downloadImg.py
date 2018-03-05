import urllib.request


#tool

import os
import random
import time
import math


#获取url的文件名
def getfileName(url):
    return os.path.basename(url)


#tool end

#保存路径


def downloadImg(imgList,path,savePath):

    i = 0
    imglen = len(list)
    pathUrl = np.where(path,path,'')
    dirPath = np.where(savePath,savePath,'images/')

    for x in range(imglen):

        tname = imgList[x].name

        ranName = 'img'+ str(random.random()*100)+str( math.floor(time.time)) 

        imgNmame = np.where(tname, tname, ranName)

        fullPath = pathUrl + imgNmame

        response = urllib.request.urlopen(fullPath)
        cat_img = response.read()

        saveimgName = getfileName(fullPath)

        saveName = dirPath + 
 
        with open('123.jpg','wb') as f:
            f.write(cat_img)
