# builtin packages
from typing import List
import threading
from queue import Queue
import logging

# local modules
from scraper_service.service import content_scraper
# from repository import url_repo


def scraper_thread():
    while True:
        url = scrape_q.get()
        logging.debug("scraping %s" % url.url)
        content_scraper.get_news_content(url)
        scrape_q.task_done()


def set_scrape_queue(url_list: List):
    global scrape_q
    scrape_q = Queue()
    for url in url_list:
        scrape_q.put(url)


def start_scraper(num_of_threads):
    for x in range(num_of_threads):
        t = threading.Thread(target=scraper_thread)
        t.daemon = True
        t.start()
    scrape_q.join()
