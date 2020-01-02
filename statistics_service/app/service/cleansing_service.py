# Standard library
from collections import Counter

# Internal modules
from statistics_service.app.repository import stopword_repo


def create_wordlist(text: str):
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


def remove_stop_words(c: Counter) -> Counter:
    """
    Cleans list of words from stop words.

    Parameters:
    wordlist (list): list of words (strings)

    Returns:
    new_list (list) --  with stop words removed
    len(new_list) (int) -- length of the returned list.
    """
    stopword_list = stopword_repo.get_all_stopwords()
    for word in stopword_list:
        c.__delitem__(word)
    return c
