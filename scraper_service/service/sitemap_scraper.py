# standard library
import logging
from typing import List

# 3rd party modules
import requests
from requests import Response
from bs4 import BeautifulSoup

# internal modules
from dto import AddUrlDTO, UrlDTO
from scraper_service.service import rpc
from service.error import UnwantedArticleException


def start(yearmonth: str) -> None:
    url_list: List[AddUrlDTO] = get_news_urls_from_sitemap(yearmonth)
    counter: int = 0
    existing_news: List[UrlDTO] = rpc.get_urls_by_yearmonth(yearmonth)
    existing_ids: List[str] = [url.id for url in existing_news]
    for url in url_list:
        if url.id not in existing_ids:
            rpc.post_url(url)
            counter += 1
    logging.info(f"Inserted {counter} URLs to database")


def get_news_urls_from_sitemap(yearmonth: str) -> List[AddUrlDTO]:
    sitemap_url: str = \
        f"https://www.aftonbladet.se/sitemaps/files/{yearmonth}-articles.xml"
    sitemap_content: BeautifulSoup = _fetch_sitemap_as_soup_object(sitemap_url)
    return _scrape_sitemap_soup(yearmonth, sitemap_content, list())


def _scrape_sitemap_soup(
    yearmonth: str,
    soup: BeautifulSoup,
    value_list: List
) -> List[AddUrlDTO]:
    # find all loc tags and extract the news url value into a list
    for item in soup.find_all("loc"):
        try:
            # TODO: ändra till DTO med metod som konverterar till json.
            add_url_dto = AddUrlDTO(
                id=item.get_text().split("/")[
                    item.get_text().split("/").index("a") + 1
                ],
                url=item.get_text(),
                yearmonth=yearmonth,
                undesired_url=False,
            )
            add_url_dto = _check_if_undesired_url(add_url_dto)
            value_list.append(add_url_dto)
        except UnwantedArticleException as e:
            logging.warning(e)
        except Exception as e:
            logging.error(
                f"Error {e} when scraping sitemap for url {item.get_text()}"
                )
    return value_list


def _check_if_undesired_url(add_url_dto: AddUrlDTO):
    undesired_urls = [
        "www.aftonbladet.se/autotest",
        "special.aftonbladet.se",
        "www.aftonbladet.se/nyheter/trafik",
        "www.aftonbladet.se/sportbladet"
    ]
    for string in undesired_urls:
        if string in add_url_dto.url:
            add_url_dto.undesired_url = True
    return add_url_dto


def _fetch_sitemap_as_soup_object(url: str) -> BeautifulSoup:
    page: Response = requests.get(url, timeout=3)
    return BeautifulSoup(page.content, "lxml")
