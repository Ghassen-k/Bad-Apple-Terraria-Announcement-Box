import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path



def blacken(image):
    """Convert an image to colored blocks format."""
    height, width = image.shape  # Get image dimensions (height x width)
    for y in range(height):
        for x in range(width):

            intensity = int(image[y, x])

     
            if intensity > 125:
                image[y, x] = np.uint8(255)  # White block
            else:
                image[y, x] = np.uint8(0)  # Black block

    return image


frames = 0
dict_frames = {}
folder_path = Path('frames')

# Iterate over each file in the folder
for file_path in folder_path.iterdir():
    # Check if the current path is a regular file
    if file_path.is_file():
        # Process the file here (e.g., print its name)
        print(file_path.name)

    
    # reads image 'opencv-logo.png' as grayscale
    img = cv2.imread('frames/'+file_path.name, 0) 
    img_bw = blacken(img)
    plt.imshow(img, cmap='gray')
    
    
    frame_counter = 0
    line_reset = 1
    height, width = img_bw.shape
    
    
    
    
    for y in range(height):
        for x in range(width):
            pixel_clr = int(img_bw[y, x])
            if frame_counter == 0:
                if pixel_clr == 0:
                    sign_message = '[c/000000:■'
                    current_colour = 0
                    line_reset = 0
                elif pixel_clr == 255:
                    sign_message = '[c/FFFFFF:■'
                    current_colour = 1
                    line_reset = 0
            elif pixel_clr == 0 and line_reset:
                sign_message += '[c/000000:■'
                current_colour = 0
                line_reset = 0
            elif pixel_clr == 255 and line_reset:
                sign_message += '[c/FFFFFF:■'
                current_colour = 1
                line_reset = 0
            elif pixel_clr == 255 and current_colour:
                sign_message += '■'
            elif pixel_clr == 255 and not current_colour:
                sign_message += '][c/FFFFFF:■'
                current_colour = 1
            elif pixel_clr == 0 and not current_colour:
                sign_message += '■'
            elif pixel_clr == 0 and current_colour:
                sign_message += '][c/000000:■'
                current_colour = 0
    
                    
            frame_counter += 1
        sign_message += ']\n'
        line_reset = 1
    dict_frames[file_path.name.split('.')[0][5:]] = sign_message




            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

