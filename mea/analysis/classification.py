from utils.logger import setup_logger

logger = setup_logger()

class DeviceClassifier:
    """ # line 6
    Classifies device behavior based on entropy and change rate.
    Confidence is expressed as Low / Medium / High.
    """

    def classify(self, entropy_result, behavior_result):
        entropy = entropy_result.get("entropy", 0)
        change_rate = behavior_result.get("change_rate", 0)

        classification = "Unknown"
        confidence = "Low"

        # Rule-based classification

        if entropy < 1:
            classification = "Static Device"
            confidence = "High"

        elif entropy > 4 and change_rate < 0.01:
            classification = "Possible Simulator or Fixed Dataset"
            confidence = "Medium"

        elif change_rate > 0.2:
            classification = "Active Industrial Process"
            confidence = "High"

        elif 0.01 <= change_rate <= 0.2:
            classification = "Idle or Slow-Changing Process"
            confidence = "Medium"

        else:
            classification = "Low Activity Device"
            confidence = "Low"

        result = {
            "classification": classification,
            "confidence": confidence,
            "entropy": entropy,
            "change_rate": change_rate
        }

        logger.info(f"Device classified as: {classification} (Confidence: {confidence})")
        return result