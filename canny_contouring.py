import sys, os
import matplotlib.pyplot as plt
import numpy as np
import skimage
from skimage import feature # We need to import this seperately becasue it does not autoimport
from scipy import ndimage

from util import image_path_gen, skimage_hyperparam_tuning, skimage_imshow_complete_wrapper

# Grey scale the item
def apply_greyscale(im):
    
    im = skimage.color.rgb2gray(im)
    return im # Note that rgb2gray outputs to float by default

# Gaussian (we primarily use this to determine the optimal)
def apply_gaussian(im, sigma = 4):
    pass

# Canny
def apply_canny(im, sigma = 4.5):
    im = feature.canny(im, sigma)
    return im

# Thresholding

# Filling
def apply_fill(im):
    im = ndimage.binary_fill_holes(im)
    return im

# Apply contouring (contouring + visualization largely pulled from https://scikit-image.org/docs/stable/auto_examples/edges/plot_contours.html#sphx-glr-auto-examples-edges-plot-contours-py)
def apply_contour(im):
    contours = skimage.measure.find_contours(im, level = .2) # Since I am not using most up to date version of scikit-image, i need to set level to its usualy default
    return contours

def viz_contours(im, ax, contours, plt_im = True):
    if plt_im:
        ax.imshow(skimage.util.img_as_float(im), cmap = plt.cm.gray) # See if this works and/or is any different than passing 'Grays'
    
    for contour in contours:
        # contour is essentially 2 vectors (row & col) stacked along the 2nd index
        # numpy uses (row, col) while matplotlib uses (x,y). Since col is essentially x and row is essentially y, we need to make sure that mapping remains true
        ax.plot(contour[:, 0], contour[:, 1], 'b')
    
    ax.axis('image') # this makes the axis limits the same as the datalimits. See https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html
    
    # Remove x and y ticks
    ax.set_xticks([])
    ax.set_yticks([])
    
    return ax

# Grab biggest encompassing contouring

# Masking & Image Transform

# Image transform

if __name__ == "__main__":
    in_dir = './compressed_images/'
    for im_name in os.listdir(in_dir):
        im = skimage.io.imread(os.path.join(in_dir, im_name)) # Note: these images are rotated 90* counterclockwise from the original due to how numpy indexes (with 0,0 being in the top right corner)
        
        # print(skimage.util.dtype_limits(im))
        im = skimage.util.img_as_ubyte(im)
        # plt.imshow(skimage.util.img_as_float(im))
        # plt.title(im_name)
        # plt.show()

        im = apply_greyscale(im)
        # plt.imshow(skimage.util.img_as_float(im), cmap = 'Greys')
        # plt.title(im_name)
        # plt.show()

        # skimage_hyperparam_tuning(im, apply_canny, skimage_imshow_complete_wrapper, sigma = np.linspace(0, 10, num = 20))

        im = apply_canny(im)

        im = apply_fill(im)
        plt.imshow(skimage.util.img_as_float(im), cmap = 'Greys')
        plt.title(im_name)
        plt.show()


        contours = apply_contour(im)
        #print(contours) 
        fig,ax = plt.subplots()
        ax = viz_contours(im, ax, contours, plt_im= False)
        plt.show()



