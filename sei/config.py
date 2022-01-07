import configparser
from loguru import logger

parser = configparser.ConfigParser()
try:
    parser.read(r'./config.cfg')
except:
    logger.error("Please fill out a config.cfg file according to specifications.")
    exit()

try:
    prefix = parser.get('Bot', 'prefix')
    if prefix=='':
        raise Exception('Missing prefix in config.cfg')
except:
    logger.error('Please enter `prefix = &` in [Bot] in config.cfg.')
    exit()

try:
    token = parser.get('Discord', 'token')
    if token=='':
        raise Exception('Missing Discord token in config.cfg.')
except:
    logger.error('Please enter `token = TOKEN` in [Discord] in config.cfg.')
    exit()
