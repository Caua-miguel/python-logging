import logging.config
import logging
import pathlib
import json

def setup_logging():
    config_file = pathlib.Path("./log/config/config.json")
    with open(config_file) as f_in:
        config = json.load(f_in)
    logging.config.dictConfig(config)

def main():
    setup_logging()

    logger = logging.getLogger("my_app")

    logger.debug("debug message", extra={"x": "hello"})
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")

    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("exception message")

if __name__ == "__main__":
    main()