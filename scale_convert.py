#!/usr/bin/env python

import os
from PIL import Image

directory = os.path.abspath('/Users/ralphdelacruz/Desktop/Projects/PILProject/images')
save_directory = os.path.abspath('/Users/ralphdelacruz/Desktop/Projects/PILProject/opts/icons')

def main():
    for file_name in os.listdir(directory):
        output = os.path.splitext(file_name)[0]
        new_path = os.path.join(directory, output)
        im = Image.open(new_path)
        rgb_im = im.convert('RGB')

        new_path = os.path.join(save_directory, output)
        rgb_im.rotate(270).resize((128,128)).save(new_path, 'JPEG')
        print(output)
main()

# remove the .DS_Store file first
