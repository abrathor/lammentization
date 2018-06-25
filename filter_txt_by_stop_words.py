from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# here we will make method that will take a input text and will remove all stop words from there

def filter_txt_by_stop_word_func(text):

    # so first i have to tokenize the word
    tokens = word_tokenize(text)
    lemmantizer = WordNetLemmatizer()
    lemmantized = [lemmantizer.lemmatize(token.lower()) for token in tokens  if token.isalpha()]
    stop_words = set(stopwords.words("english"))
    return [lemma for lemma in  lemmantized if lemma  not in stop_words]


# filter_txt_by_stop_word_func("the shark is running ")

