import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

#convert img int32 values to float32
def im2float(m):
    return np.array(m/255, dtype = 'float32')


def remove_channel(img: np.array):

    return img[:,:,0:3]

def create_subplot(img : str, img2 : str , diff):

    img_p1 = imread(img)
    img_p2 = imread(img2)

    fig, (ax1,ax2,ax3) = plt.subplots(1,3)
    fig.suptitle("Difference between the two images")
    ax1.imshow(img_p1)
    ax2.imshow(img_p2)
    ax3.imshow(diff)
    ax3.set_title("Difference")
    ax1.set_title("Original")
    ax2.set_title("Modified")
    return fig

def imgprocessor():
    im1 = imread('sushi1.png')
    im2 = imread('sushi2.png')


    im1_no_alpha_channel = remove_channel(im1)
    im2_no_alpha_channel = remove_channel(im2)
    #take the mean over the 3 rgb channels after removing the alpha channel
    img1_gray = np.mean(im1_no_alpha_channel, axis=2)
    img2_gray = np.mean(im2_no_alpha_channel, axis=2)

    diff = img1_gray - img2_gray
    diff_thresholded = diff**2 > 0.010
    xdim , ydim  = img1_gray.shape
    img1_gray_3d = np.reshape(img1_gray,(xdim,ydim,1))
    img1_gray_3d.shape
    diff_rgb = np.tile(img1_gray_3d, (1,1,3))
    red = [1,0,0]
    diff_rgb[diff_thresholded, :] =red
    difference = create_subplot("sushi1.png","sushi2.png",diff_rgb)
    plt.show()
imgprocessor()