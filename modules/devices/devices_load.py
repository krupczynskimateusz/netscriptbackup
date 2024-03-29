#!/usr/bin/env python3.10
import logging
import json
from modules.other.functions import get_and_valid_path
from modules.devices.cisco import Cisco
from modules.devices.mikrotik import Mikrotik
from modules.devices.juniper import Juniper


class Devices_Load:
    """
    An object that collects all the functions 
    needed to create device objects.
    """
    def __init__(self) -> None:
        self.logger = logging.getLogger(
            "netscriptbackup.devices.Devices_Load"
            )

    def load_jsons(self, path) -> None:
        """
        This function loads devices from device.json file.
        
        :param path: str path to devices json file.
        """
        try:
            self.logger.debug("Loading basic devices list.")
            with open(path, "r") as f:
                _basic_devs = json.load(f)
            self.devices_data = _basic_devs
            del _basic_devs
        except FileNotFoundError as e:
            self.logger.critical(f"{e}")
            exit()
        except json.decoder.JSONDecodeError as e:
            self.logger.critical(f"{e}")
            exit()
        except Exception as e:
            self.logger.critical(f"{e}")
            exit()

    def create_devices(self) -> None:
        """
        The function is responsible for creating 
        all devices based on the loaded json file
        """
        self.logger.info(f"Creating device objects..")
        devices = self.devices_data
        for ip in devices:
            try:
                _device_parametrs = {
                    "ip": ip,
                    "port": devices[ip]["port"],
                    "name": devices[ip]["name"],
                    "vendor": devices[ip]["vendor"],
                    "connection": devices[ip]["connection"],
                    "username": devices[ip]["username"],
                    "password": devices[ip]["password"],
                    "mode_cmd": "",
                    "mode_password": None,
                    "key_file": None,
                    "passphrase": None
                }
                if devices[ip]["change_mode"] != None:
                    change_mode = devices[ip]["change_mode"]
                    if isinstance(change_mode, list):
                        if change_mode[0] != None:
                            _device_parametrs["mode_cmd"] = change_mode[0]
                        _device_parametrs["mode_password"] = change_mode[1]
                    else:
                        _device_parametrs["mode_password"] = change_mode
                if devices[ip]["key_file"] != None:
                    _device_parametrs["key_file"] = get_and_valid_path(
                        devices[ip]["key_file"]
                        )
                    if _device_parametrs == None:
                        pass
                    _device_parametrs["passphrase"] = devices[ip]["passphrase"]
            except KeyError as e:
                self.logger.warning(f"{ip}:KeyError in devices file: {e}")
                pass
            except Exception as e:
                self.logger.critical(f"Error ocure {e}")
                exit()
            if devices[ip]["vendor"] == "cisco":
                Cisco(**_device_parametrs)
            elif devices[ip]["vendor"] == "mikrotik":
                Mikrotik(**_device_parametrs)
            elif devices[ip]["vendor"] == "juniper":
                Juniper(**_device_parametrs)
            else:
                self.logger.warning(f"{ip}:Device is not supported.")
                pass


if __name__ == "__main__":
    pass