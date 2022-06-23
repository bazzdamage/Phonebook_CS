import logging

logger = logging.getLogger('Telephone dictionary')
logger.setLevel(logging.DEBUG)
log_file = logging.FileHandler('logger.log')
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_file.setFormatter(formatter)
logger.addHandler(log_file)


def logger_add_record(lst: list):

    logger.debug(f'Add || Name {lst[0]}, Phone {lst[1]}, Adress {lst[2]}')


def logger_cls():
    with open('logger.log', 'w'):
        pass
