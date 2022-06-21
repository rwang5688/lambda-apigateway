import json

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # DEBUG: print event with formattings
    print("event: %s" % json.dumps(event, indent=2))

    # convert queryStringParameters from JSON object to Python dictionary
    queryStringParameters = json.loads(event['queryStringParameters'])
    print("queryStringParameters: %s" % (queryStringParameters))
    
    message = ''
    if 'message' in queryStringParameters:
        message = queryStringParameters['message']

    response = {
        "message": message
    }
    
    print("response: %s" % json.dumps(response, indent=2))

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
