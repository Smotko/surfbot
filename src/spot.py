"""Spot"""

import re
from typing import Optional

from spot_db import ALL_SPOTS


def to_msw_id(name: str) -> Optional[int]:
    """Convert spot name to msw api id"""
    for spot in ALL_SPOTS:
        assert isinstance(spot["name"], str)
        if re.search(name, spot["name"], flags=re.IGNORECASE):
            assert isinstance(spot["id"], int)
            return spot["id"]
    return None
