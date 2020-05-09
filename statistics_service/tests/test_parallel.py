from pprint import pprint
from collections import namedtuple, Counter
from functools import reduce
from rpc_mock import article_list_1, article_list_2

Article = namedtuple("Article", ['id', 'headline', 'body', 'created_at'])
article_list = article_list_1 + article_list_2

articles = tuple(Article(id=x["article_id"], headline=x["headline"], body=x["body"], created_at=x["created_at"]) for x in article_list)


def clean_text(article):
    return Counter(
        article.body.replace(".", "")
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


if __name__ == "__main__":
    clean_texts = tuple(map(clean_text, articles))
    print(reduce(lambda x, y: print(x, y), [1, 2, 3, 4, 5]))
    c = Counter()
    for text in clean_texts:
        c.update(text)
    print(c)
    c = Counter()
    count = tuple(reduce(lambda x, y: Counter(x).update(y), clean_texts))
    print(count)
