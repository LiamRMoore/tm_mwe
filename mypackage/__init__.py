import logging
import sys

import timbermafia as tm

from pathlib import Path

LOG_LEVEL = 20

tm.basic_config(
    palette='sensible',
    style='compact',
    stream=sys.stdout,
    level=LOG_LEVEL
)
