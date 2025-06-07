# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 19:27:33 2023

@author: Aymam
"""

from PIL import Image
import os


def thecropperfunction(thedirinput):

    # folder path
    dir_path = thedirinput
    path_clear = f"{dir_path}\Formatlananlar"

    if "Formatlananlar" not in os.listdir(dir_path):
        directory = "Formatlananlar"
        parent_dir = dir_path
        path = os.path.join(parent_dir, directory)
        path_clear = os.path.join(parent_dir, directory)

        os.mkdir(path)

    # list to store files
    res = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            if path[-1] == 'g' or path[-1] == 'G':
                res.append(path)

    for element in res:
        thefile = os.path.join(dir_path, element)

        im = Image.open(thefile)

        pix_x = 5184
        pix_y = 3456

        pos_x1 = 0.2592
        pos_y1 = 0.1731

        pos_x2 = 0.776
        pos_y2 = 0.85

        x1 = pix_x * pos_x1
        y1 = pix_y * pos_y1

        x2 = pix_x * pos_x2
        y2 = pix_y * pos_y2

        box = (round(x1), round(y1), round(x2), round(y2))

        theratio = 2679 / 2340

        img2 = im.crop(box)
        img2 = img2.resize((round(200 * theratio), 200), Image.ANTIALIAS)

        im1 = img2.save(f"{path_clear}\{element}")


# thecropperfunction(r'C:\Users\Aymam\Desktop\dukkan\patikat - cropper deneme\FİLET\GARSON')