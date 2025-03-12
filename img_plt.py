import numpy as np
import matplotlib.pyplot as plt

# img = np.zeros((90, 90, 3), dtype=np.uint8) # col row clr
# img[0:30,:,:] = [128, 0, 128]
# img[30:60,:,:] = [128, 128, 0]

img = np.random.randint(0,256,(100,100,3), np.uint8)
plt.title('Random img')
plt.imshow(img)
plt.show()