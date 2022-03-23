from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

#print(blob)

sentences = blob.sentences#this breaks up the sentences and seperates them

#print(sentences) #we are looking at a list
#breaks it up into two

words = blob.words #split it into words

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

