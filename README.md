# python-logging

Projeto para estudar as configurações de logging no python. Próximo passo vai ser criar uma lib minha com essa configuração para que ela funcione em qualquer projeto, apenas para estudar como fazer libs, endendo que seria pouco util uma lib com minhas configurações de log. Mas nesse projeto, ao rodar o programa você vai gerar alguns logs, eles serão exibidos em json e vai ser criado um arquivo extra sempre que o execeder o limite de 10 kilobytes no arquivo principal.

O projeto em si usa as configurações do artigo: 

https://medium.com/@rob-blackbourn/how-to-use-python-logging-queuehandler-with-dictconfig-1e8b1284e27a

Eu apenas repliquei e estou estudando essas configurações para implementar em outros projetos.

## Requisitos

- python 3.11.9

## Execução

Para rodar o programa, basta usar o comando:

`python app.py`

Isso vai gerar alguns logs no terminal e gravar eles no arquivo `log/my_app.log.jsonl`

## Modificações

Caso queira testar outras configurações você pode editar o arquivo `log/config/config.json`

Para retirar informações dos logs você pode adicionar as chaves do construtor refente a classe `logging.LogRecord` dentro da constante `LOG_RECORD_BUILTIN_ATTRS`
