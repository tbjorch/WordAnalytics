# Standard library
import os
import logging

# Internal modules
from scraper_service.service.sitemap_scraper import start
from scraper_service.service.manager import start_service


try:
    values = os.environ["INITIAL_VALUES"]
    yearmonth_list = values.split(",")
    for yearmonth in yearmonth_list:
        try:
            start(yearmonth)
        except Exception as e:
            logging.warning(e)
except KeyError as e:
    logging.warning(e)

start_service()
