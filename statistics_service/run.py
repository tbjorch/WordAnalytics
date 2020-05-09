# Standard library
import os
import logging

# Internal modules
from statistics_service.app.controller import (
    statistics_controller as controller
)


try:
    logging.info("Checking for initial values")
    values = os.environ["INITIAL_VALUES"]
    yearmonth_list = values.split(",")
    for yearmonth in yearmonth_list:
        try:
            controller.calculate_yearmonth_data(yearmonth)
        except Exception as e:
            logging.warning(e)
except KeyError as e:
    logging.warning(e)


from statistics_service.app import app  #
