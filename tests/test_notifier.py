"""Unit tests for Notifier module."""

from src.notifier import Notifier

THRESHOLD = 10
HIGH_VALUE = 15
LOW_VALUE = 5

def test_send_alert() -> None:
    """Test that Notifier sends an alert when the threshold is exceeded."""
    notifier = Notifier(threshold=THRESHOLD)

    assert notifier.send_alert(HIGH_VALUE) == (
    f"Alert! Value {HIGH_VALUE} exceeds threshold {THRESHOLD}"
)

    assert notifier.send_alert(LOW_VALUE) == "Value is within the limit."
