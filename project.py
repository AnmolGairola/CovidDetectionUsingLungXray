import cv2
from skimage import color
from skimage import io
import matplotlib.pyplot as plt #importing matplotlib
import numpy as np


covidList = []
normalList = []


limit = 0.04
for bruh in range(0,28):

    img = cv2.imread('C:\\Users\\hp\\Desktop\\College\\Sem5\\image processing\\project\\CovidDetectionUsingLungXray\\dataset\\normal\\'+str(bruh)+'.jpeg')
    img = color.rgb2gray(img)
    count = 0
    for i in img:
        for j in i:
            if(j < limit):
                count += 1
            
    #print(count, bruh)
    normalList.append(count)
    
#print(normalList)


for bruh in range(0,36):

    img = cv2.imread('C:\\Users\\hp\\Desktop\\College\\Sem5\\image processing\\project\\CovidDetectionUsingLungXray\\dataset\\covid\\'+str(bruh)+'.jpeg')
    img = color.rgb2gray(img)
    count = 0
    for i in img:
        for j in i:
            if(j < limit):
                count += 1
            
    #print(count, bruh)
    covidList.append(count)
    
#print(covidList)

listofones = [0] * len(covidList)
listofzeros = [0] * len(normalList)


lo = plt.scatter(covidList, listofones)
ll = plt.scatter(normalList, listofzeros)
lp = plt.scatter(min(normalList),0,s=50,c="red")



#test here -------------------------------------------------------------------

timg = cv2.imread('C:\\Users\\hp\\Desktop\\College\\Sem5\\image processing\\project\\CovidDetectionUsingLungXray\\dataset\\covid\\66.png')

testList = []
timg = color.rgb2gray(timg)

count = 0
for i in timg:
    for j in i:
        if(j < limit):
            count += 1
            
print(count, bruh)
testList.append(count)   

lk = plt.scatter(testList, 0, s=100) 
plt.legend((lo, ll, lp, lk),
           ('Covid positive', 'normal', 'separation point', 'Image'))

if testList[0] < min(normalList):
    print("Covid positive")

else:
    print("covid negative")
    
print(min(normalList))

    