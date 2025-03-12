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
        # Sanitizing values (limiting each value to one byte's range)
        np.clip(tmp_arr, 0, 255)
        
        # Returning np array converted back to P.I.I
        return Image.fromarray(tmp_arr)
    
    def sepia(self, img: Image.Image, intensity: int = 0.6)->Image.Image:
        # SEE: https://drafts.fxtf.org/filter-effects/#sepiaEquivalent 
            tmp = np.array(img)

            # Transforming each pixel's bands (r,g,b) 
            map_a = np.matrix([
                                [ 0.393 + 0.607 * (1 - intensity), 0.769 - 0.769 * (1 - intensity), 0.189 - 0.189 * (1 - intensity)],
                                [ 0.349 - 0.349 * (1 - intensity), 0.686 + 0.314 * (1 - intensity), 0.168 - 0.168 * (1 - intensity)],
                                [ 0.272 - 0.349 * (1 - intensity), 0.534 - 0.534 * (1 - intensity), 0.131 + 0.869 * (1 - intensity)]
            ])

            filter_mapper = np.array([x * map_a for x in tmp] )

            # Sanitizing values
            np.clip(filter_mapper, 0, 255)

            # Returning np array converted back to P.I.I
            return Image.fromarray(filter_mapper.astype('uint8'))


filter = ImgFilter()
first = Image.open('sven.jpg')

second_sep = filter.sepia(first, 0.55)
second_sep.show()

