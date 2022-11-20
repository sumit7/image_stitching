import numpy as np
import cv2
import glob
import imutils

#image_paths = glob.glob('frames/11*.png')

e = 0
for a in range(0,100,20):
    images = []
    image_paths = []
    print(a)
    b = a+100
    c = 1
    d = f"{a}"+"-"+f"{b}"
    for i in range(a,b,c):
        image_paths.append('frames/'+f"{i}"+".png")


    for image in image_paths:
        img = cv2.imread(image)
        images.append(img)
    
    imageStitcher = cv2.Stitcher_create(mode=1)

    error, stitched_img = imageStitcher.stitch(images)
    print(error)
    if not error:
        cv2.imwrite('stit/'+f"{d}"+".png", stitched_img)
    
    else:
        print("Images could not be stitched!")
        print("Likely not enough keypoints being detected!"+f"{d}")
