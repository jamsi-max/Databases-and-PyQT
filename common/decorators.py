import os
import inspect
import logging.config
from settings.server_log_config import logger_config


class LogInfo():

    def __init__(self, format=None):
        self.module_call = inspect.stack()[-1].filename
        self.format = format

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            log_file_name = self.module_call.split('.')[0]
            PATH = os.path.join(
                os.path.abspath(os.getcwd()),
                f'log/{log_file_name}.log'
                )
            logger_config['handlers']['file']['filename'] = PATH
            if self.format == 'full':
                logger_config['formatters']['std_format']['format'] = '{asctime}\
 - {levelname} - {module}:{funcName}:{lineno} - {args}- \
{threadName} - {message} !!!'

            logging.config.dictConfig(logger_config)
            logger = logging.getLogger('app_loger')

            logger.info(f'The "{func.__name__}" function is called from the \
module -> {inspect.stack()[-1].filename} -> function:\
{inspect.stack()[-1].code_context[0].strip()}')

            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                logger.exception(f'ERROR NAME: {e}')

        return wrapper
