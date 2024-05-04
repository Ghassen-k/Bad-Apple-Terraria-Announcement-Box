import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path



from PIL import Image

# Path to the input image file
image_path = 'lena.png'

# Open the PNG image file
image = Image.open(image_path)

# Get the width and height of the image
width, height = image.size


# Close the image

frame_counter = 0

for y in range(height):
        for x in range(width):
            r, g, b, _ = image.getpixel((x, y))
            
            if frame_counter == 0:
                sign_message = '[c/' + f"{r:02X}{g:02X}{b:02X}" + ':■]'
            else:
                sign_message += '[c/' + f"{r:02X}{g:02X}{b:02X}" + ':■]'
            frame_counter += 1
        sign_message += '\n'
        line_reset = 1
print(sign_message)
                    

image.close()
                    
