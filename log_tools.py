# -*- coding=utf-8 -*-

import logging
import logging.handlers


'''
日志模块

使用方式：
from you_logging_filename.py import init_logger
logger = init_logger(__name__)
def you_function():
    logger.info()
    logger.error()
'''


def init_logger(logger_name, log_path='.', total_name='/total.log', error_name='/error.log'):
    if logger_name not in logging.Logger.manager.loggerDict:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        # 全部日志信息, 按天分文件, 保留 7 天
        # 日志格式形如 '2021-03-25 10:24:19,285 - DEBUG - debug message'
        # rf_handler = logging.handlers.TimedRotatingFileHandler(log_path + total_name, when='D', backupCount=7)
        # rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

        # 错误日志信息, 单一文件
        # 日志格式形如 '2021-03-25 10:24:19,285 - ERROR - log_tools.py[:31] - error message'
        f_handler = logging.FileHandler(log_path + error_name)
        f_handler.setLevel(logging.ERROR)
        f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

        # logger.addHandler(rf_handler)
        logger.addHandler(f_handler)
    else:
        logger = logging.getLogger(logger_name)
    return logger


def main():
    logger = init_logger(__name__)

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')


if __name__ == '__main__':
    main()
