from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image

text='Python is an interpreted, interactive, object-oriented programming language. It incorporates modules, exceptions, dynamic typing, very high level dynamic data types,and classes. It supports multiple programming paradigms beyond object-oriented programming, such as procedural and functional programming.'

wc=WordCloud().generate(text)
plt.imshow(wc)
plt.axis('off')
plt.show()
