import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud

def make_wc(text, title=''):

    wc = WordCloud(background_color="white", max_words=1000)

    # generate word cloud
    wc.generate(text)

    plt.imshow(wc)
    plt.axis("off")
    plt.title(title, fontsize=24)
    plt.show()