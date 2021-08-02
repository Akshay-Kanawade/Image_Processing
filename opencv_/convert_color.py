import cv2
import os
import numpy as np
from PIL import Image

Dir=os.getcwd()
path = os.path.join(Dir, 'source')
images = os.listdir(path)
for file in images:
    filename = file.split('.')[0]
    image = cv2.imread(f"{path}/{file}")
    img = cv2.resize(image, (500, 500))
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    GRAY = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rgb_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    cv2.imwrite(f"{os.path.join(Dir, 'target/color')}/{filename}1.png", lab)
    cv2.imwrite(f"{os.path.join(Dir, 'target/color')}/{filename}2.png", GRAY)
    cv2.imwrite(f"{os.path.join(Dir, 'target/color')}/{filename}3.png", rgb_hsv)

    cv2.imwrite(f"{os.path.join(Dir, 'target/color')}/{filename}4.png", rgb)
    cv2.imwrite(f"{os.path.join(Dir, 'target/color')}/{filename}5.png", hsv)
