import logging
from filters import Filtro

logging_config = dict(
    version = 1,
    formatters = {
        'f': {'format': '%(levelname)s : %(asctime)s : %(message)s'}
    },
    filters = {
        'leaked_password': {
            '()': Filtro,
        },
    },
    handlers = {
        'sh': {'class': 'logging.StreamHandler',
                'formatter': 'f',
                'level': logging.DEBUG,
                'filters': ['leaked_password']},
        'fh': {'class': 'logging.FileHandler',
                'filename': 'log/logs.log',
                'mode': 'a',
                'formatter': 'f',
                'level': logging.WARNING,
                'filters': ['leaked_password']},      
    },
    root = {
        'handlers': ['sh', 'fh'],
        'level': logging.DEBUG,
    },
)