# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:32:33 2019

@author: binuri
"""
import codecs
import re
import nltk

#for tweeter data

#f = codecs.open("data\TwitterData.txt", "r", encoding="utf-8").read()
f = codecs.open("data/TwitterData.txt", "r", encoding="ISO-8859-1").read()

#f = f.replace('@', ' ')
#f = f.replace('#', '')
#f = f.replace(',', '')
#f = f.replace('"', ' ')
#f = f.replace('?', ' ')
#f = f.replace(',', ' ')
#f = f.replace('..', '')
#f = f.replace(':', '')

regex = re.compile('\s+')
print(regex.sub(' ', f))

#print(f)
print("######################################")
      
from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()
tokenized_list = tknzr.tokenize(f)

#from nltk.tokenize import sent_tokenize
#tokenized_list = sent_tokenize(f)
print(tokenized_list)

#from nltk.tokenize.toktok import ToktokTokenizer
#tt = ToktokTokenizer()
#tokenized_list = tt.tokenize(f)

#from nltk.tokenize import  word_tokenize
#tokenized_list = word_tokenize(tokenized_list)
#print(tokenized_list)

f= open("tokenized_TwitterData.txt","w+")


print('#####part two #######')
##################isolated word correction

from spellchecker import SpellChecker
spell = SpellChecker()

# find those words that may be misspelled
misspelled = spell.unknown(tokenized_list)

for word in tokenized_list:
#    # Get the one `most likely` answer
    
    if(spell.unknown(tokenized_list)):
        word = spell.correction(word)
        #print(word)
        with open("tokenized_TwitterData.txt", "a") as twitter_correctData:
            twitter_correctData.write(word)
            twitter_correctData.write(' ')

print("tokenized twitter correct Data")       
print(tokenized_list)
        
        
twitter_correctData.close()
##################context sensitive word correction    
        
        
##to do        
        
        
    

    
correct_dataFile = codecs.open('tokenized_TwitterData.txt','r', encoding="utf-8").read()  

print('#####part three #######')    
######stemming   
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()

print(porter_stemmer.stem(correct_dataFile))
print('\n\n')       


######lemetization
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

print(wordnet_lemmatizer.lemmatize(correct_dataFile))
    


