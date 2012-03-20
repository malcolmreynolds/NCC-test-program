#!/usr/bin/env ipython
import numpy as np
from skimage.feature.template import match_template as ncc  # Tony Yu's fork of skimage, https://github.com/scikits-image/scikits-image/pull/100
from scipy.misc import imread, imsave
import matplotlib.pyplot as plt
import sys

im_filename = 'lena.png'


def image_cc_self(im):
    """Run cross correlation where the template is the centre of the image
    so we should see a huge peak."""
    # Get size of image, extract red channel
    (h, w, _) = im.shape
    im_red = im[:, :, 0]

    # Crop out central image using these indices
    hrng_start, hrng_end = np.round(h / 4), np.round(3 * h / 4)
    wrng_start, wrng_end = np.round(w / 4), np.round(3 * w / 4)
    im_centre_red = im_red[hrng_start:hrng_end, wrng_start:wrng_end]

    # Print out some stuff just to confirm we have loaded the same segment
    # as in matlab
    print "image size is %s" % str(im_red.shape)
    print "template size is %s" % str(im_centre_red.shape)
    print "template min/max = %f/%f" % (im_centre_red.min(), im_centre_red.max())
    print "template mean = %f" % im_centre_red.mean()

    # Do NCC, with and without padding
    ncc_result_pad = ncc(im_red, im_centre_red, True)
    ncc_result_nopad = ncc(im_red, im_centre_red, False)

    # Display output and save
    plt.figure()
    plt.imshow(ncc_result_pad)
    plt.title('ncc result padded, size %s' % str(ncc_result_pad.shape))
    imsave('py_result_pad.png', ncc_result_pad)

    plt.figure()
    plt.imshow(ncc_result_nopad)
    plt.title('ncc_result not padded, size %s' % str(ncc_result_nopad.shape))
    imsave('py_result_nopad.png', ncc_result_nopad)

if __name__ == "__main__":
    # User can override the default image
    if len(sys.argv) > 1:
        im_filename = sys.argv[1]

    print "testing NCC on", im_filename
    image_cc_self(imread(im_filename))
