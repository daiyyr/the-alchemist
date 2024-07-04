## Introduction
I believe this is the cheapest way to host a SPA or static website with https on S3

## Estimated Monthly Cost
* An AWS Hosted Zone: **$0.50 per month**
* An AWS Domain Name: **$5.00 per year**
* Free Tier AWS CloudFront:
- 1 TB of data transfer out to the internet per month
- 10,000,000 HTTP or HTTPS Requests per month

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

## Host your own website
- Replace secrets.AWS_ACCESS_KEY_ID_TEEMO1DAI and secrets.AWS_SECRET_ACCESS_KEY_TEEMO1DAI with your github secrets that stores aws credentials.
- Replace www.the-alchemist.link with a s3 name you choose (do not manually create it).
- Replace www.the-alchemist.link with the domain name you manually registered or imported in aws.
- After the first github action run, the ACM cert will be created. Put its ARN here: AcmCertificateArn: arn:aws:acm:us-east-1:account_id:certificate/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
- Update the site with your content in the /eleventy folder; Or update .github/workflows/deploy-static-page.yaml to put your own content in the s3 bucket
