import re

from keras.models import load_model
from keras_preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
import pandas as pd

model_path = './nn/nnlstm_im_ds_epochs_6_acc_0.829.h5'
# model_path = './nn/nnconv_im_ds_epochs_6_acc_0.801.h5'
pretrained_model = load_model(model_path)

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

def preprocess_text(sen):
    '''Cleans text data up, leaving only 2 or more char long non-stepwords composed of A-Z & a-z only
    in lowercase'''
    
    sentence = sen.lower()

    sentence = remove_tags(sentence)
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence) 
    sentence = re.sub(r'\s+', ' ', sentence)  

    # Remove Stopwords
    pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
    sentence = pattern.sub('', sentence)

    return sentence

news = pd.read_csv("./nn/a1_IMDB_Dataset.csv")
X = []
sentences = list(news["review"])
for sen in sentences:
    X.append(preprocess_text(sen))
y = news['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
word_tokenizer = Tokenizer()
word_tokenizer.fit_on_texts(X_train)

nltk.download('stopwords')


def categorize(news_data):
    unseen_processed = []
    for n in news_data:
        guess = preprocess_text(n)
        unseen_processed.append(guess)
    unseen_tokenized = word_tokenizer.texts_to_sequences(unseen_processed)
    unseen_padded = pad_sequences(unseen_tokenized, padding='post', maxlen=100)
    unseen_sentiments = pretrained_model.predict(unseen_padded)
    
    return ([float(i[0]) for i in unseen_sentiments])