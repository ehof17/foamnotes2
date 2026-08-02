
# Compute
Compute services are color coded as orange in AWS.
Some compute services are:
[[EC2]], not often used on its own in large scale systems because other abstraction

[[Lambda]], you don't have to pay if you don't use it. Only draw back is you pay a lot more than you would if you spun up your own servers.

[[ECS]], not exactly a "compute" service itself, you would run this with [[EC2]] or [[fargate]]. Kinda like kubernetes but seen as easier to run than [[EKS]]

[[EKS]], for multi cloud portability

Common to see [[fargate]] with [[ECS]] for long lived serverless architecture

[EC2]: EC2.md "EC2"
[Lambda]: Lambda.md "Lambda"
[ECS]: ECS.md "ECS"
[fargate]: fargate.md "fargate"
[EKS]: EKS.md "EKS"
