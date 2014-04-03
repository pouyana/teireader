#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

class Logger:
    """
    The logger class, which manages the logging in whole application. It is inhertaed in all other moudles.
    This uses python standard logging class with small changes.
    """
    def __init__(self,level="ERROR"):
        self.logger = logging
        self.logger.basicConfig(format='%(levelname)s:%(message)s', level=self.logging_level(level))
    
    def get_logger(self):
        return self.logger
    
    def logging_level(self,level):
        if (level=="DEBUG"):
            log_level = logging.DEBUG
        elif (level=="INFO"):
            log_level = logging.INFO
        elif (level=="WARNING"):
            log_level = logging.WARNING
        else:
            log_level = logging.ERROR
        return log_level
