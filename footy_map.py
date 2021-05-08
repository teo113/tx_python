import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch


# Fixing random state for reproducibility
np.random.seed(19680801)

# A sample image
#w, h = 369, 612
with cbook.get_sample_data(r'C:/Users/theo/Pictures/pitch_port.jpg') as image_file:
    image = plt.imread(image_file)

fig, ax = plt.subplots()
ax.imshow(image)
ax.axis('on')  # clear x-axis and y-axis
plt.show()

# And another image

# Data are 256x256 16-bit integers.
w, h = 369, 612
with cbook.get_sample_data(r'C:\Users\theo\Pictures\pitch_port.jpg') as datafile:
    s = datafile.read()
A = np.frombuffer(s, np.uint16).astype(float).reshape((w, h))

fig, ax = plt.subplots()
extent = (0, 25, 0, 25)
im = ax.imshow(A, cmap=plt.cm.hot, origin='upper', extent=extent)

markers = [(15.9, 14.5), (16.8, 15)]
x, y = zip(*markers)
ax.plot(x, y, 'o')

ax.set_title('MRI')

plt.show()
