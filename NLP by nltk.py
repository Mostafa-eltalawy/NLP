import nltk

from nltk.tokenize import sent_tokenize
text='Trump claims that he had no choice but to risk his own health. Americans disagree.'

#lemmatizer and stemmer
from nltk.stem import PorterStemmer,WordNetLemmatizer

#stemmer  -- give you the root of word 
stemer=PorterStemmer()
print(stemer.stem('Americans'))

#lemmatizer .. give you the word type orgin according to pos 
lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize('claims',pos='v'))

from nltk.corpus import wordnet,stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
stop_words=set(stopwords.words('english'))  # here we defined stop words in english language 

tok_words=word_tokenize(text) # here we made a tokenization for the test .. splitting it to words  
print(tok_words)
#len(stop_words)
#print(stop_words)

#filltering words in text 
#by removing stop words as it is  not importamt words  
words_filltered=[]
for word in tok_words:
    if word not in stop_words:
        words_filltered.append(word)
print(words_filltered) 



