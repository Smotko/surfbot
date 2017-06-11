"""Logger"""

import logging
import settings

# pylint: disable=invalid-name

logger = logging.getLogger("SF_LOGGER")
logger.setLevel(settings.LOG_LEVEL)
