import ipaddress
import socket
from ipwhois import IPWhois


def _is_private(ip):
    return ipaddress.ip_address(ip).is_private


def _resolve_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return None


def _get_whois_org(ip):
    try:
        obj = IPWhois(ip)
        result = obj.lookup_rdap(depth=1)

        org = None

        # Prefer ASN description (usually cleaner)
        if result.get("asn_description"):
            org = result["asn_description"]
        else:
            network = result.get("network", {})
            org = network.get("name")

        return org
    except Exception:
        return None


def get_ip_info(ip):
    info = {
        "ip": ip,
        "type": "private" if _is_private(ip) else "public",
        "hostname": None,
        "org": None
    }

    # Hostname
    info["hostname"] = _resolve_hostname(ip)

    # WHOIS only for public IPs
    if info["type"] == "public":
        info["org"] = _get_whois_org(ip)

    return info
