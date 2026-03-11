"""
logger.py

Utility module used for configuring logging for the automation framework.

This logger helps in tracking test execution flow, debugging failures,
and maintaining execution logs for analysis.

Features:
 Creates a dedicated logs folder automatically
 Generates timestamp-based log files for each execution
 Records log messages with time, level, and message details
 Used across test files and page objects for consistent logging
"""

import logging
import os
from datetime import datetime


def get_logger():
    """
    Initializes and returns a configured logger instance.

    Functionality:
    - Creates 'logs' directory if it does not exist
    - Generates a unique log file using timestamp
    - Configures logging format and level
    - Attaches file handler to logger

    Returns:
        logger (logging.Logger): Configured logger object
    """

    try:
        # Directory where log files will be stored
        log_dir = "logs"

        # Create logs directory if it doesn't exist
        os.makedirs(log_dir, exist_ok=True)

        # Generate unique log file name with timestamp
        log_file = os.path.join(
            log_dir,
            f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )

        # Get the root logger instance
        logger = logging.getLogger()

        # Set logging level to INFO
        logger.setLevel(logging.INFO)

        # Prevent duplicate log handlers during multiple test runs
        if not logger.handlers:

            # Create file handler to write logs to file
            file_handler = logging.FileHandler(log_file)

            # Define log message format
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )

            # Attach formatter to file handler
            file_handler.setFormatter(formatter)

            # Attach handler to logger
            logger.addHandler(file_handler)

        # Return configured logger
        return logger

    except PermissionError:
        print("ERROR: Permission denied while creating log file.")
        raise

    except OSError as e:
        print(f"ERROR: File system issue while creating logs directory: {e}")
        raise

    except Exception as e:
        print(f"Unexpected error occurred while initializing logger: {e}")
        raise