import cv2
import os
import numpy as np
from PIL import Image

Dir = os.getcwd()
path = os.path.join(Dir, 'source')
images = os.listdir(path)
for file in images:
        filename = file.split('.')[0]
        image = cv2.imread(f"{path}/{file}")
        img = cv2.resize(image,(500,500))
        # <class 'numpy.ndarray'>
        #print(img.size)
        # (225, 400, 3)
        #path = os.path.join(Dir, 'rotate')

        img_rotate_90_clockwise = cv2.rotate(np.float32(img), cv2.ROTATE_90_CLOCKWISE)
        #img_rotate_90_clockwise.save(f"{os.path.join(Dir, 'rotate')}/{filename}.png", "PNG")
        cv2.imwrite(f"{os.path.join(Dir, 'target/rotate')}/{filename}1.png", img_rotate_90_clockwise)
        # True

        img_rotate_90_counterclockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite(f"{os.path.join(Dir, 'target/rotate')}/{filename}2.png", img_rotate_90_counterclockwise)
        # True

        img_rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
        cv2.imwrite(f"{os.path.join(Dir, 'target/rotate')}/{filename}3.png", img_rotate_180)
        # True