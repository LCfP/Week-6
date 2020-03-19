from PIL import Image
import numpy as np

# open the image to be accessed using 'im'
original_image = Image.open("fruit_fade.png")
# convert the image to a numpy array called 'pix'
pixel_array = np.array(original_image)

# create a new list for the new image
new_pixel_array = []
for row in pixel_array:
    # create a new list for each row of pixels in the image
    new_row = []
    for pixel in row:
        # add each converted pixel (here +100) to the new row
        new_row.append(pixel + 100)
        # should make sure the new numbers are in range...
    # add the new row to the new image
    new_pixel_array.append(new_row)

# convert the new image to an array of 8 bit integers
# uint8 => unsigned (no negative numbers) integers of 8 bits
new_pixel_array = np.array(new_pixel_array).astype('uint8')
# convert the array into an image
lighter_image = Image.fromarray(new_pixel_array)
# show the new image
lighter_image.show()
