#!/usr/bin/env python3

import boto3

zone_id = 'Z06958611JDYVCG41K93R'
record = 'www.the-alchemist.link'
r_type = 'A'

def del_record():
    r53 = boto3.client('route53')
    response = r53.change_resource_record_sets(
        HostedZoneId=zone_id,
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'DELETE',
                    'ResourceRecordSet': {
                        'Name': record,
                        'Type': r_type,
                        'TTL': 300
                    }
                }
            ]
        }
    )
    return response

def lambda_handler(event, context):
    del_record()
