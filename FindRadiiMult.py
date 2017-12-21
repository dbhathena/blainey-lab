import cv2
import numpy as np
import argparse
import os

from PIL import Image
from resizeimage import resizeimage


def get_diameters(path, minR, maxR):
    """
    Parameters: a path to the directory containing images, and the minimum and maximum radii expected in the images
    Creates a text file that relates file name to average circle size within that image
    """

    file_names = os.listdir(path)

    for file_name in file_names:
        try:
            name_file = path + "/" + file_name
            img = cv2.imread(name_file,0)
            img = cv2.medianBlur(img,5)
            cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

            circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,0.5, 100,
                                        param1=50,param2=30,minRadius=minR,maxRadius=maxR)

            circles = np.uint16(np.around(circles))

            radii = np.array([])

            for i in circles[0,:]:
                radii = np.append(radii, i[2])
                # draw the outer circle
                cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
                # draw the center of the circle
                cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

            avg = np.mean(radii)
            diameter_averages = open(path + "/Diameter Averages", 'a')
            diameter_averages.write(str(file_name[:-4]) + ': ' + str(2*avg) + '\n')
            diameter_averages.close()
            #cv2.imwrite('detected circles.png', cimg)
            #cv2.imshow('detected circles',cimg)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
        except:
            pass


path = "/Users/Darian/School/MIT/Freshman Year/IAP/UROP/Microscopy/2017_1_18"
minR = 50
maxR = 150

get_diameters(path, minR, maxR)

