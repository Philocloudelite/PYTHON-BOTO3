
import boto3
from pprint import pprint

client = boto3.session.Session().client(service_name = 'ec2', region_name = 'us-east-1')
resource = boto3.session.Session().resource(service_name = 'ec2', region_name = 'us-east-1')

def meta_object():
    """ working with meta objects using resource
    """
    count = 1
    for each_region in resource.meta.client.describe_regions()['Regions']:
        # print(each_region)
        print(f"{count}, {each_region['RegionName']}, Region_endpoint: {each_region['Endpoint']}")
        count +=1
   

meta_object()



def filter_instance():
    """
    
    """