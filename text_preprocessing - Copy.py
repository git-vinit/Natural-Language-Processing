import nltk
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download('punkt')

#input
text = " The English Wikipedia is, with the Simple English Wikipedia, one of two English-language editions of Wikipedia, an online encyclopedia. It was founded on January 15, 2001, as Wikipedia's first edition, and, as of May 24, 2023, has the most articles of any edition, at 6,659,326.[1] As of May 2023, 10.9% of articles in all Wikipedias belong to the English-language edition; this share is down from more than 50% in 2003.[2][3] The edition's one-billionth edit was made on January 13, 2021.[4]"

#creating tokens
tokens=word_tokenize(text)
print(tokens)

#removing punctuations
clean_tokens=[i for i in tokens if i not in punctuation]
print(clean_tokens)

print(len(tokens))
print(len(clean_tokens))


#stemming and limitization
#stemming
stm=PorterStemmer()
print(stm.stem('studied'))
print(stm.stem('playing'))

#limitization
nltk.download('wordnet')
lem=WordNetLemmatizer()
print(lem.lemmatize('wolves'))
print(lem.lemmatize('buggies'))
print(lem.lemmatize('mice'))

lem_tokens= [lem.lemmatize(i) for i in clean_tokens]
print(lem_tokens)


#remove stopwords
nltk.download('stopwords')
stwordlist = stopwords.words("english")
print(stwordlist)
print(len(stwordlist))
clean_tokens=[i for i in clean_tokens if i not in stwordlist]
print(clean_tokens)