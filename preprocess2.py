import pandas as pd
import cv2
import time
import gc
import numpy as np
import os
import math
from operator import itemgetter
time_start=time.time()

def getAngle(x1, x2, y1, y2):
    if y2 == y1:
        if x2 > x1:
            a = 90
        elif x1 > x2:
            a = 270
        else:
            a = -1
    else:
        a = math.atan((x2 - x1)/(y2 - y1))* 180 /math.pi
        if y1 > y2:
            a = a + 180
        elif x1 > x2:
            a = a + 360
    return a

def pre(file, fl):
    img_main = cv2.imread('sjz_m_c14.tif', 0)
    img_matum = cv2.imread('shi000.tif', 0)
    img_matdm = cv2.imread('shi000.tif', 0)
    img_mats = cv2.imread('shi000.tif')
    mat = pd.read_csv(file, header = None, usecols=[0, 1, 2, 5, 6], chunksize=10000000)
    for chunk in mat:
        chunk = chunk.values
        try :
            chunk = sorted(chunk, key=itemgetter(0,3))
            for i in range(len(chunk)):
                
                    if chunk[i][0]==chunk[i+1][0] and chunk[i][4]<9 and chunk[i+1][4]<10 and (114.375< chunk[i][1] <= 114.62499)and (38.0 < chunk[i][2] <= 38.16666):
                        x1 = int(round((chunk[i][1] - 114.375)*27830))
                        y1 = 4639 - int(round((chunk[i][2]-38.0)*27830))
                        x2 = int(round((chunk[i+1][1] - 114.375)*27830))
                        y2 = 4639 - int(round((chunk[i+1][2]-38.0)*27830))
                        if 0 < (chunk[i+1][3] - chunk[i][3]) <= 10 and 0 < (np.square(x1 - x2) + np.square(y1 - y2)) < np.square(25*(chunk[i+1][3] - chunk[i][3])):
                            if img_main[y1][x1] > 0:
                                ang = getAngle(chunk[i][1], chunk[i+1][1], chunk[i][2], chunk[i+1][2])
                                if 0 <= ang < 180:
                                    img_matum[y1][x1] = 255
                                elif 180 <= ang < 360:
                                    img_matdm[y1][x1] = 255
                                else:
                                    continue
                            elif img_main[y2][x2] == 0:
                                cv2.line(img_mats, (x1, y1), (x2, y2), (255, 255, 255), 1)                   
                            else:
                                continue
                        else:
                            continue            
                    else:
                        continue
        except Exception:
            pass
    
    cv2.imwrite('shi_img/shi' + fl + 'u_main.tif', np.array(img_matum))
    cv2.imwrite('shi_img/shi' + fl + 'd_main.tif', np.array(img_matdm))
    cv2.imwrite('shi_img/shi' + fl + '_side.tif', np.array(img_mats))

def fun(path):
    files_mat = []
    for root, dirs, files in os.walk(path):
        for fn in files:
            files_mat.append(fn)
    return files_mat

path = 'g:/shijiazhuang_liuan/shijiazhuang'
files_mat = fun(path)
for fl in files_mat:
    file_data = path + '/' + fl
    pre(file_data,fl[-4:] )

time_end1=time.time()
print(time_end1-time_start)