import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from string import punctuation

def input_text(text):
  
    nltk.download('stopwords')

    nltk.download('punkt')

    stop_words = set(stopwords.words('english'))

    stemmer = PorterStemmer()

    lem=WordNetLemmatizer()

    tokens = word_tokenize(text)

    input_tokens = [
        stemmer.stem(token) for token in tokens if token.lower() not in stop_words
    ]

    input_text = input_tokens

    return input_text

text = "The number of articles on the English Wikipedia is shown by the MediaWiki variable {{NUMBEROFARTICLES}}, with all Wikipedias as total {{NUMBEROF|ARTICLES|total}} = 61,146,625.535973 (about 9%) more than the next in rank, the Cebuano Wikipedia. See m:List of Wikipedias.Wikimedia Meta-Wiki (21 September 2008). List of Wikipedias. Archived from the original on 3 November 2015. Retrieved 21 September 2008."
input_text = input_text(text)
print(input_text)

