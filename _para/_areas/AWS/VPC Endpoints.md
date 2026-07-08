
# VPC Endpoints

https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html
- There is no additional charge for using gateway endpoints.

- gateway endpoints do not allow access from on-premises networks from peered VPCs in other AWS Regions, or through a transit gateway. For those scenarios, you must use an interface endpoint, which is available for an additional cost. For more information, see Types of VPC endpoints for Amazon S3 in the Amazon S3 User Guide.

- A gateway endpoint is available only in the Region where you created it. Be sure to create your gateway endpoint in the same Region as your S3 buckets.
