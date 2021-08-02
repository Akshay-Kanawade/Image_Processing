import cv2
import numpy as np
import os

Dir = os.getcwd()
path = os.path.join(Dir, 'source')
images = os.listdir(path)

for file in images:
    filename = file.split('.')[0]
    image = cv2.imread(f"{path}/{file}")

    dst = cv2.filter2D(image, -1, (3, 3))

    cv2.imwrite(f"{os.path.join(Dir, 'target/filter')}/{filename}1.jpg", dst)
