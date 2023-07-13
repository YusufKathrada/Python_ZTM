# cmd line arguements, (1) [Existing] folder where images are from (2) [new] folder where you want new images to be
# saved, if folder does not exist, create the folder

# Loop through existing folder, convert images from jpg to png, save to new folder

# Example of cmd line: python JPGtoPNGConverter.py existing_folder new_folder

# --------------------------------------------------------

import sys
import os
from PIL import Image

# Input from cmd line
existing_folder = sys.argv[1]
new_folder = sys.argv[2]

# Checking to see if new folder exists
check_new_folder = os.path.isdir(new_folder)
# if not, create it
if not check_new_folder:
    os.makedirs(new_folder)

# iterating through each file in existing_folder
for file in os.listdir(existing_folder):
    filename = os.fsdecode(file)
    img = Image.open(existing_folder + "\\" + filename)

    # converting jpg to png AND saving to new_folder
    img.save(new_folder + "\\" + os.path.splitext(filename)[0] + ".png", "png")

    print(f"Converted " + {filename})

print("All Done!")







