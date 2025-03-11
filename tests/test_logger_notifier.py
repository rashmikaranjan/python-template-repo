"""Integration tests for Logger and Notifier components."""

from unittest.mock import Mock

import pytest
from pytest import LogCaptureFixture

from src.logger.logger import Logger
from src.notifier.notifier import Notifier


class TestLoggerNotifierIntegration:
    """Test suite for Logger and Notifier integration."""

    @pytest.fixture
    def setup_components(self) -> tuple[Mock, Logger, Notifier]:
        """Set up test components with Logger, Notifier and mocked Calculator."""
        mock_calculator = Mock()  # Not used but available if needed
        notifier = Notifier(threshold=10)
        logger = Logger()
        return mock_calculator, logger, notifier

    def test_log_below_threshold \
    (
        self, 
        setup_components: tuple[Mock, Logger, Notifier], 
        caplog: LogCaptureFixture
    ) -> None:
        """Testing logging when value is below notification threshold."""
        _, logger, notifier = setup_components
        caplog.set_level('INFO')

        logger.log("Operation: add 5 and 3. Result: 8")
        alert = notifier.send_alert(8)

        assert "Operation: add 5 and 3. Result: 8" in caplog.text
        assert alert == "Value is within the limit."

    def test_log_above_threshold \
    (
        self, 
        setup_components: tuple[Mock, Logger, Notifier], 
        caplog: LogCaptureFixture
    ) -> None:
        """Testing logging when value exceeds notification threshold."""
        _, logger, notifier = setup_components
        caplog.set_level('INFO')

        logger.log("Operation: multiply 5 and 3. Result: 15")
        alert = notifier.send_alert(15)

        assert "Operation: multiply 5 and 3. Result: 15" in caplog.text
        assert alert == "Alert! Value 15 exceeds threshold 10"

    def test_log_at_threshold \
    (
        self, 
        setup_components: tuple[Mock, Logger, Notifier], 
        caplog: LogCaptureFixture
    ) -> None:
        """Testing logging when value equals notification threshold."""
        _, logger, notifier = setup_components
        caplog.set_level('INFO')

        logger.log("Operation: add 7 and 3. Result: 10")
        alert = notifier.send_alert(10)

        assert "Operation: add 7 and 3. Result: 10" in caplog.text
        assert alert == "Value is within the limit."

    def test_log_error \
    (
        self, 
        setup_components: tuple[Mock, Logger, Notifier],  
        caplog: LogCaptureFixture
    ) -> None:
        """Testing error message logging."""
        _, logger, _ = setup_components
        caplog.set_level('INFO')

        error_message = "Error: Cannot divide by zero"
        logger.log(error_message)
        
        assert error_message in caplog.text
