import json


def save_json_report(data, filename="report.json"):
    """
    Save analysis data to a JSON file.

    Args:
        data (dict): Data to save
        filename (str): Output file name
    """
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"[INFO] JSON report saved to {filename}")
    except Exception as e:
        print(f"[ERROR] Failed to save JSON report: {e}")
