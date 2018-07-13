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
    data=cv2.imread(img, 0)
    image_arr = signal.medfilt2d(data, kernel_size = 5)
    cv2.imwrite(img[:-4] + '_f2.tif', image_arr)

path = 'wh_img/dif/d'
files_mat = fun(path)
for fl in files_mat:
    file_data = path + '/' + fl
    # print(fl[-2:])
    filt(file_data)