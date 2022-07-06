
from multiprocessing.connection import Client
import glob
from sqlite3 import register_converter
import botocore
#from urllib import response
import boto3
from pprint import pprint
import time
from calendar import c
import csv



resource = boto3.session.Session().resource(service_name = 'ec2', region_name = 'us-east-1')
client = boto3.session.Session().client(service_name='ec2', region_name = 'us-east-1')

def iam_aacountid():
    client = boto3.session.Session().client (service_name = 'sts')
    return client.get_caller_identity().get('Arn')

arn_link = iam_aacountid()


def create_ec2_instances():
    """ 
    Create 3 ec2 instances with needed ec2 components
    """
    instance = resource.create_instances( 
        ImageId='ami-0cff7528ff583bf9a', 
        InstanceType='t1.micro',
        KeyName ='boto3kp',
        MaxCount= 3,
        MinCount= 3,
        #IamInstanceProfile= {'Arn': 'arn_link', 'Name': ''},
    )
    #print(instance)
#     return instance
# created_instance = create_ec2_instances() 
#create_ec2_instances()



def describe_instances():
    """
    describe the created instances and thier the instance id. Image id, instance type, running state, launch time, and instance arn and
    use a csv module to load those information inside
    
    creating a csv file and dumping all the above values to it

    """
    
    resource = boto3.session.Session().resource('ec2', 'us-east-1')
    responses = resource.instances.all()
    for each_response in responses:
        #print(each_response.iam_instance_profile.iam)
        print("----------------------------------------------------")
        print(f"instance state: {each_response.state.get('Name')}\ninstance type: {each_response.instance_type}\nlaunch time: {each_response.launch_time.strftime('%Y-%m-%d %H:%M:%S')}\nimage id: {each_response.image_id, each_response.instance_id}")
        just_ids = each_response.instance_id
        print(just_ids)
        #return (just_ids)

    header = ['name', 'instance id', 'Image id', 'instance type', 'running state', 'launch time', 'instance arn']
    data = [{"instance state":  "instance type":   "launch time":   "image id":  }]


    with open("address.csv", "w") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows()

describe_instances()
#ids = describe_instances()



# def melo_driven_script():
#     """This function is to perform actions like terminate, stop, and start bases on exixting imstances
#     Paremeter: opt(int)
#     return: None
#     """
#     waiter_stop = client.get_waiter('instance_stopped')
#     waiter_running = client.get_waiter('instance_running')
#     waiter_terminate = client.get_waiter('instance_terminated')    
#     print("the above script run these actions on ec2 instance.")
#     print("""
#         1. start
#         2. stop
#         3. terminate
    
#     """)
#     action = int(input("Enter your action"))
#     if action == 1:
#         print("Starting ec2 instances.....")
#         client.start_instances(InstanceIds=ids)
#         waiter_running.wait(InstanceIds=ids)
#         print("instances started!!")
#     elif action == 2:
#         print("stopping ec2 instance...")
#         client.stop_instances(ids)
#         waiter_stop.wait(ids)
#         print("instances stopped!")
#     elif action == 3:
#         print("Terminating instance...")
#         client.terminate_instances(InstanceIds=ids)
#         waiter_terminate.wait(InstanceIds=ids)
#         print("Instance terminated!")

          
#     else:
#         print(f"{action} is invalid. please a valid option and try once again.")
#     return None           
    
    
# melo_driven_script()




def listing_instances():
    """
    listing instances with filter in us-east-1a 
    and  catching any exceptions
    """
    instance_ids = []
    ec2 = boto3.resource('ec2')
    for each_inst in ec2.instances.all():
        instance_ids.append(each_inst) 
    #print(instance_ids)
    #return instance_ids      
#ec2_ids = listing_instances()
    

# def ec2_instance_filter_state():
#     """Get just instances that are running
#     """
#     try:
#         filter_running = {"Name": "instance-state-name", "Values": ["running"]}
#         response = client.instances.filter(Filters=[filter_running])
#         for each_inst in response:
#             for each_id in each_inst.tags:
#                 print(each_id['Value'], each_inst.state.get('Name'), each_inst.instance_id)
#         return None
        
        
    
#     except Exception as e:
# #         print(e)
            

# # ec2_instance_filter_state()       










