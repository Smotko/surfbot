"""Spot Resolver Test"""

import spot


def test_to_msw_id() -> None:
    """Test if spot resolving works as expected"""
    res = spot.to_msw_id("Carcavelos")
    assert res == 912, \
        "to_msw_id() return expected {} but returned {}".format(912, res)


def test_to_msw_id_case_insensitive() -> None:
    """Test if resolving works even if case does not match"""
    res = spot.to_msw_id("carcavelos")
    assert res == 912, \
        "to_msw_id() return expected {} but returned {}".format(912, res)


def test_to_msw_id_no_spot_found() -> None:
    """Test if returns None when no spot found"""
    res = spot.to_msw_id("invalid spot")
    assert res is None, \
        "to_msw_id() return expected {} but returned {}".format(None, res)
