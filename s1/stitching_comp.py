import numpy as np
import cv2
import glob
import imutils

#image_paths = glob.glob('stit/*.png')
images = []
#image_paths = ['frames/11.png','frames/15.png','frames/19.png','frames/23.png','frames/27.png','frames/31.png','frames/34.png','frames/18.png']
image_paths = ['stit/300-400.png','stit/320-420.png']


print(image_paths)


for image in image_paths:
    img = cv2.imread(image)
    images.append(img)
    #cv2.imshow("Image", img)
    #cv2.waitKey(0)

print("hey")
imageStitcher = cv2.Stitcher_create(mode=1)

error, stitched_img = imageStitcher.stitch(images)
print(error)
if not error:
    cv2.imwrite("stitchedOutputfinal260above.png", stitched_img)
    #cv2.imshow("Stitched Img", stitched_img)
    #cv2.waitKey(0)

    print("hi")
    #cv2.waitKey(0)

else:
    print("Images could not be stitched!")
    print("Likely not enough keypoints being detected!")
