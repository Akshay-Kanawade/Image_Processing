import cv2
import numpy as np
import os

Dir = os.getcwd()
path = os.path.join(Dir, 'source')
images = os.listdir(path)

for file in images:
    filename = file.split('.')[0]
    img = cv2.imread(f"{path}/{file}")
    #r, img = cv2.threshold(img, 120, 227, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(img, kernel, iterations=1)
    eroded = cv2.erode(img, kernel, iterations=1)
    opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite(f"{os.path.join(Dir, 'target/simple')}/{filename}1.jpg", closed)
    cv2.imwrite(f"{os.path.join(Dir, 'target/simple')}/{filename}2.jpg", dilated)
    cv2.imwrite(f"{os.path.join(Dir, 'target/simple')}/{filename}3.jpg", eroded)
    cv2.imwrite(f"{os.path.join(Dir, 'target/simple')}/{filename}4.jpg", opened)
