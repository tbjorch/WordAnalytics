# standard library
from datetime import datetime
from time import sleep
import logging
from typing import List

# internal modules
from service import threader, sitemap_scraper, rpc
from scraper_service.dto import UrlDTO
# from repository import url_repo

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level="INFO"
    )


def start_service():
    logging.info("Starting scraper service")
    while True:
        now = datetime.now()
        if now.minute % 30 == 0:
            logging.info("Starting sitemap scraper")
            sitemap_scraper.start(f"{now:%Y%m}")
            unscraped_urls: List[UrlDTO] = rpc.get_unscraped_urls()
            url_count = len(unscraped_urls)
            if url_count > 0:
                logging.info(
                    f"Starting content scraper to scrape {url_count} articles"
                    )
                threader.set_scrape_queue(unscraped_urls)
                threader.start_scraper(20)
        sleep(60)
