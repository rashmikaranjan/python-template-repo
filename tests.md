# Running Tests in This Project

This project uses **pytest** for unit and integration testing.

---

## How to Run Tests

To run all **Unit Tests** correctly, please use:

```sh
python -m pytest tests/
```


To run **Integration Tests** correctly, please use:

**For calculator_logger:**

```sh
python -m pytest integration_test/calculator_logger.py
```

or for detailed output:

```sh
python -m pytest -v -s integration_test/calculator_logger.py
```

**For logger_notifier:**

```sh
python -m pytest integration_test/logger_notifier.py
```
or for detailed output:

```sh
python -m pytest -v -s integration_test/logger_notifier.py
```