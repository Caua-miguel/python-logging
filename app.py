from logging.config import dictConfig
from logging import critical, error, warning, info, debug, getLogger #funções
from log.config.config import logging_config

dictConfig(logging_config)

debug("Error, cartao!!!")
warning("Warning, cartao!!!")