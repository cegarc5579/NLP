from typing import Text
from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

#print(blob)

sentences = blob.sentences#this breaks up the sentences and seperates them

#print(sentences) #we are looking at a list
#breaks it up into two

words = blob.words #split it into words
'''
#print(words)

#print(blob.tags) #this tells you what the word is like noun/adjectives/verbs and stuff like that 

#print(blob.noun_phrases) #identifies which are noun phrases


#print(blob.sentiment)#analyzes the sentence and gives us information

#how subjective and how positive/negative something is 
#between -1 and 1
#subjective = personal thought
#polarity = rates the negativity positivity 

#print(blob.sentiment.polarity)
#print(blob.sentiment.subjectivity)#these give you independently 
#analyzing on all of the sentences combined 

#for sentence in sentences:
    #print(round(sentence.sentiment.polarity,3)) #going to show different number than above because it's analyzing each sentence independently 
    #the above rounds it to three commas 

from textblob.sentiments import NaiveBayesAnalyzer
blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

print(blob.sentiment)

for sentence in blob.sentences:
    print(sentence.sentiment)
#gives you positive and negative, can say it is a mutual comment because they are so close 

#just translating the sentences to different languages (spanish, chinese, french)
spanish = blob.translate(to="es")

print(spanish)

chinese = blob.translate(to='zh')
print(chinese)

french = blob.translate(to='fr')
print(french)

'''

#change singular words to plural, plural words to singular 
#different methods to change these

from textblob import Word

index = Word('index') #changing this to plural
cacti = Word('cacti') #changing this to singular

print(index.pluralize())
print(cacti.singularize())

#word list
animals = TextBlob('dog cat fish bird').words #pluralizing the list of words that we provided 
print(animals.pluralize())

#spellcheck and corrections
word = Word('theyr')

print(word.spellcheck())#spellcheck method returns words and their confidence level about what we are trying to say

print(word.correct())#correct goes with the word with the highest confidence that is displayed by the function above

word1 = Word('studes')
word2 = Word('varieties')

print(word1.stem()) #these functions take off the end of the word
print(word2.stem())

#print(word1.lemmatize())
#print(word2.lemmatize())