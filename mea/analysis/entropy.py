import math
from collections import Counter
# Removed the import as it's not a standard library and not provided
# from utils.logger import setup_logger
# For demonstration purposes, we'll create a simple logger
class SimpleLogger:
    def warning(self, msg):
        print(f"WARNING: {msg}")

    def info(self, msg):
        print(f"INFO: {msg}")

logger = SimpleLogger()

class EntropyAnalyzer:
    """ # Corrected indentation
    Calculates Shannon entropy of Modbus register data.
    """

    def __init__(self, registers):
        self.registers = registers or []

    def calculate(self):
        if not self.registers:
            logger.warning("No register data for entropy analysis")
            return {
                "entropy": 0,
                "unique_values": 0
            }

        total = len(self.registers)
        counts = Counter(self.registers)

        entropy = 0
        for count in counts.values():
            probability = count / total
            entropy -= probability * math.log2(probability)

        result = {
            "entropy": entropy,
            "unique_values": len(counts)
        }

        logger.info(f"Entropy calculated: {entropy:.3f}")
        return result