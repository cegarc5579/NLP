import spacy 

nlp = spacy.load('en_core_web_sm')

document = nlp("In 1994, Tim Berners-Lee founded the World Wide Web Consortium (W3C), devoted to developing web technologies. Stanford Federal Credit Union was the first financial institution to offer online Internet banking services. In 1996, OP Financial Group, also a cooperative bank, became the second online bank in the world and the first in Europe.")
#this goes through the text and identifies different entities in the text
for entity in document.ents:
    print(entity.text,':',entity.label_) #this provides a description and not just a number 
    #this will tell us what an label is, such as 1994 being a data  
    #that's what ent does (i think)

#doing this for the second spacy text file
document2 = nlp("The Mars Orbiter Mission (MOM), informally known as Mangalyaan, was launched into Earth orbit on 5 November 2013 by the Indian Space Research Organisation (ISRO) and has entered Mars orbit on 24 September 2014. India thus became the first country to enter Mars orbit on its first attempt. It was completed at a record low cost of $74 million.")

for entity in document2.ents:
    print(entity.text,':',entity.label_)

#this shows us the similarity between both documents
#we get a .95 which means that they are pretty similar to one another 
#and this suggests that they were written by the same person 
for entity in document.ents:
    print(entity.text, ":", entity.label_)

from pathlib import Path
document1 = nlp(Path("RomeoAndJuliet.txt").read_text())
document22 = nlp(Path("EdwardTheSecond.txt").read_text())

print(document1.similarity(document22))


