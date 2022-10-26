from skimage.metrics import structural_similarity 
import cv2
import os
import imutils
import numpy as np
%matplotlib auto

vidcap = cv2.VideoCapture(r"C:\Users\Sam\Downloads\studio_vid.MP4")

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        print('Success')
        path = r"C:\Users\Sam\Downloads"
        cv2.imwrite(os.path.join(path,"studio_vid"+str(count)+".jpg"), image) # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 1 #//capture image in each second
count=1
success = getFrame(sec)
while count < 5:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

path1 = r'C:\Users\badge\OneDrive - Virginia Tech\Virginia Tech\2021-2022\Studio\PRR\SpotDiffBWStart.png'
image1 = cv2.imread(path1)

path2 = r'C:\Users\badge\OneDrive - Virginia Tech\Virginia Tech\2021-2022\Studio\PRR\SpotDiffBWEnd.png'
image2 = cv2.imread(path2)

# compute difference
difference = cv2.subtract(image1, image2)

# color the mask red
Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(Conv_hsv_Gray, (7, 7), 0)
#thresh = cv2.adaptiveThreshold(blurred, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10)
ret, mask = cv2.threshold(blurred, 200, 255,cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
#cv2.imshow("Mean Adaptive Thresholding", thresh)
difference[mask != 255] = [0, 10, 255]

# add the red mask to the images to make the differences obvious
image1[mask != 255] = [0, 0, 255]
image2[mask != 255] = [0, 0, 255]

# store images
path = r"C:\Users\badge\OneDrive - Virginia Tech\Virginia Tech\2021-2022\Studio\PRR"
cv2.imwrite(os.path.join(path,'diffOverImage1BW.png'), image1)
#cv2.imwrite(os.path.join(path,'diffOverImage2.png'), image1)
cv2.imwrite(os.path.join(path,'diffBW.png'), difference)
cv2.imwrite('diffBW.png', difference)

diff_path = r'C:\Users\badge\OneDrive - Virginia Tech\Virginia Tech\2021-2022\Studio\PRR\diffBW.png'
overlay_path = r'C:\Users\badge\OneDrive - Virginia Tech\Virginia Tech\2021-2022\Studio\PRR\diffOverImage1BW.png'
diff = cv2.imread(diff_path)
overlay = cv2.imread(overlay_path)
cv2.imshow("Difference", diff)
cv2.imshow("Overlay", overlay)