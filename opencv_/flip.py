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
    img = cv2.resize(image, (500, 500))

    img_flip_ud = cv2.flip(img, 0)  # vertical
    cv2.imwrite(f"{os.path.join(Dir, 'target/flip')}/{filename}1.png", img_flip_ud)

    img_flip_lr = cv2.flip(img, 1)  # horizontal
    cv2.imwrite(f"{os.path.join(Dir, 'target/flip')}/{filename}2.png", img_flip_lr)
    # True

    img_flip_ud_lr = cv2.flip(img, -1)  # vertical and horizontal
    cv2.imwrite(f"{os.path.join(Dir, 'target/flip')}/{filename}3.png", img_flip_ud_lr)
