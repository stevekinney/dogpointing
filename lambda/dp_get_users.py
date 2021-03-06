import boto3
import logging
from boto3.dynamodb.conditions import Key, Attr

logger = logging.getLogger()
logger.setLevel(logging.INFO)
dynamodb = boto3.resource("dynamodb", region_name='us-east-2', endpoint_url="http://dynamodb.us-east-2.amazonaws.com")
table = dynamodb.Table('dp_users')

def lambda_handler(event, context):
    logger.debug('got event{}'.format(event))
    session_key = event['session_key']
    response = table.query(
      KeyConditionExpression=Key('session_key').eq(session_key)
    )
    
    return response["Items"]
