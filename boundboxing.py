import numpy as np
import math
from skimage.morphology import convex_hull_image

def min_bounding_rect(im):
    inds = np.argwhere(im)
    min_r, min_c = np.min(inds, axis = 0)
    max_r, max_c = np.max(inds, axis = 0)
    return (min_r, max_r), (max_r, min_r)

def min_bounding_area(range1, range2):
    return (range1[1]-range1[0]) * (range2[1] - range2[0])

# Valley descent algorithm can be used to find the rotation that produces the minimal boundbox are
# Add some epsilon for the imprecision of the rotation
# 1. Apply some rotation and see if it gets better
# 2. If not, then reverse direction and apply the same amount of rotation
# 3. Continue to apply until it gets worse
# Essentially, the change should be proportional & sign reversed from the error

def valley_descent(objective_func, initial_step_size, altereration_func, initial_data, allowable_error):
    error = objective_func(initial_data)
    theta = 0
    while error > allowable_error:
        pass
    pass

def parallelogram_rotation(r_range, c_range):
    return math.atan(r_range[0], c_range[0])

def apply_convex_hull(im):
    return convex_hull_image(im)

    
