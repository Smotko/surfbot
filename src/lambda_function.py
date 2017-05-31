import json
import logging
import urllib.request
import os

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

MSW_API = os.environ.get('SF_MSW_API', None)

if not MSW_API:
  logger.error("Couldn't read SF_MSW_API env variable")


def close(fulfillment_state, message):
    return {
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }


def lambda_handler(event, context):
    logger.debug('event.bot.name={}'.format(event['bot']['name']))
    logger.debug('dispatch userId={}, intentName={}'.format(
        event['userId'], event['currentIntent']['name']))
    j = json.loads(urllib.request.urlopen(
        "http://magicseaweed.com/api/{}/forecast/?spot_id=912".format(
            MSW_API)).read())
    logger.debug('json.response={}'.format(j))

    return close('Fulfilled',
                 {'contentType': 'PlainText',
                  'content': 'This worked! {}'.format(j[0]['solidRating'])})
