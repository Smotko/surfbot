"""Test lambda function"""

from unittest.mock import MagicMock
from unittest.mock import Mock
from _pytest.monkeypatch import MonkeyPatch
import lambda_function


def test_close() -> None:
    """Test lambda_function.close method"""
    res = lambda_function.close("state", {"content": "message"})
    action = res["dialogAction"]
    assert action["type"] == "Close"
    assert action["fulfillmentState"] == "state"
    assert action["message"] == {"content": "message"}


def test_lambda_handler_throws(monkeypatch: MonkeyPatch) -> None:
    """Test if lambda_handler throws if MSW_API is not defined"""
    log_mock = Mock()
    monkeypatch.setattr(lambda_function.settings, "MSW_API", None)
    monkeypatch.setattr(lambda_function.logger, "error", log_mock)
    res = lambda_function.lambda_handler({}, {})
    assert res is None
    log_mock.assert_called_once()
    log_mock.assert_called_with("Couldn't read SF_MSW_API env variable")


def test_lambda_handler_no_spot(monkeypatch: MonkeyPatch) -> None:
    """Test if error message is displayed when no surf spot given"""
    monkeypatch.setattr(lambda_function.settings, "MSW_API", "my_key")
    res = lambda_function.lambda_handler({
        "bot": {
            "name": "Surfko"
        },
        "userId": "Userko",
        "currentIntent": {
            "name": "Userko"
        }
    }, {})
    assert res is not None
    assert res['dialogAction']['message']['content'] == "Surf spot not found :("


def test_lambda_handler(monkeypatch: MonkeyPatch) -> None:
    """Test the main method of lambda function"""
    read = MagicMock()
    read.read.return_value = '[{"solidRating": 1}]'
    urlopen = MagicMock(return_value=read)  # type: ignore
    monkeypatch.setattr(lambda_function.settings, "MSW_API", "my_key")
    monkeypatch.setattr(lambda_function.urllib.request, "urlopen", urlopen)
    res = lambda_function.lambda_handler({
        "bot": {
            "name": "Surfko"
        },
        "userId": "Userko",
        "currentIntent": {
            "name": "Userko"
        },
        "slots": {
            "SurfSpot": "Carcavelos"
        }
    }, {})
    assert res is not None
    assert res['dialogAction']['message']['content'] == "Number of stars: 1"
