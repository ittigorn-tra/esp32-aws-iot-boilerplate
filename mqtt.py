from ssl import PROTOCOL_TLS_CLIENT, SSLContext

from settings import logger
from umqtt.simple import MQTTClient


class Mqtt:
    def __init__(
        self,
        cert_file_path: str,
        private_key_file_path: str,
        callback,
        client_id: str,
        keepalive: int,
        mqtt_endpoint: str,
        mqtt_port: int,
        topic: str,
    ) -> None:
        self._cert_file_path = cert_file_path
        self._private_key_file_path = private_key_file_path
        self._callback = callback
        self._client_id = client_id
        self._keepalive = keepalive
        self._mqtt_endpoint = mqtt_endpoint
        self._mqtt_port = mqtt_port
        self._topic = topic

        self._client = None

        # put together ssl
        ssl_context = SSLContext(PROTOCOL_TLS_CLIENT)
        ssl_context.load_cert_chain(
            self._cert_file_path, self._private_key_file_path)

        try:
            client = MQTTClient(
                client_id=self._client_id,
                server=self._mqtt_endpoint,
                port=self._mqtt_port,
                keepalive=self._keepalive,
                ssl=ssl_context,
            )
            logger.info("Connecting to AWS IoT...")
            client.connect()

        except Exception as e:
            logger.error(f"Unable to connect to MQTT: {e}")
            return None

        self._client = client
        logger.info("Connected to MQTT")

        self._client.set_callback(self._callback)
        logger.info('Callback has been set')

        self._client.subscribe(self._topic)
        logger.info(f'Subscribed to {self._topic}')

    def is_connected(self):
        return self._client is not None

    def wait_for_message(self):
        self._client.wait_msg()

    def check_message(self):
        self._client.check_msg()

    def ping(self):
        self._client.ping()
