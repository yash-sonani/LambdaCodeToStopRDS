import json
import boto3

def lambda_handler(event, context):
    
    
    client = boto3.client('rds')
    
    response = client.describe_db_instances()
    
    # Find ARN of Every DB Instances
    
    for items in response['DBInstances']:
        
        res = client.list_tags_for_resource(
            ResourceName = items['DBInstanceArn']
        )
    
        # Flag is used for check flag present in DB Instance
        flag1 = False
        
        # Check Flag present in given DB Instance
        for tag in res['TagList']:
            
            if tag['Key'] == 'Tag1' and tag['Value'] == 'Value1':
                flag1 = True
        
        # If flag is True We need to stop Instance
        if flag1 :
            Res = stop_db_instance(DBInstanceIdentifier = items['DBInstanceIdentifier'])
            print('Response for Stop Call: ', Res)
 
