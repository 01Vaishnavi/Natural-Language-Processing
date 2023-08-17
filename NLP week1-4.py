#!/usr/bin/env python
# coding: utf-8

# In[5]:


noise_list=["is","a","this","..."] #21jg1a4222
def _remove_noise(input_text):
    words=input_text.split()
    noise_free_words=[word for word in words if word not in noise_list]
    noise_free_text="".join(noise_free_words)
    return noise_free_words

_remove_noise("once upon a time there is a dog")
    


# In[6]:


#to remove a regex like hashtag pattern
#21jg1a4222
import re

def _remove_regex(input_text,regex_pattern):
    
    urls=re.finditer(regex_pattern,input_text)
    for i in urls:
        input_text=re.sub(i.group().strip(),'',input_text)
    return input_text
regex_pattern="#[\w]*"
_remove_regex("#this #hashtag from the document",regex_pattern)


# In[7]:


#using tokenizer to stem a sentence 21jg1a4222
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.stem import PorterStemmer
def stemSentence(sentence):
    porter = PorterStemmer()
    token_words=word_tokenize(sentence)
    token_words
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)
sentence="Natural Language Processing kit package providid by Natural Language Processing task"
x = stemSentence(sentence)
print(x)


# In[8]:


from nltk.stem import PorterStemmer  #21JG1A4222
from nltk.stem import LancasterStemmer
porter=PorterStemmer()
lancaster=LancasterStemmer()
print("Porter Stemmer")
print(porter.stem("eating"))
print(porter.stem("twisted"))
print(porter.stem("beautifully"))
print("Lancaster Stemmer")
print(lancaster.stem("staying"))
print(lancaster.stem("exaggeration"))
print(lancaster.stem("execution"))


# In[9]:


#a list of words to be stemmed, 21JG1A4222
word_list=["friend","disney","friends","widgets","changes","destabilize","understanding","moonlight","jupiter"]
print("{0:20}{1:20}{2:20}".format("Word","Porter Stemmer","lancaster Stemmer"))
for word in word_list:
    print("{0:20}{1:20}{2:20}".format(word,porter.stem(word),lancaster.stem(word)))
          


# In[15]:


import nltk
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer=WordNetLemmatizer()
sentence="I am buying a new pair of shoes :She likes to paint by herself.she has a bad habit of consuming junk food"
punctuations="?;!.,:"
sentence_words=nltk.word_tokenize(sentence)
for word in sentence_words:
    if word in punctuations:                     #lemmatization 21JG1A4222
        sentence_words.remove(word)
sentence_words
print("{0:20}{1:20}".format("Word","Lemma"))
for word in sentence_words:
    print("{0:20}{1:20}".format(word,wordnet_lemmatizer.lemmatize(word)))


# In[7]:


#pos parameter 21j1a4222
for word in sentence_words:
    print("{0:20}{1:20}".format(word,wordnet_lemmatizer.lemmatize(word,pos='v')))


# In[35]:


import nltk
nltk.download('gutenberg')


# In[12]:


#stemming using corpora 
#21JG1A4222
nltk.corpus.gutenberg.fileids()


# In[8]:


from nltk.stem.snowball import SnowballStemmer
englishStemmer=SnowballStemmer("english")
englishStemmer.stem("melting") #non english stemmers #21jg1a4222


# In[40]:


import nltk
nltk.download('stopwords')


# In[9]:


#stopwords corpus 21jg1a4222
englishStemmer2=SnowballStemmer("english",ignore_stopwords=True)
englishStemmer2.stem("melting")


# In[10]:


spanishStemmer=SnowballStemmer("spanish",ignore_stopwords=True)
spanishStemmer.stem("melting")


# In[4]:


lookup_dict={'rt':'Retweet','dm':'Direct message','awsm':'awesome','luv':'love',"...":'so on'}
def _lookup_words(input_text):
    words=input_text.split()        #21JG1A4222
    new_words=[]
    for word in words:
        if word.lower() not in lookup_dict:
            new_words.append(word)
        else:
            word=lookup_dict[word.lower()]
            new_words.append(word)
    new_text=" ".join(new_words)
    return new_text
_lookup_words("dm me ")


# In[1]:


import nltk
nltk.download('averaged_perceptron_tagger')


# In[13]:


#pos 21JG1A4222
from nltk import word_tokenize, pos_tag
text = "Human language is filled with ambiguities that make it incredibly difficult to write software that accurately determines the intended meaning of text or voice data"
tokens = word_tokenize(text)
print(pos_tag(tokens))

