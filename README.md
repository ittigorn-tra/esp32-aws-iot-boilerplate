# ESP32 AWS IoT Boilerplate
A project built for enabling ESP32 with Micropython to connect to AWS Iot Core.

# Setting up for the first time

## Create and populate necessary files not included in this repo
Please make sure you have created all the files below brefore attempting to run the code.

### Certificate and private key file
Please create a "thing" in AWS IoT Core and create the files below in your ESP32 device. 
```
creds/private.pem.key
creds/cert.pem.crt
```

### Secret configs
Please create `secret_configs.py` file.
This file is designed to he excluded from the Git repository for security purposes and some configs are machine-specific.
The correct schema of the file can be found in `secret_configs_template.txt`

## Install libraries
Please replace `xxx` placeholders below with real WiFi SSID and password.
```python
import mip
from wlan import Wlan

Wlan(ssid='xxx', pwd='xxx').connect()

mip.install('umqtt.simple')
mip.install('logging')
```
