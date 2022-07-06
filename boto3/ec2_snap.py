
import boto3
import botocore
import sys
from pprint import pprint


# create service role for lambda function. (attach policy ec2 full access, cloudwatch full access)
# create our lambda function, assign this role to lambda, edit 15m, create 3sec.
# edit configuration set time set for 1m
def landba_handler(event, context):
    return snapshots_size()



resource = boto3.resource(service_name = 'ec2', region_name = 'us-east-1' )

def snapshots_size():
    """ sorting out snapshot sizes of 10gb
    """
    filter_size = {'Name': 'volume-size','Values': ['8']}

    snaps = resource.snapshots.filter(Filters=[filter_size],OwnerIds=[ ''])
    for snap in snaps:
        print("---------------")
        print(f"snapshot_ID: {snap.snapshot_id}\nsnapshot_size: {snap.volume_size}\nsnapshot_creation_time: {snap.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    

snapshots_size()
