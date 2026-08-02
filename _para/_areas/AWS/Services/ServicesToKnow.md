# Services Actually used in AWS

Can be broken down into different categories.
[[Compute]] for processing data
[[Networking and Delivery]],
[[Databases]], [[Storage]], [[Security and Identity]]

[[Management and Monitoring]]

[[App Integration and Messaging]]


## Basic stack
[[Lambda]] + [[API Gateway]] + [[Dynamo DB]]

## Standard Production architecture
Client -> [[Route 53]] to resolve IP
Static assets are delivered via [[Cloud Front]], pulling assets from [[S3]]. [[WAF]] sitting on top of it to block suspicious requests.

Frontend is now loaded from s3.

User request now goes to [[ELB ALB]] to decide which [[Compute]] will be handling that request.
> If compute is [[Lambda]] you don't really need a load balancer.. it could just be [[API Gateway]] at that point

The compute service probably need to access data. It gets the database secrets from [[Secrets Manager]] to access the [[Databases]].


[[VPC]] has the load balancer, backend compute, and the data layer

If the request is a slow job, we can instead send it off to [[Simple Queue Service]] (Outside the VPC), and have a [[Lambda]] worker.

All while this happens, [[CloudWatch]], [[CloudTrail]] log everything.

This was all deployed by [[CloudFormation]]

[Compute]: Compute.md "Compute"
[Networking and Delivery]: <Networking and Delivery.md> "Networking and Delivery"
[Lambda]: Lambda.md "Lambda"
[API Gateway]: <API Gateway.md> "API Gateway"
[Databases]: Databases.md "Databases"
[Storage]: Storage.md "Storage"
[Security and Identity]: <Security and Identity.md> "Security and Identity"
[Management and Monitoring]: <Management and Monitoring.md> "Management and Monitoring"
[App Integration and Messaging]: <App Integration and Messaging.md> "App Integration and Messaging"
[Dynamo DB]: <Dynamo DB.md> "Dynamo DB"
[Route 53]: <Route 53.md> "Route 53"
[Cloud Front]: <Cloud Front.md> "Cloud Front"
[S3]: S3.md "S3"
[WAF]: WAF.md "Web application firewall"
[ELB ALB]: <ELB ALB.md> "ELB ALB"
[Secrets Manager]: <Secrets Manager.md> "Secrets Manager"
[VPC]: VPC.md "VPC"
[Simple Queue Service]: <Simple Queue Service.md> "Simple Queue Service"
[CloudWatch]: CloudWatch.md "CloudWatch"
[CloudTrail]: CloudTrail.md "CloudTrail"
[CloudFormation]: CloudFormation.md "CloudFormation"
