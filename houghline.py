import cv2
import numpy as np
import skimage.transform as st
import pandas as pd
import os
def fun(path):
    files_mat = []
    for root, dirs, files in os.walk(path):
        for fn in files:
            files_mat.append(fn)
    return files_mat
def hough(data_img):
    img = cv2.imread(data_img, 0)
    image = cv2.imread('wh_img/2/wh0627u_main.tif')
    # edges = cv2.Canny(img, 50, 150, apertureSize=3)
    minLineLength = 50
    maxLineGap = 30
    lines = cv2.HoughLinesP( img, 1.0, np.pi/180,30, 100, minLineLength,maxLineGap)
    line_csv = []
    print(type(lines))
    try:
        print(len(lines))
        for line in lines:
            x1, y1, x2, y2 = line[0]
            lo1 = x1/27830 + 114.375
            la1 = (4639 - y1)/27830 + 38.0
            lo2 = x2/27830 + 114.375
            la2 = (4639 - y2)/27830 + 38.0
            line_csv.append([lo1, la1, lo2, la2])
            cv2.line(image,(x1, y1),(x2, y2),(0,0,255),5)
        cv2.imwrite(data_img[:-4] + 'sg0.tif', image) 
        line_csv = pd.DataFrame(line_csv)
        line_csv.to_csv(data_img[:-4] + 'sg0', index=False, header=None)
    except TypeError:
        pass

path = 'wh_img/f'
files_mat = fun(path)
for fl in files_mat:
    file_data = path + '/' + fl
    # print(fl[-2:])
    hough(file_data)
