from config import MAX_REGISTERS, SCAN_DELAY
from utils.logger import setup_logger
import time

logger = setup_logger()

class RegisterCollector:
    """ 
    Safely collects Modbus register data (read-only).
    """
    def __init__(self, connection, unit_id=1):
        self.connection = connection
        self.client = connection.client
        self.unit_id = unit_id

    def collect_holding_registers(self, start=0, count=MAX_REGISTERS):
        """
        Reads holding registers safely.
        Returns list of values or empty list if failed.
        """

        if not self.connection.is_connected():
            logger.error("Not connected to target")
            return []

        logger.info(
            f"Reading holding registers: start={start}, count={count}"
        )

        try:
            response = self.client.read_holding_registers(
            address=start,
            count=count,
            device_id=self.unit_id
            )

            time.sleep(SCAN_DELAY)

            if response.isError():
                logger.warning("Register read returned Modbus error")
                return []

            values = response.registers
            logger.info(f"Collected {len(values)} registers")
            return values

        except Exception as e:
            logger.error(f"Collection error: {e}")
            return []