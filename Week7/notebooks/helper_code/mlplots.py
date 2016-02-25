import pandas as pd
import numpy as np
import seaborn as sns

# Convenience function to plot confusion matrix

# This method produces a colored heatmap that displays the relationship
# between predicted and actual types from a machine leanring method.

def confusion(test, predict, names, bins=3, title='Confusion Matrix'):

    # Make a 2D histogram from the test and result arrays
    pts, xe, ye = np.histogram2d(test, predict, bins)

    # For simplicity we create a new DataFrame
    pd_pts = pd.DataFrame(pts.astype(int), index=names, columns=names )
    
    # Display heatmap and add decorations
    sns.set(font_scale=1.0)
    hm = sns.heatmap(pd_pts, annot=True, fmt="d")
    
    sns.set(font_scale=2.0)
    hm.axes.set_title(title, fontsize=24)
    hm.axes.set_xlabel('Predicted', fontsize=24)
    hm.axes.set_ylabel('Actual', fontsize=24)
    sns.set(font_scale=1.0)

    return None
