import os
import scipy.signal as signal
import cv2
import numpy as np
def fun(path):
    files_mat = []
    for root, dirs, files in os.walk(path):
        for fn in files:
            files_mat.append(fn)
    return files_mat

def filt(img):
    image = cv2.imread(img, 0)
    kernel = np.ones((3, 3), np.uint8)
    erosion = cv2.erode(image, kernel, iterations = 2)  # 腐蚀
    dilation = cv2.dilate(erosion, kernel, iterations = 2)  # 膨胀
    cv2.imwrite(img[:-4] + '_f2.tif', dilation)

path = 'shi_img/add/a'
files_mat = fun(path)
for fl in files_mat:
    file_data = path + '/' + fl
    filt(file_data)