## MEA — Modbus Exposure Analyzer

MEA is a behavioral analysis tool designed to assess the **risk and authenticity of exposed Modbus devices**.

It connects to a target Modbus endpoint, collects register data over time, analyzes entropy and behavioral changes, and produces a risk-oriented report for **penetration testers and blue teams**.

---

## Why MEA?

Many Modbus services exposed to the internet are:

- Misconfigured industrial devices
- Honeypots or research sensors
- Simulators with static datasets
- ICS assets deployed without proper security controls

MEA helps answer:

- Is this a real device or a simulator?
- Is the data dynamic or static?
- How exposed is this system?
- What is the operational risk level?

---

## Features

### Behavioral Analysis
- Multi-sample register collection
- Entropy calculation
- Change-rate analysis
- Detection of:
  - Static datasets
  - Simulators
  - Low-activity devices

### Network Context
- Public vs private detection
- WHOIS / ASN lookup (ipwhois)
- Datacenter identification

### Risk Engine
Combines:
- Exposure level
- Behavioral classification
- Confidence scoring

Outputs a clear **risk assessment**.

### Reporting
- Console summary
- JSON report
- Markdown report

---

## Installation

```bash
git clone https://github.com/404saint/mea.git
cd mea
pip install -r requirements.txt
````

Requirements:

* Python 3.10+
* Network access to target Modbus device

---

## Usage

Run the interactive analyzer:

```bash
python3 mea.py
```

Example:

```
MEA - Modbus Exposure Analyzer
--------------------------------
Enter target IP: 149.12.67.238
```

MEA will:

1. Assess network exposure
2. Connect to Modbus (TCP/502)
3. Collect behavioral samples
4. Analyze entropy and change rate
5. Calculate risk
6. Save:

   * report.json
   * report.md

---

## Example Findings

```
Device classified as: Possible Simulator or Fixed Dataset
Confidence: Medium
Exposure: High (public datacenter)
Risk Level: High
```

---

## Use Cases

### Penetration Testing

* Identify fake ICS targets
* Prioritize real assets
* Validate exposed Modbus services

### Blue Team / Asset Discovery

* Detect unintended internet exposure
* Identify non-operational or static devices
* Support ICS risk assessment

### Research

* Internet-wide Modbus analysis
* Honeypot detection
* Behavioral fingerprinting

---

## Limitations (v1)

* No device fingerprinting
* MAC address not collected (remote targets)
* Limited protocol coverage (Modbus only)
* Single-port focus (502/TCP)
* Basic classification heuristics

---

## Roadmap — v2 (Coming Soon)

Planned improvements:

* Device type guessing (PLC / gateway / simulator)
* MAC/vendor detection (local network)
* Multiple register ranges
* Continuous monitoring mode
* Port scanning for additional services
* Honeypot probability scoring
* Improved risk model
* Better industrial fingerprinting
* CSV reporting
* Passive mode for local networks

---

## Disclaimer

This tool is intended for:

* Authorized security testing
* Defensive security analysis
* Research and education

Do not use MEA against systems without permission.

The author is not responsible for misuse.
