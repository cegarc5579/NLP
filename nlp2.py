from typing import Text
from numpy import sort
from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd 


nltk.download("stopwords")
from nltk.corpus import stopwords


stops = stopwords.words("english")
print(stops)

blob = TextBlob("Today is a beautiful day.")
print(blob.words)


cleanlist = [word for word in blob.words if word not in stops]

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

print(blob.word_counts['juliet']) #should come out 178 with a lower case j 
print(blob.word_counts['romeo'])#should come out 299 times 

#could count noun phrases

#print(blob.noun_phrases.cont("lady capulet"))#takes a little longer 
#should return 46

more_stops = ['thee','thy','thou']
stops += more_stops

items = blob.word_counts.items()
print(items) #items method prints out a list of words and the number of times it appears in text 

# use a list comprehendsion to eliminate any tuples
# containing stop words:
items = [i for i in items if i[0] not in stops]
print(items[:10])

from operator import itemgetter

sorted_items = sorted(items)
print(sorted_items[:10]) #does it by the word and not by the count, but we want it to be sorted by the count

sorted_items = sorted(items, key=itemgetter(1), reverse=True)
print(sorted_items[:10])

top20 = sorted_items[:20]

df = pd.DataFrame(top20, columns=["words","Count"])

print(df)

import matplotlib.pyplot as plt #why isn't this workign????????

df.plot.bar(x="words", y="Count", legend=False)
plt.gcf().tight_layout()
plt.show()