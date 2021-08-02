import cv2
import os

Dir = os.getcwd()
path = os.path.join(Dir, 'source')
images = os.listdir(path)

for file in images:
    filename = file.split('.')[0]
    image = cv2.imread(f"{path}/{file}")
    b, g, r = cv2.split(image)
    cv2.imwrite(f"{os.path.join(Dir, 'target/split')}/{filename}1.jpg", b)
    cv2.imwrite(f"{os.path.join(Dir, 'target/split')}/{filename}2.jpg", g)
    cv2.imwrite(f"{os.path.join(Dir, 'target/split')}/{filename}3.jpg", r)
