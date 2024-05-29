## Introduction
Cheapest way to host a SPA or static website with https on S3

## Pricing
* Hosted Zone: **$0.50 per month**
* Domain Name: **$5.00 per year**

## Security

CloudFront automatically mitigates DDoS (Distributed Denial of Service) attacks at the network and application layers. Additionally, to sleep well at night, a budget alarm is setup. When monthly costs or forecasts exceed $1, it triggers:
- an email notification.
- a sns topic pointing to a lambda that removes R53 records away from cloudfront. Hence CloudFrontDistribution.DomainName is considered confidential and should be treated accordingly.

## Services Leveraged
- Github Action
- CFN
- CloudFront
- S3
- ACM
- AWS Budgets
- SNS
- Lambda

## ACM

* Use a seperate pipeline to deploy ACM because:
    - To use a certificate in AWS Certificate Manager (ACM) to require HTTPS between viewers and CloudFront, make sure you request (or import) the certificate in the US East (N. Virginia) Region (us-east-1).
    - https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-requirements.html

* Once cert created, manually update the second stack to triger the second pipeline
* The easiest way for cross-region cfn reference is customised Resource. I'd rather manual update here

## R53 Record

* For any CloudFrontDistribution AliasTarget, the HostedZoneId is always Z2FDTNDATAQYW2
* https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-aliastarget.html#cfn-route53-recordset-aliastarget-hostedzoneid
