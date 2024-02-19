#!/usr/bin/env python3

from configparser import ConfigParser
from pathlib import Path
from logging import getLogger



class Config_Load():
    """
    An object that has the necessary functions 
    to load config.ini and validate it.
    """

    def __init__(self):
        self.logger = getLogger("backup_app.config_load.Config_Load")
        self._config = ConfigParser()
        try:
            self._config.read("config.ini")
            self.load_config()

        except Exception as e:
            self.logger.critical("Can't read config.ini file...")
            self.logger.critical(e)
            exit()


    def load_config(self):
        def _get_and_valid_path(path):
            valid_path = Path(path)
            if valid_path.exists():
                return valid_path
            else:
                self.logger.critical(f"{path} doesn't exist.")
                exit()

        try:
            _devices_path = self._config["Application_Setup"]["Devices_Path"]
            self.devices_path = _get_and_valid_path(_devices_path)

            _configs_path = self._config["Application_Setup"]["Configs_Path"]
            _configs_path = _get_and_valid_path(_configs_path)

            self.configs_path = _configs_path

        except KeyError as e:
            self.logger.critical(
                f"Loading mandatory parametrs faild. Not allowed atribute: {e}"
                )
            exit()