#!/usr/bin/env python3

from modules.backup_app import backup_execute
from modules.app_logger import logger_setup

logger_setup()

def main():
    backup = backup_execute()

    if backup:
        print("Script execute..")


if __name__ == "__main__":
    main()