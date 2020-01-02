# Standard library
from typing import List

# Internal modules
from statistics_service.app import db
from statistics_service.app.models import Stopword


def save(word: Stopword) -> None:
    db.session.add(word)
    db.session.commit()


def find_all() -> List[Stopword]:
    return Stopword.query.all()
