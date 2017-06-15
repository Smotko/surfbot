"""lambda_function.py main entry point for aws lambda"""

import json
import urllib.request
from typing import Dict, Optional

import settings
from logger import logger
from spot import to_msw_id


def close(fulfillment_state: str, message: Dict[str, str]) -> dict:
    """Close dialog generator"""
    return {
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }


def lambda_handler(event: dict, context: dict) -> Optional[dict]:
    """Lambda Handler
       Entry point for every lambda function call
    """

    logger.debug('event=%s context=%s', event, context)

    if not settings.MSW_API:
        logger.error("Couldn't read SF_MSW_API env variable")
        return None

    spot = event["currentIntent"].get("slots", {}).get("SurfSpot", None)
    spot = to_msw_id(spot) if spot is not None else None

    if not spot:
        logger.error("Couldn't parse spot id")
        return close('Fulfilled',
                     {'contentType': 'PlainText',
                      'content': 'Surf spot not found :('})

    res = json.loads(urllib.request.urlopen(
        "http://magicseaweed.com/api/{}/forecast/?spot_id={}".format(
            settings.MSW_API, spot)).read())
    logger.debug('json.response=%s', res)

    return close('Fulfilled',
                 {'contentType': 'PlainText',
                  'content': 'Number of stars: {}'.format(
                      res[0]['solidRating'])})
