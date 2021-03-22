from rake_nltk import Rake, Metric
from nltk.corpus import stopwords
import os 

def get_best(text):
    text = str(text).lower()

    nltk_stop = stopwords.words('english')
    r = Rake(ranking_metric=Metric.DEGREE_TO_FREQUENCY_RATIO,
        stopwords=nltk_stop,
        punctuations='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
    ) 
    

    text = text
    r.extract_keywords_from_text(text)

   

    return r.get_ranked_phrases_with_scores() 

def checkKeywords(data):
    '''
    find ways to use these key words

    options -> use this only if the discription is long more than 100 words
    -> otherwise compare all the words in the symtoms to the json data file (brute force)

    '''
    pass


