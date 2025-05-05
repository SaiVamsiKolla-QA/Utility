# Test Automation Utilities

A collection of reusable utility functions for test automation frameworks. These utilities provide common components for
logging, configuration management, and screenshot capture, designed to be used with Python-based test automation
projects.

## Features

* Centralized logging with customizable output location
* Path resolution for consistent file locations
* Configuration management with config.ini
* Path resolution for consistent file locations

## Prerequisites

* Python 3.9 or higher

## Methods

**1. Logging Utility**

```bash
from utilities.logging_utility import generate_logs

# Initialize logger
logger = generate_logs()

# Use in your tests
logger.info("Test execution started")
logger.warning("Warning message")
logger.error("Error occurred")

# Conditional logging
if condition:
    logger.info("Condition met")
else:
    logger.info("Condition not met")
```

## Project Structure

```
Utility/
├── src/
│   ├── utilities/           # Core utilities package
│   │   ├── __init__.py      # Package initialization
│   │   ├── logging_utils.py # Logging functionality
│   │   ├── config_utils.py  # Configuration reading utilities
│   │   ├── file_utils.py    # File handling utilities
│   │   ├── driver_utils.py  # WebDriver management utilities
│   │   └── report_utils.py  # Reporting and screenshot utilities
│   └── common/              # Common components used across projects
│       ├── __init__.py
│       ├── constants.py     # Shared constants and enums
│       └── exceptions.py    # Custom exception classes
├── tests/                   # Tests for the utilities themselves
│   ├── __init__.py
│   ├── test_logging.py      # Unit tests for logging utilities
│   ├── test_config.py       # Unit tests for config utilities
│   └── test_driver.py       # Unit tests for WebDriver utilities
├── logs/                    # Generated log files
│   └── utility.log          # Main log file

├── docs/                    # Documentation
│   ├── README.md            # Main documentation
├── pyproject.toml           # Poetry configuration
├── poetry.lock              # Poetry lock file (generated)
└── README.md                # Project overview
```

## Installation

The utilities package can be installed using Poetry:

```bash
# Install dependencies
poetry install

# Activate the virtual environment
poetry shell
```
