import cv2
from skimage import color
from skimage import io
import matplotlib.pyplot as plt #importing matplotlib
import numpy as np

# Save image in set directory
# Read RGB image
#img = cv2.imread('C:\\Users\\hp\\Desktop\\College\\Sem5\\image processing\\project\\dataset\\covid\\covid (2).jpeg') 


covidList = []
normalList = []

limit = 0.04
for bruh in range(0,28):

    img = cv2.imread('C:\\Users\\hp\\Desktop\\College\\Sem5\\image processing\\project\\dataset\\normal\\'+str(bruh)+'.jpeg')
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

    img = cv2.imread('C:\\Users\\hp\\Desktop\\College\\Sem5\\image processing\\project\\dataset\\covid\\'+str(bruh)+'.jpeg')
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

#np.savetxt('C:\\Users\\hp\\Desktop\\College\\Sem5\\image processing\\project\\dataCovid.csv', (covidList, listofones), delimiter=',')
#np.savetxt('C:\\Users\\hp\\Desktop\\College\\Sem5\\image processing\\project\\dataNormal.csv', (normalList, listofzeros), delimiter=',')

plt.scatter(covidList, listofones)
plt.scatter(normalList, listofzeros)

#plt.hist(img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k') #calculating histogram

# Output img with window name as 'image'
#cv2.imshow('image', img) 
  
# Maintain output window utill
# user presses a key
#cv2.waitKey(0)        
  
# Destroying present windows on screen
#cv2.destroyAllWindows() 