import cv2
import numpy as np
import os

Dir = os.getcwd()
path = os.path.join(Dir, 'source')
images = os.listdir(path)

for file in images:
    filename = file.split('.')[0]
    image = cv2.imread(f"{path}/{file}", 0)
    blur = cv2.blur(image, (7, 7))
    G_blur = cv2.GaussianBlur(blur, (5, 5), 0)
    median = cv2.medianBlur(blur, 5)
    B_blur = cv2.bilateralFilter(blur, 15, 75, 75)

    cv2.imwrite(f"{os.path.join(Dir, 'target/blur')}/{filename}1.jpg", blur)
    cv2.imwrite(f"{os.path.join(Dir, 'target/blur')}/{filename}2.jpg", median)
    cv2.imwrite(f"{os.path.join(Dir, 'target/blur')}/{filename}3.jpg", B_blur)
    cv2.imwrite(f"{os.path.join(Dir, 'target/blur')}/{filename}4.jpg", G_blur)
