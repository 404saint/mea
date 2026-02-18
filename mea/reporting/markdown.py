def save_markdown_report(data, filename="report.md"):
    """
    Save analysis data to a Markdown report.

    Args:
        data (dict): Analysis results
        filename (str): Output file name
    """
    try:
        with open(filename, "w") as f:
            f.write("# MEA Analysis Report\n\n")

            # IP Info
            ip_info = data.get("ip_info", {})
            f.write("## IP Information\n")
            f.write(f"- IP: {ip_info.get('ip', 'N/A')}\n")
            f.write(f"- Type: {ip_info.get('type', 'N/A')}\n")
            f.write(f"- Hostname: {ip_info.get('hostname', 'N/A')}\n")
            f.write(f"- Organization: {ip_info.get('org', 'N/A')}\n\n")

            # Exposure
            exposure = data.get("exposure", {})
            f.write("## Exposure\n")
            f.write(f"- Internet Exposed: {exposure.get('exposed', 'N/A')}\n\n")

            # Behavior / Entropy
            analysis = data.get("analysis", {})
            f.write("## Behavior Analysis\n")
            f.write(f"- Classification: {analysis.get('classification', 'N/A')}\n")
            f.write(f"- Confidence: {analysis.get('confidence', 'N/A')}\n")

            entropy = analysis.get("entropy", {})
            f.write(f"- Entropy: {entropy.get('entropy', 'N/A')}\n")
            f.write(f"- Unique Values: {entropy.get('unique_values', 'N/A')}\n")
            f.write(f"- Change Rate: {analysis.get('change_rate', 'N/A')}\n\n")

            # Risk
            risk = data.get("risk", {})
            f.write("## Risk Assessment\n")
            f.write(f"- Score: {risk.get('score', 'N/A')}\n")
            f.write(f"- Level: {risk.get('level', 'N/A')}\n")

        print(f"[INFO] Markdown report saved to {filename}")

    except Exception as e:
        print(f"[ERROR] Failed to save Markdown report: {e}")
