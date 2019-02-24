# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:46:39 2019

@author: binuri
"""

import codecs
import re


f = codecs.open("data/ReseaarchPaperData.txt", "r", encoding="ISO-8859-1").read()

f = f.replace(':', '')
f = f.replace(',', ' ')
f = f.replace('.', ' ')

f = f.strip()
regex = re.compile('.*?\((.*?)\)')
print(regex.sub(' ', f))

f = f.replace("'", "")

#regex = re.compile(".*?\((.*?)\)")
#f = re.findall(regex, f)

print("######################################")
 
from nltk.tokenize import sent_tokenize, word_tokenize
tokenized_list = word_tokenize(f)

#print(tokenized_list)


f= open("tokenized_ResearchData.txt","w+")


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
        with open("tokenized_ResearchData.txt", "a") as research_correctData:
            research_correctData.write(word)
            research_correctData.write(' ')

print("tokenized research data")       
print(tokenized_list)
        
        
research_correctData.close()



##################context sensitive word correction    
        
##to do        
        
        
    





    
correct_dataFile = codecs.open('tokenized_ResearchData.txt','r', encoding="utf-8").read()  

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
    

##tf.close()
#f.close()