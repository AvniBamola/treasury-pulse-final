def classify_gap(position: float, threshold: float) -> dict:
    if threshold <= 0:
        return {"status": "invalid_threshold", "gap": round(position-threshold, 2)}
    gap = position - threshold
    pct = gap / threshold * 100
    if position < 0 or gap < 0:
        status = "emergency"
    elif pct < 5:
        status = "critical"
    elif pct <= 10:
        status = "warning"
    else:
        status = "healthy"
    return {"status": status, "position": round(position, 2), "threshold": round(threshold, 2),
            "gap": round(gap, 2), "buffer_pct": round(pct, 2)}
