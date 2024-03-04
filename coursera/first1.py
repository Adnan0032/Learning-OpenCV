import numpy as np
import matplotlib.pyplot as plt
import PIL


image = PIL.Image.open("python.png")
print(image)
image_array = np.asarray(image)
print(image_array.shape)
print(image_array)
plt.imshow(image_array)