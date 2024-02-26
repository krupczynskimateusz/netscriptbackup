import logging
from modules.devices.base_device import Device


class Juniper(Device):
    """Juniper device object."""

    def __init__(
            self,
            ip: str,
            port: int,
            name: str,
            vendor: str,
            connection: str,
            username: str,
            password: str,
            mode_cmd: str,
            mode_password: str,
            key_file: str,
            passphrase: str
            ) -> "Device":
        super().__init__(
            ip,
            port,
            name,
            vendor,
            connection,
            username,
            password,
            mode_cmd,
            mode_password,
            key_file,
            passphrase
            )
        self.logger = logging.getLogger("backup_app.devices.Juniper")
        self.logger.debug(f"Device {self.ip} creatad.")
        self.device_type = "juniper"

    def command_show_config(self):
        self.logger.debug(f"{self.ip} - Returning commands.")
        return "show config | display set"

    def config_filternig(self, config):
        self.logger.debug(f"{self.ip} - Configuration filtering.")
        _tmp_config = []
        config = config.splitlines()
        for line in config:
            if "#" in line:
                self.logger.info(f"{self.ip} - Skiping line '{line}'.")
                continue
            _tmp_config.append(line)
        config_to_return = "\n".join(_tmp_config)
        print(type(config_to_return))
        return config_to_return