# Experiments with PIL 
# SINCE: 2025-03-06
from PIL import Image
import numpy as np


class PILFilter:
    """" Applying different filters to PIL.* instances  """
    
    def change_value_by(self, img: Image.Image, value: int)->Image.Image:
        """ Changing each value by given value (+/-) """
        # Converting PII to np.array
        tmp_arr = np.array(img)
        # Setting (+/-) value
        tmp_arr += value
        # Limiting each value to one byte's range
        np.clip(tmp_arr, 0, 255)
        
        # returning np array converted back to P.I.I
        return Image.fromarray(tmp_arr)


filter = PILFilter()
first = Image.open('ernstes_bild.jpg')
dim = first.size
print(dim)
r,g,b = first.split()
# b_a = filter.change_value_by(b, 99)
r_a = filter.change_value_by(r, 99)
second = Image.merge("RGB", (r_a, g, b))
size = 533, 300

thumb = first.resize(size)
# thumb.show()

print(type(thumb))
print(second.size)
pixelated = thumb.resize((1066, 600))
pixelated.show()
exit()
# first.mode
# splitting to r,g,b bands



r_arr = np.array(r)
np.clip(r_arr,0,255)

print(type(r), r)

# exit()
r_arr +=99

# 

second = PIL.Image.merge("RGB", (PIL.Image.fromarray(r_arr), g, b))
second.save('red.jpg')
# second.show()

r.show()
#first.show()


print(type(r_arr), r_arr)
