#!/usr/bin/env python3

import boto3

zone_id = 'Z06958611JDYVCG41K93R'
record_name = 'the-alchemist.link.'
record_type = 'A'
aliasTarget = {}

def del_record():
    r53 = boto3.client('route53')

    # find the record's AliasTarget
    paginator = r53.get_paginator('list_resource_record_sets')
    source_zone_records = paginator.paginate(HostedZoneId=zone_id)
    for record_set in source_zone_records:
        for record in record_set['ResourceRecordSets']:
            if record['Type'] == record_type and record['Name'] == record_name:
                aliasTarget = record['AliasTarget']
                print(f"find aliasTarget: {aliasTarget}")
                break

    response = r53.change_resource_record_sets(
        HostedZoneId=zone_id,
        ChangeBatch={ 
            'Changes': [
                {
                    'Action': 'DELETE',
                    'ResourceRecordSet': {
                        'Name': record_name,
                        'Type': record_type,
                        'AliasTarget': aliasTarget
                    }
                }
            ]
        }
    )
    return response

def lambda_handler(event, context):
    print(f"budget_alert_action lambda triggered. event: {event}; context: {context}")
    del_record()
