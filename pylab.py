from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
# read image to array
im = np.array(Image.open('python.png'))
# plot the image
plt.imshow(im)
# some points
x = [100,100,400,400]
y = [200,500,200,500]
# plot the points with red star-markers
plt.plot(x,y,'go-')
# line plot connecting the first two points
plt.plot(x[:2],y[:2],'go-')
# add title and show the plot
plt.title('Plotting: "python.png"')
plt.show()