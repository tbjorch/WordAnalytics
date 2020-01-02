# Internal modules
from statistics_service.app.models import Stopword
from statistics_service.app.repository import stopword_repo


def load_stopwords_into_db():
    stop_word_file = open(
        "utils/new_stop_words.txt",
        "r",
        encoding="latin-1"
    )
    stop_word_list = [(word.split("\n")[0]) for word in stop_word_file]
    for word in stop_word_list:
        if word != "-----------":
            stopword_repo.save(Stopword(word=word))
