import skimage
import matplotlib.pyplot as plt
import numpy as np
import os
from util import image_path_gen

def apply_compress(im):
    im = skimage.transform.rescale(im, 0.5, anti_aliasing=True)
    return im

if __name__ == "__main__":
    in_dir = './raw_images/'
    out_dir = './compressed_images/'
    for im_path, im_name in image_path_gen(in_dir):
        im = skimage.io.imread(im_path)
        im = apply_compress(im)
        skimage.io.imsave(os.path.join(os.path.realpath(out_dir), im_name), im) # note these images are rotated 90* counter clockwise
