## Introduction
A static page

## Pricing
0.5 USD per month for one hosted zone
5 USD per year for one domain name

## Leverage below
- Github Action
- CFN
- Cloud Front
- s3
- ACM
- Budget
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

## Security

* CloudFront automatically mitigates DDoS (Distributed Denial of Service) attacks at the network and application layers.
* To sleep well at night, a budget alarm is setup to trigger email and sns pointing to a lambda that removes R53 records away from cloudfront. CloudFrontDistribution.DomainName itself is considered confidential.
