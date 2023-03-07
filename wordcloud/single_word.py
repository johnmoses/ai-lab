"""
Word cloud with a single word
"""

import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = "New Electricity"

# define total rows and total columns
x, y = np.ogrid[:300, :300]

mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
mask = 255 * mask.astype(int)


wc = WordCloud(background_color="black", repeat=True, mask=mask)
wc.generate(text)

plt.axis("off")
plt.imshow(wc, interpolation="bilinear")
plt.show()