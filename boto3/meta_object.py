
from urllib import response
import boto3
from pprint import pprint
import time


client = boto3.session.Session().client('ec2', 'us-east-1')


def using_meta_object():
    '''
    
    '''
    region = []    
    resource = boto3.session.Session().resource('ec2', 'us-east-1')
    #pprint(dir(resource.meta.client))

    for each_region in resource.meta.client.describe_regions().get('Regions'):
        region.append(each_region['RegionName'])
    print(len(region), region)

#using_meta_object()



def ec2_instance_id():
    ids = []
    resource = boto3.session.Session(profile_name="shared").resource(service_name='ec2', region_name='us-east-1')
    for all_ids in resource.instances.all():
        ids.append(all_ids.id)
    print(ids)    
    
    
#ec2
def ec2_instance_with_filter():
    ids = []
    resource = boto3.session.Session().resource(service_name='ec2', region_name='us-east-1')
    for all_ids in resource.instances.limit(1):
        ids.append(all_ids.id)
    print(ids)

#ec2_instance_with_filter()



def describe_instance_rsource():
    '''
    this function list instances using resource objects
    parameter: None
    Return: None
    '''

    client = boto3.session.Session().client('ec2', 'us-east-1')
    response = client.describe_instances()['Reservations']
    for instance in response:
        #pprint(instance.get('Instances'))
        for each_instance in instance.get('Instances'):
            #pprint(each_instance)

            response2 = client.describe_volumes()
            attactchment = response2.get('Volumes')
            gp3 = client.modify_volume(VolumeId='id', VolumeType='gp3')
            for each_volume in attactchment:
                type = each_volume.get('VolumeType')
                id = each_volume.get('VolumeId')
            pprint(gp3)
describe_instance_rsource()




