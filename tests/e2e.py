"""End to end tests for Calculator, Logger & Notifier."""

from pathlib import Path

import pytest

from src.calculator.calculator import Calculator
from src.logger.logger import Logger
from src.notifier.notifier import Notifier


@pytest.fixture
def setup_objects() -> tuple[Calculator, Logger, Notifier]:
    """Fixture to set up the necessary objects for the test."""
    calculator = Calculator()
    logger = Logger()
    notifier = Notifier(threshold=100)  # Set threshold to 100 for testing
    return calculator, logger, notifier

def test_calculation_log_and_notify \
(setup_objects: tuple[Calculator, Logger, Notifier]) -> None:
    """Test that calculation is performed.
    
    Logged, and notification is sent when the threshold is exceeded.
    """
    # Unpack the objects from the fixture
    calculator, logger, notifier = setup_objects

    a = 50
    b = 60
    expected_result = 110

    # Step 1: Perform the calculation
    result = calculator.add(a, b)
    
    # Step 2: Log the operation
    operation_message = f"Added {a} and {b} to get {result}"
    logger.log(operation_message)

    # Step 3: Send a notification if the result exceeds the threshold
    alert_message = notifier.send_alert(result)

    # Assertions:
    # 1. Check if the calculation result is correct
    assert result == expected_result

    # 2. Check if the send_alert method returned the correct alert message
    assert alert_message == f"Alert! Value {expected_result} exceeds threshold 100"
    
    # 3. Check the log file to verify the operation was logged
    with Path("operations.log").open() as log_file:
        log_content = log_file.read()

    # Verify that the content of the log file matches the expected message
    assert operation_message in log_content
