from utils.logger import setup_logger

logger = setup_logger()

class DeviceProfile:
    """ 
    Generates basic statistical profile of Modbus register data.
    """

    def __init__(self, registers):
        self.registers = registers or []

    def generate(self):
        if not self.registers:
            logger.warning("No register data for profiling")
            return {}

        total = len(self.registers)
        minimum = min(self.registers)
        maximum = max(self.registers)
        avg = sum(self.registers) / total

        zero_count = self.registers.count(0)
        zero_ratio = zero_count / total

        profile = {
            "total_registers": total,
            "min_value": minimum,
            "max_value": maximum,
            "average_value": avg,
            "zero_ratio": zero_ratio
        }

        logger.info("Device profile generated")
        return profile