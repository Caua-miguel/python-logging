# python-logging

Projeto para estudar as configurações de logging no python. Próximo passo vai ser criar uma lib minha com essa configuração para que ela funcione em qualquer projeto. Mas esse caso, ao rodar o programa você
vai gerar alguns logs, eles serão exibidos em json e vai ser criado um arquivo extra sempre que o execeder o limite de 10 kilobytes no arquivo principal.

# Requisitos

- python 3.11.9

## Execução

Para rodar o programa, basta usar o comando:

`python app.py`

Isso vai gerar alguns logs no terminal e gravar eles no arquivo `log/my_app.log.jsonl`

## Modificações

Caso queira testar outras configurações você pode editar o arquivo `log/config/config.json`.

Para retirar informações dos logs você pode adicionar as chaves do construtor `logging.LogRecord` dentro da constante `LOG_RECORD_BUILTIN_ATTRS`.
