

import boto3
import botocore
import sys
from pprint import pprint
import time


session = boto3.session.Session()

def list_user_client():
    client = session.client('iam')
    #pprint(dir(client))
    users = client.list_users()['Users']
    for user in users:
        pprint(user)

#list_user_client()


def list_users_withResource():
    resource = session.resource('iam')
    users = resource.users.all()
    #pprint(list(users))
    for user in users:
        print(user.name)

        # iam.create_user(
        #     Path='string',
        #     UserName='string',
        #     PermissionsBoundary='string',
        #     Tags=[{'Key': 'string', 'Value': 'string'}])

#list_users_withResource()





## working with STS(to get account ID)






