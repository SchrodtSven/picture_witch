# SUBJECT: Experiments with PIL
# SINCE: 2025-03-07
# AUTHOR: Sven Schrodt
from PIL import Image
import numpy as np


class ImgWorker:
    """ Applying different filters to PIL.* instances  using numpy operations instead of PIL methods """

    FLP_VERT = 0
    FLP_HORZ = 1

    def change_value_by(self, img: Image.Image, value: int) -> Image.Image:
        """ Changing each value by given value (+/-) - generic function 
            to be used by (color / other) filter functions
        """
        # Converting PII to np.array
        tmp_arr = np.array(img)
        # Setting (+/-) value
        tmp_arr += value
        # Sanitizing values (limiting each value to one byte's range)
        #np.clip(tmp_arr, 0, 255)

        # Returning np array converted back to P.I.I
        return Image.fromarray(tmp_arr).astype("uint8")
    

    def grayscale(self, img: Image.Image) -> Image.Image:
        # HINT: currently an RGB image is prereq 4 this
        
        # Splitting into bands
        r, g, b = img.split()
        
        # building numpy arrays
        ra = np.array(r)
        ga = np.array(g)
        ba = np.array(b)
        
        # Using NTSC formula: 0.299 ∙ Red + 0.587 ∙ Green + 0.114 ∙ Blue
        gray_a = 0.299 * ra + 0.587 * ga  + 0.114 * ba
        return Image.fromarray(gray_a.astype("uint8"))

    

    def sepia(self, img: Image.Image, intensity: int = 0.6) -> Image.Image:
        # SEE: https://drafts.fxtf.org/filter-effects/#sepiaEquivalent
        # HINT: currently an RGB image is prereq 4 this
        tmp = np.array(img)

        # Transforming each pixel's bands (r,g,b)
        map_a = np.matrix(
            [
                [
                    0.393 + 0.607 * (1 - intensity),
                    0.769 - 0.769 * (1 - intensity),
                    0.189 - 0.189 * (1 - intensity),
                ],
                [
                    0.349 - 0.349 * (1 - intensity),
                    0.686 + 0.314 * (1 - intensity),
                    0.168 - 0.168 * (1 - intensity),
                ],
                [
                    0.272 - 0.349 * (1 - intensity),
                    0.534 - 0.534 * (1 - intensity),
                    0.131 + 0.869 * (1 - intensity),
                ],
            ]
        )

        filter_mapper = np.array([x * map_a for x in tmp])
         # Returning np array converted back to P.I.I
        return Image.fromarray(filter_mapper.astype("uint8"))
        
    def rotate(self, img: Image.Image, times:int=1, axes:tuple=(0, 1)) -> Image.Image:
        """ Rotating image x times by 90°  """
       
        tmp = np.array(img)
        return Image.fromarray(np.rot90(tmp, times, axes).astype("uint8"))
    
    def roll(self, img: Image.Image, shift_by:int=1, axes=None) -> Image.Image:
        """ Rotating image x times by 90°  """

        tmp = np.array(img)
        return Image.fromarray(np.roll(tmp, shift_by, axes).astype("uint8"))
       

    def flip(self, img: Image.Image, mode=FLP_HORZ):
        tmp = np.array(img)
        return Image.fromarray(np.flip(tmp, mode).astype("uint8"))

    def crop(self, img: Image.Image, x1:int, y1:int, x2:int, y2:int):
        tmp = np.array(img)
        return Image.fromarray((tmp[y1:x1, y2:x2]).astype("uint8"))
    

class Coordinator:
    """  Getting coordinates from given objects, rel./abs. positions, radius, length... """
    
    lt = (0, 0)
    br = (0, 0)
    dim = (0, 0)
    center = (0, 0)
    current = (0, 0)
    
    x = 0
    y = 0
    
    def __init__(self, dim:tuple = (100, 100)):
        self.dim = dim
        self.calc()

    def calc(self):
        self.x = self.dim[0] -1
        self.y = self.dim[1] -1
        self.br = (self.x, self.y)
        
        self.center = (self.dim[0] //2, self.dim[1] //2)