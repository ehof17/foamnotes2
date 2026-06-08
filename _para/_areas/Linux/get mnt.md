elijah-hoffman@sigpu1:~$ findmnt -T /mnt/Machine_Learning/spark_data/dbd_files/live/pageLog
TARGET                SOURCE                                                FSTYPE OPTIONS
/mnt/Machine_Learning //sandhills.int/systems/devFramework/Machine_Learning cifs   rw,relatime,vers=3.0,cache=strict,upcall_target=app,username=ml-service@sandhills.int,uid=0,noforceuid,gid=0,noforcegid,addr=1
elijah-hoffman@sigpu1:~$ time findmnt -T /mnt/Machine_Learning/spark_data/dbd_files/live/pageLog


elijah-hoffman@wigpu1:~$  findmnt -T /mnt/Machine_Learning/spark_data/dbd_files/live/pageLog
TARGET                SOURCE                                                FSTYPE OPTIONS
/mnt/Machine_Learning //sandhills.int/systems/devFramework/Machine_Learning cifs   rw,relatime,vers=3.1.1,cache=strict,upcall_target=app,username=ml-service,domain=sandhills.int,uid=0,noforceuid,gid=0,noforceg
elijah-hoffman@wigpu1:~$
