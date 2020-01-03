# Standard library
from typing import List
from collections import Counter

# 3rd party modules
# from nltk.corpus import stopwords
# from nltk.stem import SnowballStemmer

# Internal modules
from statistics_service.app.repository import stopword_repo
from statistics_service.app.models.dto import ArticleDTO


def clean_text(article: ArticleDTO) -> ArticleDTO:
    word_list: List[str] = _create_wordlist(article.headline+" "+article.body)
    counter = Counter(word_list)
    counter = _remove_stop_words(counter)
    # counter = _stem_words(counter)
    article.add_clean_text(counter)
    return article


def _create_wordlist(text: str):
    """
    Creates a list of words from a text with delimiters,
    numbers and signs removed.

    Parameters:
    text (str) -- an arbitrary text in string format.

    Returns:
    wordlist (list) -- a list of words (strings)
    """
    text = (
        text.replace(".", "")
        .replace(":", "")
        .replace(",", "")
        .replace(";", "")
        .replace("–", "")
        .replace("-", "")
        .replace("−", "")
        .replace("(", "")
        .replace(")", "")
        .replace("?", "")
        .replace("1", "")
        .replace("2", "")
        .replace("3", "")
        .replace("4", "")
        .replace("5", "")
        .replace("6", "")
        .replace("7", "")
        .replace("8", "")
        .replace("9", "")
        .replace("0", "")
        .replace("✓", "")
        .replace("+", "")
        .replace('"', "")
        .replace("’", "")
        .replace("”", "")
        .replace("…", "")
        .replace("•", "")
        .replace("≈", "")
        .replace("▪", "")
        .replace("#", "")
        .replace("!", "")
        .replace("%", "")
        .replace("&", "")
        .replace("/", "")
        .replace("'", "")
        .replace("@", "")
    )

    wordlist: [] = text.lower().split()
    return wordlist


def _remove_stop_words(c: Counter) -> Counter:
    """
    Cleans list of words from stop words.

    Parameters:
    c (Counter): map of words (strings)

    Returns:
    c (Counter) --  with stop words removed
    """
    stopword_list = [obj.word for obj in stopword_repo.find_all()]
    # stopword_list = stopwords.words('swedish')
    for word in stopword_list:
        c.__delitem__(word)
    return c


def _stem_words(c: Counter) -> Counter:
    # stemmer = SnowballStemmer("swedish")
    word_list = list(c.keys())
    for word in word_list:
        # value = c[word]
        # stemmed_word = stemmer.stem(word)
        c.__delitem__(word)
        # c[stemmed_word] = value
    return c
