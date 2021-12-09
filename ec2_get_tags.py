import boto3
import json

ec2=boto3.resource('ec2')
dict = {}

filters = [
        {
            'Name': 'instance-state-name',
            'Values' : ['running']
        }
]


instances = ec2.instances.filter(Filters=filters)

for instance in instances:
    id = instance.id
    tags = instance.tags
    for tag in tags : 
        if tag ['Key'] == 'Name' : 
            instancename = tag ['Value']
            dict ['id'] = id
            dict ['id']['Name'] = instancename
            json.dumps(dict)
