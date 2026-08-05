# Kafka architectures

1. Producers
2. Kafka Cluster
   1. Zookeeper. Helps with the broker management. Elects the leader of the cluster, manages info of the topics, including the access control list of all the topics. Who can read/write to each topic
   2. Broker - Simply an instance of Kakfa, take messages from consumer
3. Consumer Group
   1. Set of apps that process messages 



1. Producer goes to zookeeper, to get the Kafka broker id. 
2. Kafka broker id is pushed messages 
3. Consumer then pulls the messages
4. Consumer then goes to zookeper to update offset. Offset keeps track of 



High level
Logistic management -> monolith -> database -> batch processing job

Kafka uses topics
When using a monolith app, we think in terms of data.
When working with kafka, we instead need to think in terms of events.
- When goods are picked up from warehouse
- When the delivery is completed
- When payment has been made

Logistic management now pushes these events to a topic
Internally, we have microservices that take data from the topics and process them
If we want to check the orders that are being processed every second
- We can create a mew topic for the orders processed, and push messages to the topic
- Then we can make a report that reads from the new orders processed topic to get live analytics, instead of the batch processing


### Kafka connect
- Direct connection to many services, like databases
- So databases can send their changes directly to a topic, then the app consumes them
- 
