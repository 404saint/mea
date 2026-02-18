import time

from core.connection import ModbusConnection
from core.collector import RegisterCollector

from analysis.behavior import BehaviorAnalyzer

from network.ip_info import get_ip_info
from network.exposure import assess_exposure

from risk.risk_engine import RiskEngine

from reporting.console import print_devices
from reporting.json_report import save_json_report
from reporting.markdown import save_markdown_report


def main():
    print("MEA - Modbus Exposure Analyzer")
    print("--------------------------------")

    target = input("Enter target IP: ").strip()
    if not target:
        print("No target provided.")
        return

    print("\n[+] Gathering network information...")
    # Fix: Indented the following two lines
    ip_info = get_ip_info(target)
    exposure = assess_exposure(ip_info)

    print("\n[+] Connecting to Modbus...") 
    conn = ModbusConnection(target)

    behavior_result = None

    if conn.connect():
        collector = RegisterCollector(conn)
        behavior = BehaviorAnalyzer(window_size=5)

        print("[+] Collecting behavioral samples...")

        for i in range(5):
            print(f"  Sample {i+1}/5")
            data = collector.collect_holding_registers(start=0, count=50)

            if data:
                result = behavior.add_sample(data)
                if result:
                    behavior_result = result

            time.sleep(1)

        conn.close()
    else:
        print("[-] Modbus connection failed.")

    print("\n[+] Calculating risk...")
    risk_engine = RiskEngine()
    risk = risk_engine.evaluate(behavior_result, exposure)  

    print("\n[+] Summary")
    devices = [{
        "ip": target,
        "mac": None,
        "vendor": ip_info.get("org")
    }]
    print_devices(devices)

    report_data = {
        "target": target,
        "ip_info": ip_info,
        "exposure": exposure,
        "behavior": behavior_result,
        "risk": risk
    }

    print("\n[+] Saving reports...")
    save_json_report(report_data, "report.json")
    save_markdown_report(report_data, "report.md")

    print("[+] Done.")
    print("Reports: report.json, report.md")


if __name__ == "__main__":
    main()