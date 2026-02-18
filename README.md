# MEA – Modbus Exposure Analyzer

MEA is a behavioral analysis tool designed to identify exposed, simulated, or non-responsive Modbus devices through passive register analysis.
Future versions will expand network intelligence, passive discovery, and device fingerprinting.

This tool is built for **pentesters, security researchers, and blue teams** working with ICS/OT environments.

---

## Features

* Modbus TCP connectivity (port 502)
* Register collection with rate limiting
* Entropy analysis of register values
* Behavioral change detection over time
* Simulator / fixed-dataset detection
* Public exposure assessment
* IP ownership lookup (WHOIS)
* Risk scoring engine
* Console output
* JSON and Markdown reporting

---

## How It Works

MEA connects to a Modbus device and collects multiple register snapshots.

It then analyzes:

* **Entropy** – randomness of values
* **Change rate** – how values evolve over time
* **Exposure level** – public vs private network
* **Infrastructure context** – ISP / datacenter ownership

The results are combined into a risk evaluation.

---

## Installation

```bash
git clone https://github.com/404saint/mea.git
cd mea
pip install -r requirements.txt
```

---

## Usage

Run the interactive analyzer:

```bash
cd mea
python3 mea.py
```
For clean exit:

```bash
ctrl+z
```

Enter the target IP when prompted.

Reports will be generated:

* `report.json`
* `report.md`

---

## Example Output

```
Device classified as: Possible Simulator or Fixed Dataset
Confidence: Medium
Exposure: Public (Datacenter)
Risk Level: High
```

---

## Use Cases

* Identify exposed Modbus services on the internet
* Detect honeypots or simulated devices
* Validate ICS exposure during penetration tests
* Security monitoring for OT environments

---

## Project Structure

```
core/        Connection and data collection
analysis/    Entropy and behavior analysis
network/     IP context and exposure
risk/        Risk evaluation
reporting/   Output formats
utils/       Logging
```

---

## Security Notice

This tool is intended for **authorized security testing and research only**.

Do not scan or interact with systems without proper permission.

---

## Roadmap (v2 – Coming Soon)

Planned improvements:

* MAC address discovery (local networks)
* Device fingerprinting and vendor guessing
* Passive Modbus function analysis
* Continuous monitoring mode
* Anomaly detection alerts
* ICS asset inventory mode

---

## Author

Security research project focused on practical ICS/OT exposure analysis.

---

## License

MIT License
