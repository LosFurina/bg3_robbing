from enum import Enum

DELAY = 1

class Point:
    x: int
    y: int

class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    FATAL = "FATAL"