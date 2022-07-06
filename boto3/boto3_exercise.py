
from multiprocessing.connection import Client
from urllib import response
import boto3
from pprint import pprint
import time
from calendar import c
import csv


#pprint(dir(boto3))
#pprint(dir(boto3.session))
'''
session = boto3.session.Session(profile_name = "default")
#pprint(dir(session))
# diff bn client and resource object
# resource = limited , while client works for every 
client = session.client(service_name = "s3")
#pprint(dir(client))
resource = session.resource(service_name = "s3")
#pprint(dir(resource))

def list_bucketWithClient():
    """list all bucket with using client object
    parameter: None
    Return: None
    """
    try:
        response = client.list_buckets()["Buckets"]
        for bucket in response:
            print(f"Bucket name:  {bucket.get('Name')}, Created on: {bucket.get('CreationDate')} ")

    except Exception as err:
        print(err)    


#list_bucketWithClient()



def list_bucketwithResource():
    """list all bucket with using resource object
    parameter: None
    Return: None
    """
    try:
        buckets = resource.buckets.all()
        for bucket in buckets:
            print(f"my bucket name is: {bucket.name}")

    except Exception as e:
        print(e)
    return None    

#list_bucketwithResource()


client = session.resource('iam')
resource = session.client('iam')

def list_rolewithclient():
    """
    
    """
    try:
        response = client.listroles()['Roles']
        for role in response:
            print(f"Role arn: {role.get('Arn')}\nRole Nmae: {role.get('RoleName')}\nRole Description:{role.get('Description')})
    except Exception as err:
        print(err)



def list_rolewithResource():
     try:
        response = 
        #for role in response:
            #print(f"Role Nmae: {role.get('RoleName')}\)
    except Exception as err:
        print(err)       
'''



# session = boto3.session.Session()

# client = session.client('ec2', 'us-east-1')
# resource = session.resource( 'ec2','us-east-1')

def describe_instance_client():
    '''
    
    '''

    client = boto3.session.Session().client('ec2', 'us-east-1')
    response = client.describe_instances()['Reservations']
    for instance in response:
        #pprint(instance.get('Instances'))
        for each_instance in instance.get('Instances'):
            print("-------------------------------")
            print(f"Instance_id: {each_instance.get('InstanceId')}\nLaunchTime is: {each_instance.get('LaunchTime').strftime('%y-%m-%d')}\nInstance Status: {each_instance.get('State').get('Name')}")



#describe_instance_client()



def describe_instance_rsource():
    '''
    this function list instances using resource objects
    parameter: None
    Return: None
    '''
    instance_ids = []
    resource = boto3.session.Session().resource('ec2', 'us-east-1')
    response = resource.instances.all()
    for each_instance in response:
        instance_ids.append(each_instance.id)
    return instance_ids


instance_result = describe_instance_rsource()



def stopping_instances_cli(ids):
    '''
    
    '''

    Client = boto3.session.Session().client('ec2', 'us-east-1')
    print("stopping all instances")
    client.stop_instances(InstanceIds=ids)
    time.sleep(20)
    print("instances stopped")

#stopping_instances_cli(instance_result)

def melo_driven_script():
    '''
    '''

    '''
    Client = boto3.session.Session().client('ec2', 'us-east-1')
    print("
    
    1. start
    2. stop
    3. terminate
    4. exit
    "
    )

    option = int(input("enter a given option above."))
    if option == 1:
        print("starting all instances....")
        client.start_instances(InstanceIds=instance_result)
        time.sleep(20)
        print("starting all instances......")
    elif option == 2:
        print("stopping all instances....")
        client.stop_instances(InstanceIds=instance_result)
        time.sleep(20)
        print("stopping all instances......")
    elif option == 3:
        print("terminating all instances....")
        client.terminate_instances(InstanceIds=instance_result)
        time.sleep(20)
        print("terminated all instances......")
    elif option == 4:
        sys.exit()
    else:
        print(f"{option} is invalid. please provide a valid option and try again")


#melo_driven_script()
'''

