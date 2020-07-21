import logging.config
from .settings_log import logger_config
import os

PATH = os.path.abspath(os.getcwd())
PATH = os.path.join(PATH, 'log/server.log')

logger_config['handlers']['file']['filename'] = PATH
logging.config.dictConfig(logger_config)

logger = logging.getLogger('app_loger')
