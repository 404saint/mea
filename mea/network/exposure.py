from utils.logger import setup_logger

logger = setup_logger()

# Keywords that indicate cloud / hosting / datacenter
DATACENTER_KEYWORDS = [
    "cloud",
    "hosting",
    "amazon",
    "aws",
    "google",
    "azure",
    "digitalocean",
    "ovh",
    "colo",
    "vps",
    "cogent"
]


def _is_datacenter(org_name):
    if not org_name:
        return False

    org_lower = org_name.lower()

    for keyword in DATACENTER_KEYWORDS:
        if keyword in org_lower:
            return True

    return False


def assess_exposure(ip_info):
    """
    Returns exposure assessment based on IP context.
    """

    ip_type = ip_info.get("type")
    org = ip_info.get("org")

    # Private network → low exposure
    if ip_type == "private":
        result = {
            "exposure_level": "Low",
            "reasons": ["Private network"]
        }
        logger.info("Exposure assessed: Low (private network)")
        return result

    # Public network
    if _is_datacenter(org):
        result = {
            "exposure_level": "High",
            "reasons": ["Public IP", f"Hosted in datacenter: {org}"]
        }
        logger.info("Exposure assessed: High (public datacenter)")
        return result

    result = {
        "exposure_level": "Medium",
        "reasons": ["Public IP"]
    }
    logger.info("Exposure assessed: Medium (public network)")
    return result
