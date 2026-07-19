
# Route Tables

VPC comes with default (main) route table.
All unassociated subnets use the main table.

Any subnets that do not have explicit associates will default to the main table

Since we don't want to treat our public and private subnets the same, we will need to make 2 route tables

Then we add the route tables to the subnets
Route Table > Subnet associations > Edit Subnet Associations

Finally we add the internet gateway

Route Table > Routes > Edit Routes

For destination, everything so 0.0.0.0
