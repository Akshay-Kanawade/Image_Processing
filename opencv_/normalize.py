import cv2
import os

import numpy as np

Dir = os.getcwd()
path = os.path.join(Dir, 'source')
images = os.listdir(path)

for file in images:
    filename = file.split('.')[0]
    image = cv2.imread(f"{path}/{file}")
    img = cv2.resize(image, (800, 800))
    norm = np.zeros((800, 800))
    img = cv2.normalize(img, norm, 255, 0, cv2.NORM_MINMAX)
    cv2.imwrite(f"{os.path.join(Dir, 'target/normalize')}/{filename}1.jpg", img)
