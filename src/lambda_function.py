"""lambda_function.py main entry point for aws lambda"""

import json
import logging
import urllib.request
import os
from typing import Dict, Optional

MSW_API = os.environ.get('SF_MSW_API', None)


def close(fulfillment_state: str, message: Dict[str, str]) -> dict:
    """Close dialog generator"""
    return {
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }


def lambda_handler(event: dict, _: dict) -> Optional[dict]:
    """Lambda Handler
       Entry point for every lambda function call
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.debug('event.bot.name=%s', event['bot']['name'])
    logger.debug('dispatch userId=%s, intentName=%s', event['userId'],
                 event['currentIntent']['name'])

    if not MSW_API:
        logger.error("Couldn't read SF_MSW_API env variable")
        return None

    res = json.loads(urllib.request.urlopen(
        "http://magicseaweed.com/api/{}/forecast/?spot_id=912".format(
            MSW_API)).read())
    logger.debug('json.response=%s', res)

    return close('Fulfilled',
                 {'contentType': 'PlainText',
                  'content': 'This worked! {}'.format(res[0]['solidRating'])})
