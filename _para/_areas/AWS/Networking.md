Creating a [[VPC]] can be done in console.

What [[CIDR]] range does this VPC fall in? Do 16 so theres more

Within a vpc, there are isolated networks in different cidr ranges called [[Subnets]]

Commonly find a public subnet and a private subnet

Public subnet - all public applications
- Normally see 2 public and 2 private, in different availability zone

Public Subnet
- 10.0.0.0/24
private
- 10.0.1.0/24

Often more for private since less things are public but nbd

When creating EC2 instane, can go into network settings to set the new vpc

After setting up, I can't connect. Why? Because there isn't internet access

We need an Internet [[Gateway]] to allow subnets out to the Internet

After adding the gateway to the vpc, trying to connect to ec2.... Fails

Why? We have to give our subnet a route to the internet gateway. We ca do this with [[Route Tables]]

On our public subnet, we need to allow a route out to the internet gateway.

> Do we have to do this for private traffic? No the route tables already allow for private traffic, we just need to add a rule to go out to the internet gateway

After adding the route to internet gateway we have public access to internet.

Next lets have another EC2 in the private subnet

Private instance allows ssh access from public instance

To do that we gotta get the key on the public instance


```
sudo scp -i /Users/ehof/Downloads/newKeypair.pem /Users/ehof/Downloads/newKeypair.pem ec2-user@52.203.200.115:/home/ec2-user
```

After doing that you can try sshing into the private ec2. Might run into permission issuses. Had to update permissions

```
chmod 400 newKeypair.pem
```

How do we access internet on the private ec2?
We can't update packages via yum or anything
Can we reach out to the internet, but no one can reach in to us?

Yes you can with a [[Nat gateway]]

We will need to make a Nat gateway in the public subnet

Public subnet has a route out to the internet
Private route table routes to the new nat gateway

EC2 on private sub -> Route table -> Public sub nat gateway -> Route table -> Internet

Add the NAT gateway
In private subnet add a route for everything/0 to the new nat gateway

Now we can get packages 

Additional layers of protection are
[[NACL]] and [[Security Groups]]


[VPC]: VPC.md "VPC"
[CIDR]: CIDR.md "CIDR"

[Subnets]: Subnets.md "Subnets"
[Gateway]: Gateway.md "Gateway"

[Route Tables]: <Route Tables.md> "Route Tables"
[Nat gateway]: <Nat gateway.md> "Nat gateway"
