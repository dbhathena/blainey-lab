import cv2
import numpy as np
import argparse

from PIL import Image
from resizeimage import resizeimage

name_file = 'SampleNav_3.tif'

img = cv2.imread(name_file,0)
#cv2.imshow('image test', img)
#img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,0.5, 100,
                            param1=50,param2=30,minRadius=50,maxRadius=150)

circles = np.uint16(np.around(circles))

radii = np.array([])

for i in circles[0,:]:
    radii = np.append(radii, i[2])
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

avg = np.mean(radii)
radii_averages = open('Radii Averages', 'a')
radii_averages.write(str(name_file) + ': ' + str(avg) + '\n')
radii_averages.close()


#cv2.imwrite('detected circles.png', cimg)
#cv2.imshow('detected circles',cimg)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

