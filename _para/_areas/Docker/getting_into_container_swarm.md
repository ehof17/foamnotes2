try docker service ls and get an id. i cant exec into that container

elijah-hoffman@siml106:~$ docker service ls
nm5v6vkwks0s   sandhills_recsys_live_recsys                        replicated   10/10      mlregistry.sandhills.int/recsys:1.2.1
docker exec -it nm5v6vkwks0s /bin/bash
Error response from daemon: No such container: 3x22wc41nfuc

This is because that is the swarm service ID, not the container ID.
To get the actual container id, need to find the task running

docker ps --filter "name=sandhills_recsys_live_api_activity" --format "{{.ID}}\t{{.Names}}"
1a9bd8fd37b0    sandhills_recsys_live_api_activity.4.r8twszex2iefaju551a9o1d9v
8ae995e1aa7c    sandhills_recsys_live_api_activity.3.8nazr77fhoof9ykmfqq1o0d05
4b24b27f2326    sandhills_recsys_live_api_activity.9.3gxupwlnyu18vcew554kmfjf1
1b5064f4ef41    sandhills_recsys_live_api_activity.2.kfjzxct3a7ql98f8xrkl55khe
99e0e29789a0    sandhills_recsys_live_api_activity.1.wqmamjvzv54or1c4rlfncuhsx
c3593f33cbd6    sandhills_recsys_live_api_activity.8.n5ki3e3s5ymshksimyjz47n0f
6f88e4410456    sandhills_recsys_live_api_activity.6.kiquol36psmvoiyp2av18jlaq
7ac3fdef9d25    sandhills_recsys_live_api_activity.7.jrxdyl1gbk0yn9q1gruu6bgsq
297f65fd9271    sandhills_recsys_live_api_activity.10.z315fchp2f3nl3jjbdib3wku1
7b796775d973    sandhills_recsys_live_api_activity.5.xt0129l8y6toe82t05qao5un2

