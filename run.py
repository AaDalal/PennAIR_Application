import sys, os
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.numeric import argwhere
import skimage
from skimage import feature # We need to import this seperately becasue it does not autoimport
from scipy import ndimage

from util import image_path_gen, skimage_hyperparam_tuning, skimage_imshow_complete_wrapper
from thresholding import *
from canny_contouring import *

from sklearn.cluster import DBSCAN

in_dir = './compressed_images/'
for im_name in os.listdir(in_dir):
    im = skimage.io.imread(os.path.join(in_dir, im_name)) # Note: these images are rotated 90* counterclockwise from the original due to how numpy indexes (with 0,0 being in the top right corner)
    im = skimage.util.img_as_ubyte(im)
    im = apply_greyscale(im) # This is a datatype change
    im = apply_threshold(im, high = 230 / 255) 
    plt.imshow(skimage.util.img_as_float(im))
    plt.title(im_name)
    plt.show()

    # -- Canny + fill --> works poorly :5[
    # im = apply_canny(im)
    # im = apply_fill(im)
    # plt.imshow(skimage.util.img_as_float(im))
    # plt.title(im_name)
    # plt.show()

    # -- DBSCAN clustering
    clusterer = DBSCAN(eps=20*(2**.5), min_samples=100) # Since our images are so large, we need ot include quite a large EPS and min_samples. To make it more robust, you could sacle EPS and min_samples based on image size
    clusters = clusterer.fit_predict(np.argwhere(im)) # Get the indices of all nonzero pixels and feed them into the dbscan algo to identify the imag
    # Since DBSCan uses numbers -1 to represetn no cluster nad 0-n-1 for n clusters, we need to add 2 to clusters to make sure that 0, which is the base color in our thresholded image is not accidentally folded in with a cluster
    clusters += 2 # Now unclustered points are 1, and clusters go from [2,n+1] (inclusive)
    im[np.nonzero(im)] = clusters # np.nonzero is essentially np.argwhere transposed to match what numpy indexing expects
    im_show = plt.imshow(im, cmap = plt.get_cmap('tab10'))
    plt.colorbar(im_show)
    plt.title(im_name)
    plt.show()
    