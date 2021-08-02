import cv2
import numpy as np
import os

Dir = os.getcwd()
path = os.path.join(Dir, 'source')
images = os.listdir(path)


def rescale(frame, scale=0.20):
    w = int(frame.shape[1] * scale)
    h = int(frame.shape[0] * scale)
    dim = (w, h)
    return cv2.resize(frame, dim)
for file in images:
    filename = file.split('.')[0]
    image = cv2.imread(f"{path}/{file}")
    resized_img = rescale(image)
    cv2.imwrite(f"{os.path.join(Dir, 'target/rescale')}/{filename}1.jpg", resized_img)
