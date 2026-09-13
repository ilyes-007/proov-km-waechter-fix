# test_km_wachter.py
from km_wachter import needs_service, wear_percent


def test_wear_percent_is_correct():
    # 14,900 km of a 15,000 km interval is 99.33...% — the math must NOT floor to 0.
    pct = wear_percent(14900, 15000)
    assert abs(pct - 99.333) < 0.01, f"expected ~99.33%, got {pct}"


def test_almost_due_car_is_flagged():
    # A car at 14,900 of its 15,000 km window is about 99% worn and MUST be flagged.
    assert needs_service({"id": "VOS-4471", "odometer": 14900, "last_service_km": 0}) is True


def test_missing_reading_is_not_treated_as_zero():
    # A car with no last_service_km reading must not be flagged — without a known
    # baseline we cannot measure wear, so we treat it as not due.
    assert needs_service({"id": "VOS-7788", "odometer": 92000}) is False
