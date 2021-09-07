import sys, os
import matplotlib.pyplot as plt
import numpy as np
import skimage
from skimage import feature # We need to import this seperately becasue it does not autoimport
from scipy import ndimage

from util import image_path_gen, skimage_hyperparam_tuning, skimage_imshow_complete_wrapper
from thresholding import *
from canny_contouring import *

in_dir = './compressed_images/'
for im_name in os.listdir(in_dir):
    im = skimage.io.imread(os.path.join(in_dir, im_name)) # Note: these images are rotated 90* counterclockwise from the original due to how numpy indexes (with 0,0 being in the top right corner)
    im = skimage.util.img_as_ubyte(im)
    im = apply_greyscale(im) # This is a datatype change
    im = apply_threshold(im, high = 230 / 255)
    im = apply_canny(im)
    im = apply_fill(im)


    plt.imshow(skimage.util.img_as_float(im), cmap = 'Greys')
    plt.title(im_name)
    plt.show()