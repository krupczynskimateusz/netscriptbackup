#!/usr/bin/env python3
import json
import logging.config
import logging.handlers
from pathlib import Path



def logger_setup():
    config_file = Path("./files/config_logger.json")
    
    with open(config_file) as f:
        config = json.load(f)

    logging.config.dictConfig(config)



if __name__ == "__main__":
    pass