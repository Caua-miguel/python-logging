from logging import CRITICAL, ERROR, WARNING, INFO, DEBUG #constantes
from logging import basicConfig
from logging import critical, error, warning, info, debug #funções
from logging import FileHandler, StreamHandler

file_handler = FileHandler('log/logs.log', 'a')
file_handler.setLevel(WARNING)

stream_handler = StreamHandler()
# stream_handler.setLevel(DEBUG)

basicConfig(
    level=DEBUG,
    format='%(levelname)s : %(asctime)s : %(message)s',
    handlers=[stream_handler, file_handler]
)

debug("Error, afs!!!")
warning("Warning, afs!!!")