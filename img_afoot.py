import numpy as np
from PIL import Image

array = np.zeros([100, 300, 3], dtype=np.uint8)
array[:,:100] = [255, 128, 0] #Orange left side
array[:,100:200] = [0, 0, 255]   #Blue mid part
array[:,200:] = [0, 255, 0]   #Green right side
img = Image.fromarray(array)
# img.save('testrgb.png')
img.show()
