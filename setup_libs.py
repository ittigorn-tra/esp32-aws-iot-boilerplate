import mip
from settings import WIFI_PWD, WIFI_SSID
from wlan import Wlan

print('Attempting to connect to WiFi')
wlan = Wlan(ssid=WIFI_SSID, pwd=WIFI_PWD)
wlan.connect()
print('Connected')

libs = ['umqtt.simple']

for lib in libs:
    print(f'Installing {lib}')
    mip.install(lib)
