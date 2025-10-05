"""
Logging configuration for JobScanner Pro.
"""

import logging
from pathlib import Path

def setup_logger(level="INFO", log_file=None):
    """
    Setup logging configuration
    
    Args:
        level (str): Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file (str, optional): Path to log file
    """
    # Convert string level to logging constant
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    
    # Basic configuration
    config = {
        "level": numeric_level,
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "datefmt": "%Y-%m-%d %H:%M:%S"
    }
    
    # Add file handler if log file specified
    if log_file:
        # Create log directory if it doesn't exist
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Add file handler configuration
        config["filename"] = log_file
        config["filemode"] = "a"  # Append mode
        
        # Also log to console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(
            logging.Formatter("%(levelname)s: %(message)s")
        )
        logging.getLogger().addHandler(console_handler)
    
    # Apply configuration
    logging.basicConfig(**config)
    
    # Test logger
    logger = logging.getLogger(__name__)
    logger.debug("Logging initialized") 