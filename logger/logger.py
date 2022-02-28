# -*- coding: UTF-8 -*-

import logging.config

from datetime import datetime

logger = None


def initial_logger():
    logging.basicConfig(
        level=logging.INFO,
        filename="./log_backup/" + datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + "_debug.log",
        filemode='w',
        format='%(asctime)s-[%(levelname)s]|[%(filename)s:%(lineno)d][%(module)s][%(funcName)s]|%(message)s'
    )
    global logger
    logger = logging.getLogger()
