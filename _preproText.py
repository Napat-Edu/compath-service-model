import nltk

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re

junk_word = ('Ltd', 'January', 'Maharashtra', 'Electrical', 'Exprience', 'month', 'Less', 'year', 'Education', 'It', 'using',
             'details', 'company', 'skill', 'engineering', 'college')

def cleanResume(resumeText):
    resumeText = removeWord(resumeText)
    resumeText = lemmatize_text(resumeText)
    resumeText = removeJunk(resumeText)
    return resumeText

def removeJunk(resumeText):
    texts = []
    for word in resumeText.split():
      if word not in set(stopwords.words('english')+['``',"''"]) and (not word.isdigit()) and (word not in junk_word):
        if word.istitle():
          word = word.lower()
        texts.append(word)
    return ' '.join(texts)

def removeWord(resumeText):
    resumeText = re.sub('http\S+\s', ' ', resumeText)  # remove URLs
    resumeText = re.sub('RT|cc', ' ', resumeText)  # remove RT and cc
    resumeText = re.sub('#\S+', '', resumeText)  # remove hashtags
    resumeText = re.sub('@\S+', '  ', resumeText)  # remove mentions
    resumeText = re.sub('[%s]' % re.escape("""%'()!"#$&;<=>?@[]^_`{|}-~"""), ' ',resumeText)
    resumeText = re.sub(r'[^\x00-\x7f]',r' ', resumeText)
    resumeText = re.sub('\s+', ' ', resumeText)  # remove extra whitespace
    return resumeText

def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    return ' '.join([lemmatizer.lemmatize(word) for word in text.split()])