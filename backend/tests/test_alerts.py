from backend.app.services.alerts import classify_gap

def test_emergency_below_threshold():
    assert classify_gap(39000, 40000)["status"] == "emergency"
def test_critical_at_threshold():
    assert classify_gap(40000, 40000)["status"] == "critical"
def test_warning_five_percent():
    assert classify_gap(42000, 40000)["status"] == "warning"
def test_healthy_above_ten_percent():
    assert classify_gap(44500, 40000)["status"] == "healthy"
def test_invalid_threshold():
    assert classify_gap(100, 0)["status"] == "invalid_threshold"
