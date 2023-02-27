from wordcloud import WordCloud

# wordcloud depends on numpy and pillow.
# To save the wordcloud into a file, matplotlib 
import numpy as np
import matplotlib.pyplot as plt

import PIL.Image    #Python Image Library
'''
  To load the image, we simply import the image module from the pillow and call the Image. open(), passing the image filename. Instead of calling the Pillow module,
  we will call the PIL module as to make it backward compatible with an older module called Python Imaging Library (PIL).
'''
text=''' Python is an interpreted, interactive, object-oriented programming language. It incorporates modules, exceptions, dynamic typing, very high level dynamic data 
types, and classes. It supports multiple programming paradigms beyond object-oriented programming, such as procedural and functional programming.'''

wc=WordCloud().generate(text)
plt.imshow(wc)
plt.axis('off')
plt.show()
