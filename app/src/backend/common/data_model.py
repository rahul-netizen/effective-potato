from enum import Enum, StrEnum
from typing import Any, Optional

from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict


class ExtendedEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class ExtendedStrEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class BaseModel(PydanticBaseModel):
    """Base model for all data models"""

    model_config = ConfigDict(
        populate_by_name=True,
        # validate_assignment=True,
        from_attributes=True,
        arbitrary_types_allowed=True,
        protected_namespaces=(),
    )


class LoggerConfiguration(BaseModel):
    """Represents the logger configuration"""

    log_level: str


class ServerConfiguration(BaseModel):
    """Represents the server configuration"""

    host: str
    port: str


class Configuration(BaseModel):
    """Represents the configuration"""

    application_name: str
    environment: str
    logger_configuration: LoggerConfiguration
    server_configuration: ServerConfiguration

