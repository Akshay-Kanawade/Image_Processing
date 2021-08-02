import cv2
import numpy as np
import os

Dir = os.getcwd()
path = os.path.join(Dir, 'source')
images = os.listdir(path)


def translate(img, x, y):
    transmat = np.float32([[1, 0, x], [0, 1, y]])
    dim = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transmat, dim)


for file in images:
    filename = file.split('.')[0]
    image = cv2.imread(f"{path}/{file}")
    translated = translate(image, -100, 100)
    translated1 = translate(image, 100, -100)
    translated2 = translate(image, 100, 100)
    translated3 = translate(image, -100, -100)
    cv2.imwrite(f"{os.path.join(Dir, 'target/img_translation')}/{filename}1.jpg", translated)
    cv2.imwrite(f"{os.path.join(Dir, 'target/img_translation')}/{filename}2.jpg", translated1)
    cv2.imwrite(f"{os.path.join(Dir, 'target/img_translation')}/{filename}3.jpg", translated2)
    cv2.imwrite(f"{os.path.join(Dir, 'target/img_translation')}/{filename}4.jpg", translated3)
