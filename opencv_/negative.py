from PIL import Image
import cv2
import sys
import numpy as np
import os

S = 255
Dir = os.getcwd()
path = os.path.join(Dir, 'source')
images = os.listdir(path)

for file in images:
    filename = file.split('.')[0]
    image = cv2.imread(f"{path}/{file}")
    # if in rgb
    shape = image.shape
    if shape[2] == "rgb":
        B, G, R = cv2.split(image)
        B[:] = [S - x for x in B]  # inverting blue
        G[:] = [S - x for x in G]  # inverting green
        R[:] = [S - x for x in R]  # inverting red

        # saving image
        my_img = cv2.merge((B, G, R))
        cv2.imwrite(f"{os.path.join(Dir, 'target/negative')}/{filename}1.jpg", my_img)
    else:
        # open in grayscale
        my_img = np.array([S - x for x in image])
        cv2.imwrite(f"{os.path.join(Dir, 'target/negative')}/{filename}1.jpg", my_img)
