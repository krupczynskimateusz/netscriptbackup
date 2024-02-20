#!/usr/bin/env python3

from modules.backup_app import backup_execute
from modules.my_logging import logger_setup



def main():
    
    logger_setup()
    backup = backup_execute()

    if backup:
        print("Script execute..")


if __name__ == "__main__":
    main()