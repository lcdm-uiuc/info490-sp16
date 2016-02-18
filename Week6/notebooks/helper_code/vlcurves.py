import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def get_range(trn_szs, trn_scr, tst_scr):

    trn_scr_mu = np.mean(trn_scr, axis=1)
    trn_scr_sig = np.std(trn_scr, axis=1)

    trn_high = np.array(trn_scr_mu) + np.array(trn_scr_sig)
    trn_low = np.array(trn_scr_mu) - np.array(trn_scr_sig)

    tst_scr_mu = np.mean(tst_scr, axis=1)
    tst_scr_sig = np.std(tst_scr, axis=1)

    tst_high = np.array(tst_scr_mu) + np.array(tst_scr_sig)
    tst_low = np.array(tst_scr_mu) - np.array(tst_scr_sig)
    
    return(trn_scr_mu, trn_high, trn_low, tst_scr_mu, tst_high, tst_low)


def lv_plot(title, x, y1, y1h, y1l, y2, y2h, y2l, xlbl, ylbl, ylim=None):

    # Plot the results
    sns.set(style="white", font_scale=1.0)
    fig, ax = plt.subplots(figsize=(10,8))

    trn_color = color=sns.xkcd_rgb["denim blue"]
    plt.plot(x, y1, label="Training Score", marker='d', lw=2, color=trn_color)
    plt.fill_between(x, y1h, y1l, alpha=0.2, color=trn_color)

    tst_color = color=sns.xkcd_rgb["medium green"]
    plt.plot(x, y2, label="CV Score", marker='d', lw=2, color=tst_color)
    plt.fill_between(x, y2h, y2l, alpha=0.2, color=tst_color)

    plt.title(title, fontsize=18)

    plt.xlabel(xlbl, fontsize=18)
    plt.ylabel(ylbl, fontsize=18)
    
    if ylim is not None:
        plt.ylim(*ylim)
        
    plt.legend(loc="best", fontsize=18)

    sns.despine(offset=10, trim=True)
    plt.show()