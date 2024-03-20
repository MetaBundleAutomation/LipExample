import logging

from core.config import settings

formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s",
    "%d/%m/%Y %I:%M:%S %p",
)

logger = logging.getLogger(settings.service_name)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.propagate = False