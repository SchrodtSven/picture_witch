from PIL import Image
import numpy as np

img_in = Image.open('tmp/ernstes_bild.jpg')
array = np.array(img_in)

padded_array = np.empty([600, 700, 3], dtype=np.uint8)
padded_array[:99, :] = np.array([0, 64, 128])
#padded_array[50:450, 80:570] = array

img_out = Image.fromarray(padded_array)
img_out.show()

#save('padded-boat.jpg')

