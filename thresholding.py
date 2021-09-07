import sys, os
import matplotlib.pyplot as plt
import numpy as np
import skimage
from skimage import feature # We need to import this seperately becasue it does not autoimport
from scipy import ndimage

from util import image_path_gen, skimage_hyperparam_tuning, skimage_imshow_complete_wrapper
from canny_contouring import apply_greyscale

def apply_threshold(im, low = None, high = None):
    # Apply a binary encode with either low or high
    im_binary = np.zeros(im.shape)
    if low is not None:
        im_binary[im < low] = 1
    if high is not None:
        im_binary[im > high] = 1
    return im_binary


if __name__ == "__main__":
    in_dir = './compressed_images/'
    for im_name in os.listdir(in_dir):
        im = skimage.io.imread(os.path.join(in_dir, im_name)) # Note: these images are rotated 90* counterclockwise from the original due to how numpy indexes (with 0,0 being in the top right corner)
        im = apply_greyscale(im)
        print(np.max(im))
        im_show = plt.imshow(im, cmap = plt.get_cmap('Greys'))
        plt.colorbar(im_show)
        plt.title(im_name)
        plt.show()



        im = apply_threshold(im, high = 240 / 255)
        im_show = plt.imshow(im, cmap = plt.get_cmap('Greys'))
        plt.colorbar(im_show)
        plt.title(im_name)
        plt.show()