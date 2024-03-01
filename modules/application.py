#!/usr/bin/env python3.10
import logging
from modules.config_load import Config_Load
from modules.devices.devices_load import Devices_Load
from modules.multithreading import Multithreading
from modules.devices.base_device import BaseDevice
from modules.git_operations import Git
from modules.other.functions import save_to_file


class Application:
    """
    An object that collects functions that manage
    the correct execution of the script.
    """
    def __init__(
            self, 
            configs_path: object
            ) -> None:
        self.logger = logging.getLogger(
            "netscriptbackup.Application"
            )
        self.devices = BaseDevice.devices_lst
        self.configs_path = configs_path

    def _make_backup_ssh(
            self, 
            dev: object
            ) -> bool:
        """
        The functions is responsible for creating bakup with object.

        :param dev: device object,
        :return bool: done or not.
        """
        self.logger.info(f"{dev.ip}:Attempting to create a backup.")
        config_string = dev.get_config()

        if config_string is not None:
            self.logger.debug(f"{dev.ip}:Saving the configuration to a file.")
            done = save_to_file(
                self.configs_path,
                dev.ip,
                dev.name,
                config_string
                )
            if done:
                self.logger.debug(
                    f"{dev.ip}:Operating on the Git repository."
                    )
                _git = Git(dev.ip, dev.name, self.configs_path)
                done = _git.git_exceute()
                if done:
                    self.logger.info(f"{dev.ip}:Backup created.")
                    return True
                else:
                    self.logger.warning(
                        f"{dev.ip}:Unable to create backup."
                        )
                    return False
            else:
                self.logger.warning(f"{dev.ip}:Unable to create backup.")
                return False
        else:
            self.logger.warning(
                f"{dev.ip}:Unable to connect to device."
                )
            return False

    def start_backup(self):
        """
        The function used to implement multithreading in a script.
        """
        self.logger.info(f"Start creating backup for devices.")
        execute = Multithreading()
        execute.execute(self._make_backup_ssh, self.devices)


def _init_system():
    """The function initialize all needed objects."""
    config_loaded = Config_Load()
    config_loaded.set_logging()
    devices_load = Devices_Load()
    devices_load.load_jsons(config_loaded.devices_path)
    devices_load.create_devices()
    return config_loaded.configs_path


def backup_execute():
    """
    The function starts backing up the device configuration.
    """
    conf_path = _init_system()
    app = Application(conf_path)
    app.start_backup()
    return True


def encrypt_file():
    pass


def decrypt_file():
    pass

def show_help():
    pass


if __name__ == "__main__":
    pass