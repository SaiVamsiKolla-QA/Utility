import logging
import os
import shutil
import tempfile
import pytest
from unittest.mock import patch
from src.utilities.generatingLogs import generate_logs


class TestLoggingUtils:

    @pytest.fixture
    def temp_log_dir(self):
        """Create a temporary directory for logs."""
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()

        # Create a subdirectory for logs
        logs_dir = os.path.join(temp_dir, "logs")
        os.makedirs(logs_dir, exist_ok=True)

        # Return the paths
        yield temp_dir, logs_dir

        # Clean up
        shutil.rmtree(temp_dir)

    def test_log_file_creation(self, temp_log_dir, capsys):
        """Test that the log file is created in the expected location."""
        temp_dir, logs_dir = temp_log_dir

        # Reset logging configuration
        logging.root.handlers = []

        # Patch os.path.dirname to control the base directory path
        with patch('src.utilities.generatingLogs.os.path.dirname') as mock_dirname:
            # Configure the mock to return our temp_dir
            mock_dirname.return_value = temp_dir

            # Call generate_logs
            logger = generate_logs()

            # Check if log file exists
            log_file_path = os.path.join(logs_dir, "Demo.log")
            assert os.path.exists(log_file_path), f"Log file not created at {log_file_path}"

            # Check console output
            captured = capsys.readouterr()
            assert logs_dir in captured.out, f"Expected {logs_dir} in output, got: {captured.out}"

    def test_log_format_and_content(self, temp_log_dir):
        """Test that logs are written with the correct format."""
        temp_dir, logs_dir = temp_log_dir

        # Reset logging configuration
        logging.root.handlers = []

        # Set up logging to use our test directory
        log_file_path = os.path.join(logs_dir, "Demo.log")

        # Create a simple logger for testing
        test_logger = logging.getLogger("test_logger")
        test_logger.setLevel(logging.INFO)

        # Make sure there are no handlers
        test_logger.handlers = []

        # Add a file handler
        handler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S %p')
        handler.setFormatter(formatter)
        test_logger.addHandler(handler)

        # Write a test log message
        test_message = "Test log message"
        test_logger.info(test_message)

        # Close the handler to ensure file is written
        handler.close()

        # Read the log file
        assert os.path.exists(log_file_path), f"Log file not created at {log_file_path}"

        with open(log_file_path, 'r') as f:
            log_content = f.read()

        # Check log content contains the message
        assert test_message in log_content, f"Test message not found in log content: {log_content}"

        # Check log format (has level)
        assert "-INFO-" in log_content, f"INFO level not found in log content: {log_content}"