from img_lib import ImgWorker, Coordinator
from PIL import Image
import numpy as np



coer = Coordinator()
print(str(coer))

print(coer.center, coer.br)
#exit()

worker = ImgWorker()
# test_image_rgb.webp
first = Image.open('sven.jpg') 
print(type(first.size), first.size)

exit()
""" inv = worker.invert(first)
inv.show()

exit() """


cropped = worker.crop(first, 70, 56, 123, 325)
cropped.show()
print(type(first.size), first.size)




# 738, 994 (LT)
