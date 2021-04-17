import json
from logging import Logger


def pretty_print_json(json_data: dict, logger: Logger = None,
                      log_level: int = 10):
    """Prints json nicely.

    Instead of printing one long line of the json dictionary this function
    will print the json so that is easy and pleasurable to read. It will look
    like actual json.

    Args:
        json_data (dict): The json data that will be printed.
        logger (Logger, optional): Pass a logger as argument if you want to
          use it instead of normal print().
        log_level (int, optional):
          The log level to be used. Defaults to debug (10). Refer to the docs
          to see all available levels:
          https://docs.python.org/3/library/logging.html#logging-levels
    """
    pretty_json_string = json.dumps(json_data, indent=2)
    if logger is not None:
        logger.log(level=log_level, msg=pretty_json_string)
    else:
        print(pretty_json_string)
