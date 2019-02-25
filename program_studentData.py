# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:08:17 2019

@author: binuri
"""

import codecs
import re
import nltk


wc =0
sc =0
tsc =0

#for student feedback data
f = codecs.open("data/studentCourseFeedback.txt", "r", encoding="ISO-8859-1").read()
#print(f)



f = f.replace('<br />', '')
f = f.replace('&#039;',"'")
f = f.replace(')', '')
f = f.replace('(', '')
f = f.replace('..', ' ')
f = f.replace('#', '')
f = f.replace(',', '')
f = f.replace('"', ' ')
f = f.replace('.', ' ')
f = f.replace('?', ' ')
f = f.replace(':', '')
f = f.replace(';', ' ')
f = f.replace('!', '')

              
         
f = f.strip()
regex = re.compile('\s+')
#print(regex.sub(' ', f))


################tokenization
#from nltk.tokenize import sent_tokenize
#tokenized_list = sent_tokenize(f)
#print(tokenized_list)


from nltk.tokenize import word_tokenize
tokenized_list = word_tokenize(f)
print(tokenized_list)


#after tokenize the word count
#for item in f:
#    words = item.split()
#    wc = wc + len(words)
#print(wc)

f= open("tokenized_StudentData.txt","w+")



print('#####part two #######')
##################isolated word correction

from spellchecker import SpellChecker
spell = SpellChecker()

# find those words that may be misspelled
print('mispelled words are')
misspelled = spell.unknown(tokenized_list)
print(misspelled)

for word in tokenized_list:
#    # Get the one `most likely` answer

    if(spell.unknown(tokenized_list)):
        word = spell.correction(word)
        with open("tokenized_StudentData.txt", "a") as student_correctData:
            student_correctData.write(word)
            student_correctData.write(' ')

print("tokenized student data")       
print(tokenized_list)
        
        
student_correctData.close()
##################context sensitive word correction    
        
   
        
        
    






    
correct_dataFile = codecs.open('tokenized_StudentData.txt','r', encoding="utf-8").read()  

print('#####part three stemming #######')    
######stemming   
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()

print(porter_stemmer.stem(correct_dataFile))
print('\n\n')       


######lemetization
print('#####part three lematization #######')
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

print(wordnet_lemmatizer.lemmatize(correct_dataFile))
    

#tf.close()
f.close()