from common.variables import DEFAULT_ENCODING


logger_config = {
    'version': 1,
    'disable_existing_loggers': False,  # use only current loggers

    'formatters': {
        'std_format': {
            # 'format': '{asctime} - {levelname} - {module}:{funcName}:{lineno} - {args}- {threadName} - {message}',
            'format': '{asctime} - {message}',
            'style': '{'
        }
    },
    # 'handlers': {
    #     'file': {
    #         'class': 'logging.FileHandler',
    #         'level': 'DEBUG',
    #         'formatter': 'std_format'
    #     }
    # },
    'handlers': {
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'encoding': DEFAULT_ENCODING,
            'interval': 1,
            'when': 'D',
            'level': 'DEBUG',
            'formatter': 'std_format'
        }
    },
    'loggers': {
        'app_loger': {
            'level': 'DEBUG',
            'handlers': ['file']
            # 'propagate': False  # disable send message top to root logger
        }
    },

    # 'filters': {},
    # 'root': {}, # '': {} root logger
    # 'incremental': True # если есть ещё где-то логер это будут доп настройки
}
