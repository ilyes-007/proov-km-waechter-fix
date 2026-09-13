# fleet_utils.py
# Formatting and conversion helpers for Vossberg Mobility fleet reports.

KM_TO_MILES: float = 0.621371


def km_to_miles(km: float) -> float:
    """Convert kilometres to miles. Used by the nightly UK partner report."""
    return km * KM_TO_MILES


def format_number(value: float) -> str:
    """Format a number to one decimal place."""
    return f"{value:.1f}"


def format_percent(value: float) -> str:
    """Format a number as a whole-number percentage string."""
    return f"{int(value)}%"
