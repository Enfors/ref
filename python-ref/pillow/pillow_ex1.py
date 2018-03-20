#!/usr/bin/env python3

from PIL import Image

# Open image
im = Image.open("link.jpg")

# Get format, size and mode
print(im.format, im.size, im.mode)

# Show the image - only works if xv is installed
im.show()

# Cropping
#      Left, upper, right, lower
#      bot_x, bot_y, top_x, top_y
box = (100, 100, 400, 400)
region = im.crop(box)

# Save image
#im.save("savefile.jpg", "JPEG")

# Transposing and rotating
region = region.transpose(Image.ROTATE_180)
im.paste(region, box)

