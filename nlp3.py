from pathlib import Path
from textblob import Word
from wordcloud import WordCloud
import imageio
import matplotlib.pyplot as plt

text = Path("RomeoAndJuliet.txt").read_text()
mask_image = imageio.imread("mask_heart.png") #need to be able to read the image by using imread function

wordcloud = WordCloud(colormap="prism",mask=mask_image,background_color="white")

#to generate it
wordcloud = wordcloud.generate(text)
wordcloud = wordcloud.to_file("RomeoJulietHeart.png")

plt.imshow(wordcloud)
plt.show()
print("done")