import nltk

from nltk.stem import WordNetLemmatizer
import re

def cleanResume(resumeText):
    resumeText = removeWord(resumeText)
    resumeText = lemmatize_text(resumeText)
    return resumeText
    
def removeWord(resumeText):
    resumeText = re.sub('http\S+\s', ' ', resumeText)  # remove URLs
    resumeText = re.sub('RT|cc', ' ', resumeText)  # remove RT and cc
    resumeText = re.sub('#\S+', '', resumeText)  # remove hashtags
    resumeText = re.sub('@\S+', '  ', resumeText)  # remove mentions
    resumeText = re.sub('[%s]' % re.escape("""!"#$%&'()+,-./:;<=>?@[]^_`{|}~"""), ' ', resumeText)  # remove punctuations
    resumeText = re.sub(r'[^\x00-\x7f]',r' ', resumeText)
    resumeText = re.sub('\s+', ' ', resumeText)  # remove extra whitespace
    resumeText = resumeText.lower()
    resumeText = re.sub('experience', 'exprience', resumeText)  # change experience to exprience
    return resumeText

def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    return ' '.join([lemmatizer.lemmatize(word) for word in text.split()])