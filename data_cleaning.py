import nltk
import re
import string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.tokenize import word_tokenize
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory


#data cleaning
def tweet_cleaning(tweet):
    tweet = tweet.lower()
    tweet = re.sub('\[.*?\]', '', tweet)
    tweet = re.sub('[%s]' % re.escape(string.punctuation), '', tweet)
    tweet = re.sub('\w*\d\w*', '', tweet)
    tweet = re.sub('min', '', tweet)
    return tweet

#Stemming and Stopword Removal
def stemming(tweet):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    data_tweet = stemmer.stem(tweet)
    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()
    data_tweet = stopword.remove(data_tweet)
    return data_tweet

#tokenize
def tokenize(tweet):
    return word_tokenize(tweet)