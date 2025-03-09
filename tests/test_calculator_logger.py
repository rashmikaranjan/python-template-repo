"""Integration tests for Calculator and Logger components."""

from unittest.mock import Mock

import pytest
from pytest import LogCaptureFixture

from src.calculator.calculator import Calculator
from src.logger.logger import Logger
from src.notifier.notifier import Notifier


class TestCalculatorLoggerIntegration:
    """Test suite for Calculator and Logger integration."""

    @pytest.fixture
    def setup_components(self) -> tuple[Calculator, Logger, Notifier]:
        """Set up test components with Calculator, Logger and mocked Notifier."""
        calculator = Calculator()
        mock_notifier = Mock(spec=Notifier)  # Not used but available if needed
        logger = Logger()
        return calculator, logger, mock_notifier

    @pytest.mark.parametrize("operation, a, b, expected", [
        ("add", 5, 3, 8),
        ("subtract", 10, 4, 6),
        ("multiply", 7, 2, 14),
    ])
    def test_calculator_logger_operations \
    (   # noqa: PLR0913
        self, 
        setup_components: tuple[Calculator, Logger, Notifier],
        operation: int, 
        a: int, 
        b: int, 
        expected: int,
        caplog: LogCaptureFixture
    ) -> None:
        """Testing if basic calculator operations are performed and logged correctly."""
        calculator, logger, _ = setup_components
        caplog.set_level('INFO')

        result = getattr(calculator, operation)(
            a, b
        )  # Perform calculation
        log_message = (
            f"Operation: {operation} {a} and {b}. "
            f"Result: {result}"
        )
        
        logger.log(log_message)  # Log the operation

        assert result == expected
        assert log_message in caplog.text  # Verify the log message

    def test_calculator_logger_division \
    (
        self, 
        setup_components: tuple[Calculator, Logger, Notifier], 
        caplog: LogCaptureFixture
    ) -> None:
        """Testing division operation."""
        calculator, logger, _ = setup_components
        caplog.set_level('INFO')

        result = calculator.divide(20, 5)
        expected_result = 4
        log_message = f"Operation: divide 20 and 5. Result: {result}"
        
        logger.log(log_message)

        assert result == expected_result
        assert log_message in caplog.text

    def test_calculator_logger_division_by_zero \
    (
        self, 
        setup_components: tuple[Calculator, Logger, Notifier], 
        caplog: LogCaptureFixture
    ) -> None:
        """Testing if division by zero error is caught and logged correctly."""
        calculator, logger, _ = setup_components
        caplog.set_level('INFO')

        with pytest.raises(ValueError, match="Cannot divide by zero") as exc_info:
            calculator.divide(10, 0)

        log_message = f"Error: {exc_info.value}"
        logger.log(log_message)

        assert "Cannot divide by zero" in str(exc_info.value)
        assert log_message in caplog.text
