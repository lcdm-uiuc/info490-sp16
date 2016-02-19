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

def make_fakes():
    fakes = np.zeros((16, 64))
    
    for idx in range(fakes.shape[0]):
        fake = np.zeros((8, 8))    
        fakes[idx] = fake.ravel()

    bar = np.zeros((8, 8)) 
    bar[:,0] = 16
    fakes[0] = bar.ravel()
    fakes[1] = np.rot90(bar, 1).ravel()
    fakes[2] = np.rot90(bar, 2).ravel()
    fakes[3] = np.rot90(bar, 3).ravel()

    ell = bar + np.rot90(bar, 1)
    ell[ell > 16] = 16

    fakes[4] = ell.ravel()
    fakes[5] = np.rot90(ell, 1).ravel()
    fakes[6] = np.rot90(ell, 2).ravel()
    fakes[7] = np.rot90(ell, 3).ravel()

    you = ell + np.rot90(bar, 1) + np.rot90(bar, 3)
    you[you > 16] = 16

    fakes[8] = you.ravel()
    fakes[9] = np.rot90(you, 1).ravel()
    fakes[10] = np.rot90(you, 2).ravel()
    fakes[11] = np.rot90(you, 3).ravel()

    atee = bar + np.roll(np.rot90(bar, 1), 4, axis=0)
    atee[atee > 16] = 16

    fakes[12] = atee.ravel()
    fakes[13] = np.rot90(atee, 1).ravel()
    fakes[14] = np.rot90(atee, 2).ravel()
    fakes[15] = np.rot90(atee, 3).ravel()
    
    return(fakes)

# Simple function to plot images of different numbers in a row
def plot_numbers(numbers):
    size = len(numbers)
    plt.figure(figsize=(size,1))
    plt.title('Hello')
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