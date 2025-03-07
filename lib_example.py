from img_lib import ImgWorker, Coordinator
from PIL import Image
import numpy as np



coer = Coordinator()


print(coer.center, coer.br)
exit()

worker = ImgWorker()
# test_image_rgb.webp
first = Image.open('test_image_rgb.webp') # size (2048, 1536)
# first.show()
# cropped = worker.crop(first, 994, 738, 1054, 798)
# cropped.show()
print(type(first.size), first.size)




# 738, 994 (LT)
# 798, 1054 (BR)
#gray = worker.grayscale(first)
#gray.show()



#exit()
# flipped = worker.roll(first, 192, 0)
# flipped.show()
#second_sep = worker.sepia(first, 0.55)
#second_sep.show()