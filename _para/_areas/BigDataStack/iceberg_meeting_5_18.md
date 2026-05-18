Track metadata of iceberg tables
Support audit and compliance requirements

New namespace that has series of tables
iceberg.metadata
- catalog
- schema registry
- lineage - track it all the way upstream to its og sql source
- maintenance_log

Naintenance config

Is owner enforced by iceberg?
No its for us

How often is this gonna be changed
- A job that runs every half hour 

We have 2 tables
- maintenace tables
- schema version and maintenance_log are the partitioned key

Schema table
- has data classification --pii, sensitive, public

As far as creatint tables
- pipelines would not be creating tables themselves
- Potential jenkins/airflow job that can kick off a table like a form that fills output
- Nothing stopping someone from making a different image tag and then run it with their elevated permissions
- Want to be stricter without overdefining account
- DTA data sci role has permission to create table
- Can the airflow job only run with the permissions that the user has that ran it: Ideal world
- Easiest way to do it is the DTA thing
- Just LDAP is only mapped into airflow
- Will need to tie that mapping to the same spot of the minio mapping, iceberg mapping, and polaris mapping


ML group creating iceberg catalog right now
- if they have to go through this process everytime they start a training data table
Every training table should be static
Maybe we default of some kind, then a job that updates it that can change the owner/other thing
Just gotta make sure people are doing it

For the maintence 
snapshots are backups in this context

Are metadata tables being tracked as well
- metadata on the metadata could be tracked

A new metadata namespace
- user accounts that are running this stuff

In minio theres a ton of folders
Folder corresponds to iceberg namespace
within the folder there is not really human readable json metadata files and then the parquet files


