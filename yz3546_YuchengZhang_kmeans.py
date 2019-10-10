from cv2 import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

path = "" 
img_filePath= os.path.join(path, "img/face_d2.jpg") 
img_color= cv2.imread(img_filePath) 
img_RGB= cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB) 
plt.imshow(img_RGB)

#This is just a test part, def function in the bottom
"""
#test part
r, g, b = cv2.split(img_color)
r,g,b = r.flatten(),g.flatten(),b.flatten()
rsig,gsig,bsig = r.std(),g.std(),b.std()

centroid = [np.random.uniform(0,255,3) for i in range(3)]#change 3 to k
len(centroid)

label = [0]*len(r)
print(label)
change = 1
while change:
    pre = label[:]
    #assign all points to the nearst centroid point.
    for pixel in range(len(r)):
        mindis = 0.0
        for group in range(len(centroid)):
            temp = ((r[pixel]-centroid[group][0])/rsig)**2 + ((g[pixel]-centroid[group][1])/gsig)**2 + ((b[pixel]-centroid[group][2])/gsig)**2
            if (mindis == 0) or (temp < mindis):
                mindis = temp
                label[pixel] = group
    #calculate the new mean to the centroid
    label_count = 0
    while label_count < len(centroid):
        t_r,t_g,t_b,count = 0,0,0,0
        for p in range(len(r)):
            if label[p] == label_count:
                t_r += r[p]
                t_g += g[p]
                t_b += b[p]
                count += 1
        centroid[label_count][0] = t_r/count
        centroid[label_count][1] = t_g/count
        centroid[label_count][2] = t_b/count
        label_count += 1
    if pre == label:
        change = 0

center = np.uint8(centroid)
res = center[label]
res2 = res.reshape((img_color.shape))
plt.imshow(res2)
print(res2)
print(type(res2))
cv2.findContours(img_color,cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
"""

#The k-means function is defined here, return the label and center details.
def yz3546_YuchengZhang_kmeans(filepath = "img/face_d2.jpg",k=4):
    img_color= cv2.imread(filepath)
    r, g, b = cv2.split(img_color)
    r,g,b = r.flatten(),g.flatten(),b.flatten()
    rsig,gsig,bsig = r.std(),g.std(),b.std()

    #set the centroid,label space
    centroid = [np.random.uniform(0,255,3) for i in range(k)]
    label = [0]*len(r)
    change = 1
    while change:
        #first we save the initial label
        pre = label[:]
        #assign all points to the nearst centroid point.
        for pixel in range(len(r)):
            mindis = 0.0
            #compare the distance of this point to center over k centers 
            for group in range(len(centroid)):
                temp = ((r[pixel]-centroid[group][0])/rsig)**2 + ((g[pixel]-centroid[group][1])/gsig)**2 + ((b[pixel]-centroid[group][2])/bsig)**2
                #if we find a closer center, we save it.
                if (mindis == 0) or (temp < mindis):
                    mindis = temp
                    label[pixel] = group
        #calculate the new mean to set the new centroid
        label_count = 0
        while label_count < len(centroid):
            t_r,t_g,t_b,count = 0,0,0,0
            for p in range(len(r)):
                if label[p] == label_count:
                    t_r += r[p]
                    t_g += g[p]
                    t_b += b[p]
                    count += 1
            if count != 0:
                centroid[label_count][0] = t_r/count
                centroid[label_count][1] = t_g/count
                centroid[label_count][2] = t_b/count
            label_count += 1
        if pre == label:#no change in this loop, so we end it.
            change = 0
    center = np.uint8(centroid)
    return(label,center)


#it takes really long time to run..
label,center = yz3546_YuchengZhang_kmeans('img/','face_d2.jpg', k=8)
len(label)
center
res = center[label]
res2 = res.reshape((img_color.shape))
plt.imshow(res2)
plt.imshow(img_color)
#we then locate the boundary
res[250*110 + 125]
label[250*70 + 125]
#we find out that the sixth group
#[156,171,212]represents the face color
for i,j in enumerate(label):
    if (i > 250*50 and i%250 > 75) and j == 6 :
        print(i)#we find the left upper point
        leftupper = i
        break
# I got the result of of upper left point as 12576: (76,50)
leftupper = 12576
bottom = (175,175)
# and we locate the right bottom point by hand
path = "" 
img_filePath= os.path.join(path, "img/face_d2.jpg") 
img_color= cv2.imread(img_filePath) 
img_RGB= cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB) 
rect = cv2.rectangle(img_RGB,(leftupper%250,leftupper//250),bottom,(255,0,0),2)
#we plot the result
plt.imshow(rect)


