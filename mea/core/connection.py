from pymodbus.client.tcp import ModbusTcpClient
from config import MODBUS_TIMEOUT
from utils.logger import setup_logger

logger = setup_logger()

class ModbusConnection:
    """ 
    Handles safe Modbus TCP connection lifecycle.
    """
    def __init__(self, host, port=502):
        self.host = host
        self.port = port
        self.client = None

    def connect(self):
        """
        Establish connection to Modbus device.
        Returns True if successful.
        """
        logger.info(f"Connecting to {self.host}:{self.port}")

        try:
            self.client = ModbusTcpClient(
                self.host,
                port=self.port,
                timeout=MODBUS_TIMEOUT
            )

            if self.client.connect():
                logger.info("Connection established")
                return True
            else:
                logger.warning("Connection failed")
                return False

        except Exception as e:
            logger.error(f"Connection error: {e}")
            return False

    def is_connected(self):
        if self.client:
            return self.client.connected
        return False

    def close(self):
        """
        Close connection safely.
        """
        if self.client:
            self.client.close()
            logger.info("Connection closed")