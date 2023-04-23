import glob
import os

import cv2
import numpy as np
from PIL import Image

img_path = './images/qualitative/*'
list_imgs = glob.glob(os.path.join(img_path, '*.png'))

for image_path in list_imgs:
	img = Image.open(image_path)
	img.resize((300, 300)).save(image_path)
	print(image_path)
