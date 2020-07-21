import logging.config
from .settings_log import logger_config


logger_config['handlers']['file']['filename'] = 'log/client.log'
logging.config.dictConfig(logger_config)

logger = logging.getLogger('app_loger')
