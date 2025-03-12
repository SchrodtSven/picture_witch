import numpy as np
from PIL import Image

# array = np.zeros([100, 300, 3], dtype=np.uint8)


# # [y, x]  => [r, g, b]
# array[:,:100] = [255, 128, 0] #Orange left side
# array[:,100:200] = [0, 0, 255]   #Blue mid part
# array[:,200:] = [0, 255, 0]   #Green right side


# img = Image.fromarray(array)
# # img.save('testrgb.png')
# img.show()


import numpy as np
from PIL import Image

array = np.zeros([100, 200], dtype=np.uint8)

# Set grey value to black or white depending on x position
for x in range(200):
    for y in range(100):
        if (x % 16) // 8 == (y % 16) // 8:
            array[y, x] = 0
        else:
            array[y, x] = 255

img = Image.fromarray(array)
#img.save('testgrey.png')
img.show()