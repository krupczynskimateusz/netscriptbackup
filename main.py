#!/usr/bin/env python3.10

import sys
from modules.application import (
    backup_execute,
    decrypt_file,
    encrypt_file,
    show_help
)

ALL_ARGUMENTS: set[str] = {
    "--backup",
    "-b",
    "--decrypt",
    "-d",
    "--encrypt",
    "-e",
    "--help",
    "-h"
}

ONLY_ONE_ARGUMENTS: set[str] = {
    "--decrypt",
    "-d",
    "--encrypt",
    "-e",
    "--help",
    "-h"
}


def execute_arg(arg: str) -> bool:
    if arg == "--backup":
        print("Started creating backup.")
        if backup_execute():
            print("Backups created.")
            return True
        else:
            print("Can't create backups.")
            return False
    elif arg == "-b":
        print("Started creating backup.")
        if backup_execute():
            print("Backups created.")
            return True
        else:
            print("Can't create backups.")
            return False

    elif arg == "--decrypt":
        print("File decryption has started")
        if decrypt_file():
            print("File decrypted.")
            return True
        else:
            print("Can't decrypt the file.")
            return False
    elif arg == "-d":
        print("File decryption has started")
        if decrypt_file():
            print("File decrypted.")
            return True
        else:
            print("Can't decrypt the file.")
            return False

    elif arg == "--encrypt":
        print("File encryption has started")
        if encrypt_file():
            print("File encrypted.")
            return True
        else:
            print("Can't decrypt the file.")
            return False
    elif arg == "-e":
        print("File encryption has started")
        if encrypt_file():
            print("File encrypted.")
            return True
        else:
            print("Can't decrypt the file.")
            return False

    elif arg == "--help":
        if show_help():
            return True
        else:
            print("Can't show menu.")
        return False
    elif arg == "-h":
        if show_help():
            return True
        else:
            print("Can't show menu.")
            return False


def main():

    argv_lst: list[str] = sys.argv[1:]

    for arg in argv_lst:
        if arg not in ALL_ARGUMENTS:
            print(f"Unknown argument: {arg}")
            exit()
        if arg in ONLY_ONE_ARGUMENTS and len(argv_lst) != 1:
            print(f"{arg} cannot be used with other arguments")
            exit()

    for arg in argv_lst:
        execution = execute_arg(arg)
        if execution:
            print("Script completed.")
        else:
            print("Error ocure.")


if __name__ == "__main__":
    main()