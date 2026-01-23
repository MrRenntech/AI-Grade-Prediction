def risk_scoring(probabilities):
    """
    probabilities: model.predict_proba()[0]
    Index mapping (as trained):
    0 -> Low Risk / Safe
    1 -> Medium Risk
    2 -> High Risk
    """

    high_risk_prob = probabilities[2]
    medium_risk_prob = probabilities[1]

    if high_risk_prob >= 0.75:
        return {
            "risk_level": "HIGH RISK",
            "confidence": "HIGH",
            "risk_score": round(high_risk_prob, 2),
            "recommended_action": "Immediate academic intervention required"
        }

    elif high_risk_prob >= 0.50 or medium_risk_prob >= 0.60:
        return {
            "risk_level": "MEDIUM RISK",
            "confidence": "MODERATE",
            "risk_score": round(max(high_risk_prob, medium_risk_prob), 2),
            "recommended_action": "Monitor student performance and provide support"
        }

    else:
        return {
            "risk_level": "LOW RISK",
            "confidence": "LOW",
            "risk_score": round(high_risk_prob, 2),
            "recommended_action": "No immediate action required"
        }
