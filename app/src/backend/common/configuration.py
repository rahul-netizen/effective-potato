"""Implements the default configuration"""

import configparser
import os

from common.data_model import Configuration as ConfigurationModel


class Configuration:
    """Represents the default configuration"""

    def __init__(self):
        config_obj = {
            "application_name": os.environ.get("APPLICATION_NAME", "Effective Potato"),
            "environment": os.environ.get("ENVIRONMENT", "development"),
            "logger_configuration": {"log_level": os.environ.get("LOG_LEVEL", "DEBUG")},
            "server_configuration": {
                "host": os.environ.get("HOST", "0.0.0.0"),  # nosec
                "port": os.environ.get("PORT", "8082"),  # nosec
            }
        }
        self._configuration = ConfigurationModel(**config_obj)
        # self._config = configparser.ConfigParser()  # Read the config.ini file
        # self._config.read(os.environ.get("CONFIG_INI_PATH"))

    def configuration(self):
        """Returns the configuration"""
        return self._configuration

    def config_ini(self):
        """Returns the config from ini file"""
        return self._config


# Initialize the Configuration instance
# config = Configuration()

# Export the methods as standalone functions
# def get_configuration():
#     return config.configuration()

# def get_config_ini():
#     return config.config_ini()
