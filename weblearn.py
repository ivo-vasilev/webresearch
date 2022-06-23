from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

import requests
import subprocess

LANGUAGE = "english"
SENTENCES_COUNT = 10


def wsay(text):
    subprocess.run('wsay ' + '"' + str(text) + '"')


search = input("Learn about: ")
r = requests.get("https://en.wikipedia.org/w/index.php?search=" + search)
res = r.url

print(res)

url = res
parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
stemmer = Stemmer(LANGUAGE)

summarizer = Summarizer(stemmer)
summarizer.stop_words = get_stop_words(LANGUAGE)

for sentence in summarizer(parser.document, SENTENCES_COUNT):
    print(sentence)
    wsay(sentence)
