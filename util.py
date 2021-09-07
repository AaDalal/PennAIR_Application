import json
import matplotlib.pyplot as plt
from json import dump

def skimage_hyperparam_tuning(im, func, callback,  **hyperparams):
    all_im = []
    for i in range(len(list(hyperparams.values())[0])): # We assume the dictionary kwargs list has iterable values that are all of the same length
        # Get curr_kwargs
        curr_hyperparams = {key : hyperparams[key][i] for key in hyperparams}
        curr_im = func(im, **curr_hyperparams)
        all_im.append(curr_im)
        
        # do callback
        callback(curr_im, curr_hyperparams)
    return curr_im

def skimage_imshow_complete_wrapper(im, curr_hyperparams):
    ax = plt.gca()
    skimage_imshow(im, ax, cmap = plt.cm.gray)
    ax.set_title(json.dumps(curr_hyperparams))
    plt.show()


def skimage_imshow(im, ax, **kwargs):
    ax.imshow(im, **kwargs)
    return ax

def image_path_gen(im_dir_path):
    im_dir_path = os.path.realpath(im_dir_path)
    for im_name in os.listdir(im_dir_path):
        yield os.path.join(im_dir_path, im_name), im_name