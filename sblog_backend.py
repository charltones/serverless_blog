from __future__ import print_function

import boto3
import json
import decimal
import datetime

print('Loading function')


def lambda_handler(event, context):
    '''Provide an event that contains the following keys:

      - operation: 'create' to create a blog post or 'list' to list all posts
      - name: blogger's name for create
      - sblog: blog content, for create
    '''
    #print("Received event: " + json.dumps(event, indent=2))
    operation = event['operation']
    dynamo = boto3.resource('dynamodb').Table('sblog')

    if operation=='create':
        timestamp = decimal.Decimal((datetime.datetime.utcnow() - datetime.datetime.utcfromtimestamp(0)).total_seconds())
        res = dynamo.put_item(Item={'timestamp': timestamp,
                                    'name': event.get('name'),
                                    'sblog': event.get('sblog')})
        # if more than 10 items, trim table
        items = dynamo.scan()
        count = items['Count']
        if count > 10:
            items_to_delete = sorted(items['Items'], key=lambda x: x['timestamp'])[:count-10]
            for i in items_to_delete:
                dynamo.delete_item(Key={
                    'name': i['name'],
                    'timestamp': i['timestamp']
                })
            print("Deleted %d items" % len(items_to_delete))
        return res
    elif operation=='list':
        return dynamo.scan()
    else:
        raise ValueError('Unrecognized operation "{}"'.format(operation))

if __name__=='__main__':
    import sys
    operation = sys.argv[1]
    if operation=="create":
        name = sys.argv[2]
        sblog = sys.argv[3]
    else:
        name = ""
        sblog = ""
    boto3.setup_default_session(profile_name='vertu-ec2', region_name='eu-west-1')
    # Test outside of Lambda
    event = {'operation': operation, 
             'name': name,
             'sblog': sblog
         }
    context = {}
    resp = lambda_handler(event, context)
    print(resp)
