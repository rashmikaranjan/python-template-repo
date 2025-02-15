import pytest
from unittest.mock import Mock
from src.calculator import Calculator
from src.logger import Logger
from src.notifier import Notifier

class TestCalculatorLoggerIntegration:
    @pytest.fixture
    def setup_components(self):
        calculator = Calculator()
        mock_notifier = Mock(spec=Notifier)  # Not used but available if needed
        logger = Logger()
        return calculator, logger, mock_notifier

    @pytest.mark.parametrize("operation,a,b,expected", [
        ("add", 5, 3, 8),
        ("subtract", 10, 4, 6),
        ("multiply", 7, 2, 14),
    ])
    def test_calculator_logger_operations(self, setup_components, operation, a, b, expected, caplog):
        calculator, logger, _ = setup_components
        caplog.set_level('INFO')

        result = getattr(calculator, operation)(a, b)  # Perform calculation
        log_message = f"Operation: {operation} {a} and {b}. Result: {result}"
        
        logger.log(log_message)  # Log the operation

        assert result == expected
        assert log_message in caplog.text  # Verify the log message

    def test_calculator_logger_division(self, setup_components, caplog):
        calculator, logger, _ = setup_components
        caplog.set_level('INFO')

        result = calculator.divide(20, 5)
        log_message = f"Operation: divide 20 and 5. Result: {result}"
        
        logger.log(log_message)

        assert result == 4
        assert log_message in caplog.text

    def test_calculator_logger_division_by_zero(self, setup_components, caplog):
        calculator, logger, _ = setup_components
        caplog.set_level('INFO')

        with pytest.raises(ValueError, match="Cannot divide by zero") as exc_info:
            calculator.divide(10, 0)

        log_message = f"Error: {exc_info.value}"
        logger.log(log_message)

        assert "Cannot divide by zero" in str(exc_info.value)
        assert log_message in caplog.text
