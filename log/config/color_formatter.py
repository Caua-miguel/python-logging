import logging
from colorlog import ColoredFormatter # pip install colorlog
from typing_extensions import override

class ColorCodes:
    no_style    = '#000000'
    bold        = '#FF5555'
    grey        = '#808080'
    yellow      = '#FFFF55'
    red         = '#FF0000'
    red_light   = '#FF5555'

FORMAT_COLORS = {       
            'DEBUG': ColorCodes.grey,
            'INFO': ColorCodes.no_style,
            'WARNING': ColorCodes.yellow,
            'ERROR': ColorCodes.red,
            'CRITICAL': ColorCodes.red_light + ColorCodes.bold,
}

class ColorFormatter(logging.Formatter):

    def __init__(self, fmt: str):
        super().__init__()
        self.level_to_formatter = {}

    @override
    def format(self, record: logging.LogRecord):
        pass

    def prepare_color_log(self, record: logging.LogRecord):
        pass