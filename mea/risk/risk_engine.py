class RiskEngine:
    """
    Combines analysis and network context into a final risk decision.
    Minimal decision logic for Phase 5.1.
    """

    def evaluate(self, analysis_result, exposure_result):
        """
        analysis_result = {
            "classification": str,
            "confidence": "Low/Medium/High",
            "entropy": float or dict,
            "change_rate": float
        }

        exposure_result = {
            "ip": str,
            "type": "public/private"
        }
        """

        classification = analysis_result.get("classification", "Unknown")
        confidence = analysis_result.get("confidence", "Low")
        change_rate = analysis_result.get("change_rate", 0)

        exposure_type = exposure_result.get("type", "unknown")

        reasoning = []
        risk_score = 0

        # ---- Exposure factor ----
        if exposure_type == "public":
            risk_score += 2
            reasoning.append("Device exposed to public internet")

        # ---- Behavior factor ----
        if change_rate == 0:
            risk_score += 1
            reasoning.append("No register changes detected")

        # ---- Classification factor ----
        if "Simulator" in classification:
            risk_score += 1
            reasoning.append("Device behavior suggests simulator or static dataset")

        # ---- Confidence factor ----
        if confidence == "High":
            risk_score += 1

        # ---- Final risk mapping ----
        if risk_score >= 4:
            overall_risk = "Critical"
        elif risk_score == 3:
            overall_risk = "High"
        elif risk_score == 2:
            overall_risk = "Medium"
        else:
            overall_risk = "Low"

        return {
            "overall_risk": overall_risk,
            "risk_score": risk_score,
            "reasoning": reasoning
        }
