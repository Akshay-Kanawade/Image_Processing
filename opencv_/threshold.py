import cv2
import numpy as np
import os

Dir = os.getcwd()
path = os.path.join(Dir, 'source')
images = os.listdir(path)

for file in images:
    filename = file.split('.')[0]
    img = cv2.imread(f"{path}/{file}", 0)
    _, th1 = cv2.threshold(img, 110, 185, cv2.THRESH_BINARY)
    _, th2 = cv2.threshold(img, 90, 195, cv2.THRESH_TRUNC)
    _, th3 = cv2.threshold(img, 171, 255, cv2.THRESH_BINARY_INV)
    _, th4 = cv2.threshold(img, 255, 255, cv2.THRESH_MASK)
    cv2.imwrite(f"{os.path.join(Dir, 'target/threshold')}/{filename}4.jpg", th4)


