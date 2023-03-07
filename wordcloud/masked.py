"""
Masked text
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from os import path 
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
text = open(path.join(d, 'pg1112.txt')).read()

c_mask = np.array(Image.open(path.join(d, "result1.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="black", max_words=2000, mask=c_mask,
               stopwords=stopwords, contour_width=3, contour_color='steelblue')

# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "cmask.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(c_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
