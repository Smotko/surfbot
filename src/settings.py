"""Settings Module"""

import logging
import os

MSW_API = os.environ.get('SF_MSW_API', None)
LOG_LEVEL = getattr(logging, os.environ.get('SF_LOG_LEVEL', 'DEBUG'))
