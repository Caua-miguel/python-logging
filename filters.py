from logging import Filter, DEBUG

class Filtro(Filter):
    def filter(self, record):
        if 'cartao' in record.msg:
            record.msg = 'Vazou a senha do cartão!!!'
        if record.levelno == DEBUG:
            return True
        return True
