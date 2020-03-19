from PIL import Image
import numpy as np

original_image = Image.open("fruit_fade.png")
pixel_array = np.array(original_image)

# get the maximum value
maximum = np.max(pixel_array)

# calculate the scaling factor
scale = 255.0/maximum

# create the new 2D array
new_pixel_array = []
for row in pixel_array:
    new_row = []
    for pixel in row:
        new_row.append(pixel * scale)
    new_pixel_array.append(new_row)

new_pixel_array = np.array(new_pixel_array).astype('uint8')

scaled_image = Image.fromarray(new_pixel_array)
scaled_image.show()
