# Project Components

## 1. Calculator

**Location:** `src/calculator.py`

**Description:** Provides basic arithmetic operations.

**Classes:**

- `Calculator`: Contains methods for addition, subtraction, multiplication, and division.

**Methods:**

- `add(a: float, b: float) -> float`: Returns the sum of `a` and `b`.
- `subtract(a: float, b: float) -> float`: Returns the difference between `a` and `b`.
- `multiply(a: float, b: float) -> float`: Returns the product of `a` and `b`.
- `divide(a: float, b: float) -> float`: Returns the quotient of `a` and `b`.

## 2. Logger

**Location:** `src/logger.py`

**Description:** Manages logging of operations.

**Classes:**

- `Logger`: Provides a method to log messages.

**Methods:**

- `log(message: str) -> None`: Logs the provided message.

## 3. Notifier

**Location:** `src/notifier.py`

**Description:** Sends alerts when specified conditions are met.

**Classes:**

- `Notifier`: Checks values against a threshold and sends alerts.

**Methods:**

- `send_alert(value: float) -> str`: Returns an alert message if `value` exceeds the threshold; otherwise, indicates the value is within the limit.
