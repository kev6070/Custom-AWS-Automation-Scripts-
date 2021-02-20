import json
from botocore.vendored import requests


def lambda_handler(event, context):
    
    myToken="xoxb-1213987900224-1214029079568-D86NWNbNwKnu1uhZkMvxZKGT"
    url="https://slack.com/api/chat.postMessage"
    
    myMessage= {
        'channel' : 'devops',
        'text' : event['detail']['repositoryName'] + ' has been updated. CommitID is: ' + event['detail']['commitId']
    }
    
    headers = {'Content-type': 'application/json', 'Authorization' : 'Bearer ' + myToken}

    rsp = requests.post(url, json=myMessage, headers=headers)
    print (rsp.text)