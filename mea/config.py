# config.py

# Central configuration for MEA (Modbus Exposure Analyzer)

# ---------------------------

# Network / Modbus Settings

# ---------------------------

MODBUS_PORT = 502
MODBUS_TIMEOUT = 3  # seconds
MODBUS_UNIT_ID = 1
MAX_REGISTERS = 100 # Maximum registers to read in one request
SCAN_DELAY = 0.2 # Delay between requests (seconds)

# Register ranges to collect (start, count)

REGISTER_RANGES = [
(0, 50),      # Holding registers 0–49
(100, 50),    # Holding registers 100–149
]

# Delay between requests (rate limiting)

REQUEST_DELAY = 0.2  # seconds

# ---------------------------

# Scan Behavior

# ---------------------------

MAX_RETRIES = 2

# ---------------------------

# Output

# ---------------------------

OUTPUT_DIR = "reports"
LOG_LEVEL = "INFO"

# ---------------------------

# Risk Scoring Defaults

# ---------------------------

RISK_THRESHOLDS = {
"LOW": 0,
"MEDIUM": 40,
"HIGH": 70,
"CRITICAL": 90,
}
