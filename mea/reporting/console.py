def print_devices(devices):
    """
    Print discovered devices in a table format.

    devices: list of dicts with keys:
        - ip
        - mac
        - vendor (optional)
    """

    if not devices:
        print("No devices found.")
        return

    print("\nDiscovered Devices")
    print("-" * 60)
    print(f"{'IP Address':<16} {'MAC Address':<20} {'Vendor'}")
    print("-" * 60)

    for device in devices:
        ip = device.get("ip") or "Unknown"
        mac = device.get("mac") or "Unknown"  # Fix: Proper indentation
        vendor = device.get("vendor") or "Unknown"

        print(f"{ip:<16} {mac:<20} {vendor}")  # Line 26: Now correctly indented

    print("-" * 60)
    print(f"Total devices: {len(devices)}\n")