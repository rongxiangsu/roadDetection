import cv2
import numpy as np
import time

time_start=time.time()

def diff(img1, img2, res1, res2):
    #读取待差分图像
    data1 = cv2.imread(img1, 0)
    data2 = cv2.imread(img2, 0)
    #定义两幅空白图像
    image_arr1 = np.zeros((len(data1), len(data1[0])), np.uint8)
    image_arr2 = np.zeros((len(data1), len(data1[0])), np.uint8)
    for i in range(len(data1)) :
        for j in range(len(data1[0])) :
            if int(data1[i][j])-int(data2[i][j]) > 0:
                image_arr1[i][j] = 255
            elif int(data1[i][j])-int(data2[i][j]) < 0:
                image_arr2[i][j] = 255
            else:
                continue
    #出图
    cv2.imwrite(res1, image_arr1)
    cv2.imwrite(res2, image_arr2)

img1 = 'wh_img/2/wh0627u_main.tif'
img2 = 'wh_img/2/wh0704u_main.tif'
res1 = 'wh_img/wh062704u.tif'
res2 = 'wh_img/wh070427u.tif'
diff(img1, img2, res1, res2)

time_end=time.time()
print(time_end-time_start) 