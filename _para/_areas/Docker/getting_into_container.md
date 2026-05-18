Boot up container
docker run -it -v /mnt/DBSSIS:/mnt/DBSSIS -v /home/elijah-hoffman@sandhills.int/dockerstuff:/home/datacatalog mlregistry.sandhills.int/sandhills_python:3.10 bash

Get container ID
elijah-hoffman@siml103:~/adhoc/rag/rag_pipeline_doc_retrieval$ docker ps | grep 3.12
17a1cf88cb95   mlregistry.sandhills.int/sandhills_python:3.12                                                    "bash"                    2 minutes ago    Up 2 minutes                                                                                                              angry_gauss

docker exec -it <container_name_or_id> /bin/bash

docker run -it  -v /mnt/Machine_Learning/bis/chat_bot/data/:/mnt/Machine_Learning/bis/chat_bot/data/ -v /mnt/Human_Resource_Information/Benefits:/mnt/Human_Resource_Information/Benefits -v "/mnt/Human_Resource_Information/Employee Handbook:/mnt/Human_Resource_Information/Employee Handbook" -v /mnt/Emergency_and_Safety_Information:/mnt/Emergency_and_Safety_Information -v /home/elijah-hoffman@sandhills.int/adhoc/rag:/home/rag mlregistry.sandhills.int/sandhills_python:3.12 bash

