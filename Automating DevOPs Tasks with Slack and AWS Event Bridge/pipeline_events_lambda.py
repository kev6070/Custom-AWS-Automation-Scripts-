import json
from botocore.vendored import requests


def lambda_handler(event, context):
    
    myToken="xoxb-1213987900224-1214029079568-D86NWNbNwKnu1uhZkMvxZKGT"
    url="https://slack.com/api/chat.postMessage"
    
    myMessage= {
        'channel' : 'devops',
        'text' : 'Stage ' + event['detail']['stage'] +' for ' +event['detail']['pipeline'] + ' has ' + event['detail']['state']
    }
    
    headers = {'Content-type': 'application/json', 'Authorization' : 'Bearer ' + myToken}

    rsp = requests.post(url, json=myMessage, headers=headers)
    print (rsp.text)
    