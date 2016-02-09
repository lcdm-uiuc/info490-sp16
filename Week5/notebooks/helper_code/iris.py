# https://github.com/jakevdp/sklearn_pycon2015
import numpy as np
import seaborn as sns
import pandas as pd

# Get the IRIS data, and perform PCA to restricti data to 
# 2D surface.

from sklearn.decomposition import PCA

def get_data():
    # Load the Iris Data
    iris = sns.load_dataset("iris")
    
    # Now lets get the data and labels
    data = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values
    labels = np.array([i//50 for i in range(iris.shape[0])])
    
    # For now we assume two compponents, to make plotting easier.
    pca = PCA(n_components=2)

    # Fit model to the data
    pca.fit(data)
    
    # Compute the transformed data (rotation to PCA space)
    data_reduced = pca.transform(data)

    return np.concatenate((data_reduced, labels.reshape((150, 1))), axis=1)

# Make a uniformly spaced grid of points across the space occupied by our data
# We assume a datsets is passed into this function that has two dimensions 
# coresponding to x, y

def get_mdata(data, grid_size = 100):
    
    # We grab the min and max of the points, and make the pace a bit bigger.
    # We could make this dynamic.

    x_min, x_max = data[:, 0].min() - .25, data[:, 0].max() + .25
    y_min, y_max = data[:, 1].min() - .25, data[:, 1].max() + .25

    # Meshgrid gives two 2D arrays of the ppoints
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, grid_size),
                         np.linspace(y_min, y_max, grid_size))
    
    # We want to return these points as an array of two-dimensional points
    return np.c_[xx.ravel(), yy.ravel()]

# This method produces a colored scatter plot that displays the intrisic
# clustering of a particular data set. The different types are colored
# uniquely.

import matplotlib.pyplot as plt

# Create Colormaps for the plots
from matplotlib.colors import ListedColormap

def splot_data(data, mdata, z, label1, label2, sz, grid_size = 100): #, xls, yls, sz):

    cmap_back = ListedColormap(sns.hls_palette(3, l=.4, s=.1))
    cmap_pts = ListedColormap(sns.hls_palette(3, l=.9, s=.9))

    sns.set(style="white")
    sns.set(style="ticks", font_scale=2.0)
    fig, ax = plt.subplots(figsize=(10,6))
    ax.set_aspect('equal')

    # Decorate the plot
    ax.set_xlabel(label1)
    ax.set_ylabel(label2)
    
    # We need grid points and values to make the colormesh plot
    xx = mdata[:, 0].reshape((grid_size, grid_size))
    yy = mdata[:, 1].reshape((grid_size, grid_size))
    zz = z.reshape((grid_size, grid_size))

    plt.pcolormesh(xx, yy, zz, cmap=cmap_back)
    
    # Now draw the points, with bolder colors.
    plt.scatter(data[:, 0], data[:, 1], c=data[:, 2], s=sz, cmap=cmap_pts)

    sns.despine(offset=0.25, trim=True)

# This method produces a colored scatter plot that displays the intrisic
# clustering of a particular data set. The different types are colored
# uniquely.

def scplot_data(col1, col2, data, hue_col, label1, label2, xls, yls, sz=8):
    
    # Make the  scatter plot on the DataFrame
    jp = sns.lmplot(col1, col2, data,
                    fit_reg=False, hue=hue_col, size=sz, scatter_kws ={'s': 60})
    
    # Decorate the plot and set limits
    jp.set_axis_labels(label1, label2)

    jp.axes[0,0].set_xlim(xls)
    jp.axes[0,0].set_ylim(yls)

    sns.despine(offset=0, trim=True)
    sns.set(style="ticks", font_scale=2.0)
