import sys

import secret_configs
import logging


LOG_TO_STREAM_LEVEL = logging.INFO
LOG_TO_FILE_LEVEL = logging.ERROR
LOG_TO_FILENAME = './runtime_logs/runtime.log'


def setup_logger() -> logging:
    stream = sys.stdout
    filename = LOG_TO_FILENAME
    filemode = 'a'
    encoding = 'UTF-8'
    log_format = '%(asctime)s - %(name)s:%(levelname)s | %(message)s'
    formatter = logging.Formatter(log_format)

    logger: logging = logging.getLogger('main')
    logger.setLevel(LOG_TO_STREAM_LEVEL)

    stream_handler = logging.StreamHandler(stream)
    stream_handler.setLevel(LOG_TO_STREAM_LEVEL)
    stream_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(filename, filemode, encoding)
    file_handler.setLevel(LOG_TO_FILE_LEVEL)
    file_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger


ENVIRONMENT = secret_configs.ENVIRONMENT

WIFI_SSID = secret_configs.WIFI_SSID
WIFI_PWD = secret_configs.WIFI_PWD

# MQTT SETTINGS
MQTT_TOPIC = secret_configs.MQTT_TOPIC
AWS_IOT_ENDPOINT = secret_configs.AWS_IOT_ENDPOINT
MQTT_PORT = 8883
MQTT_CLIENT_ID = secret_configs.MQTT_CLIENT_ID
MQTT_KEEPALIVE = 60
MQTT_CHECK_MESSAGE_INTERVAL = 0.5
MQTT_PING_INTERVAL = 35

# CREDENTIALS SETUP
AWS_CERT_FILE = secret_configs.AWS_CERT_FILE
AWS_PRIVATE_KEY_FILE = secret_configs.AWS_PRIVATE_KEY_FILE

# LOGGING
logger = setup_logger()
