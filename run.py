import sys, os
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.numeric import argwhere
import skimage
from sklearn.cluster import DBSCAN

from util import image_path_gen, skimage_hyperparam_tuning, skimage_imshow_complete_wrapper
from thresholding import *
from canny_contouring import *
from boundboxing import *

in_dir = './compressed_images/'
for im_name in os.listdir(in_dir):
    im = skimage.io.imread(os.path.join(in_dir, im_name)) # Note: these images are rotated 90* counterclockwise from the original due to how numpy indexes (with 0,0 being in the top right corner)
    im = skimage.util.img_as_ubyte(im)
    
    # **********
    # * PART I *
    # **********


    # -- Grayscale
    im = apply_greyscale(im) # This is a datatype change
    
    # -- Threshold
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
    clusterer = DBSCAN(eps=20*(2**.5), min_samples=500) # Since our images are so large, we need ot include quite a large EPS and min_samples. To make it more robust, you could sacle EPS and min_samples based on image size
    clusters = clusterer.fit_predict(np.argwhere(im)) # Get the indices of all nonzero pixels and feed them into the dbscan algo to identify the imag
    # Since DBSCan uses numbers -1 to represetn no cluster nad 0-n-1 for n clusters, we need to add 2 to clusters to make sure that 0, which is the base color in our thresholded image is not accidentally folded in with a cluster
    clusters += 2 # Now unclustered points are 1, and clusters go from [2,n+1] (inclusive)
    im[np.nonzero(im)] = clusters # np.nonzero is essentially np.argwhere transposed to match what numpy indexing expects
    im_show = plt.imshow(im, cmap = plt.get_cmap('tab10'))
    plt.colorbar(im_show)
    plt.title(im_name)
    plt.show()

    # -- CONVEX HULL
    clusters_chulls = []
    for i in range(2, int(np.max(im))+1): # Remember that we added two to everything, so actual clusters are labeled starting at 2 up to and including the max label value
        cluster_im = np.zeros(im.shape)
        cluster_im[im == i] = 1

        chull = apply_convex_hull(cluster_im)
        clusters_chulls.append(chull)

        im_show = plt.imshow(chull, cmap = plt.get_cmap('binary'))
        #plt.colorbar(im_show)
        plt.title(im_name + ": " + str(i))
        plt.show()

    # -- Picking a DBSCAN cluster based on how boxy the cluster hulls are


    # ***********
    # * PART II *
    # ***********

    # -- Compute a perspective transform to a square 
    
    # See: https://scikit-image.org/docs/dev/auto_examples/transform/plot_geometric.html

    # ************
    # * PART III *
    # ************   
    
    # -- Use pattern identification to determine which way the 3 pieces with the eyes on them should face
    
    # See: https://scikit-image.org/docs/dev/auto_examples/features_detection/plot_template.html

    # -- Either use aspect ratio of 4th piece or Change the orientation of the fourth piece to determine and scan each option with something like QRtools (https://launchpad.net/qr-tools) 

    # -- (if needed) iteratively bring adjacent QR codes closer together and take the sum of the elementwise multiplication (like a dot product) to calculate a cross-correlation value. 

    # -- Take overlap value with max cross correlation to be actual overlap.