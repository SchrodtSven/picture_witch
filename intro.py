# Experiments with PIL 
# SINCE: 2025-03-06
from PIL import Image
import numpy as np


class ImgFilter:
    """" Applying different filters to PIL.* instances  """
    
    def change_value_by(self, img: Image.Image, value: int)->Image.Image:
        """ Changing each value by given value (+/-) - generic function """
        # Converting PII to np.array
        tmp_arr = np.array(img)
        # Setting (+/-) value
        tmp_arr += value
        # Limiting each value to one byte's range
        np.clip(tmp_arr, 0, 255)
        
        # Returning np array converted back to P.I.I
        return Image.fromarray(tmp_arr)
    
    def sepia(img: Image.Image, intensity: int = 0.6)->Image.Image:
        # SEE: https://drafts.fxtf.org/filter-effects/#sepiaEquivalent 
            tmp = np.array(img)

            # Tranforming each pixel's r,g,b parts

            lmap = np.matrix([
                                [ 0.393 + 0.607 * (1 - intensity), 0.769 - 0.769 * (1 - intensity), 0.189 - 0.189 * (1 - intensity)],
                                [ 0.349 - 0.349 * (1 - intensity), 0.686 + 0.314 * (1 - intensity), 0.168 - 0.168 * (1 - intensity)],
                                [ 0.272 - 0.349 * (1 - intensity), 0.534 - 0.534* (1 - intensity), 0.131 + 0.869 * (1 - intensity)]
            ])

            filter_mapper = np.array([x * lmap.T for x in img] )

            # Sanitizing values
            np.clip(filter_mapper, 0, 255)

            # Returning np array converted back to P.I.I
            return Image.fromarray(filter_mapper.astype('uint8'))


filter = ImgFilter()
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
