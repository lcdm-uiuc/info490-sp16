import numpy as np
import matplotlib.pyplot as plt

# Get the digit data, and return the data as x, y and images in case 
# we want to show them.

import sklearn.datasets as ds

def get_data():
    # Load the digit data
    digits = ds.load_digits()
    
    x = digits.data
    y = digits.target
    
    i = digits.images
    
    return (x, y, i)

def im_plot(x, y, images):
    
    # First we build an array of the indicaes contianing the first ten images for each digit.
    vals = np.where(y == 0)[0][:10]
    
    for i in range(1, 10):
        vals = np.vstack((vals, np.where(y == i)[0][:10]))
        
    nrows, ncols = vals.shape
    
    plt.figure(figsize=(8.5,8))
    plt.gray()

    # Build a list of the indices in the order I want.
    # plot them, one by one.

    for idx, i in enumerate(vals.T.ravel()):
        ax = plt.subplot(nrows, ncols, idx + 1)
        
        # We want square images
        ax.set_aspect('equal')
        
        # Now show the images, by default pixels are shown as white on black.
        # To show black on white, reverse colormap: cmap=plt.cm.gray_r
        # To smooth pixelated images: interpolation='nearest'
        ax.imshow(images[i])
        
        # No tick marks for small plots
        plt.xticks([]) ; plt.yticks([])
        
        # Only put plot lables over columns
        if idx < 10:
            plt.title(y[i])

def make_ones():
    ones = np.zeros((6, 64))

    for idx in range(6):
        one = np.zeros((8, 8))
        one[1:-1, idx + 1] = 16
    
        ones[idx] = one.ravel()
        
    return(ones)

def make_sevens():
    sevens = np.zeros((3, 64))

    for idx in range(3):
        seven = np.zeros((8, 8))
        seven[1:-1, idx + 4] = 16
        seven[1,idx + 1: idx + 5] = 16
    
        sevens[idx] = seven.ravel()
  
    return(sevens)

# Simple function to plot images of different numbers in a row
def plot_numbers(numbers):

    size = len(numbers)
    plt.figure(figsize=(size,1))
    plt.gray()

    for idx, i in enumerate(numbers):
        ax = plt.subplot(1, size, idx + 1)
        
        # We want square images
        ax.set_aspect('equal')
        
        # Now show the images, by default pixels are shown as white on black.
        # To show black on white, reverse colormap: cmap=plt.cm.gray_r
        # To smooth pixelated images: interpolation='nearest'
        ax.imshow(numbers[idx].reshape(8,8))
        
        # No tick marks for small plots
        plt.xticks([]) ; plt.yticks([])