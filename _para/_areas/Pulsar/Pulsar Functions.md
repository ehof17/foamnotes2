# Pulsar functions

Pulsar team noticed that with Kafka, oftentimes a very simple but full microservice had to be deployed to make the data ingestion middleware work

Pulsar functions solve this

>Scenario: Processing user orders
Bob,28,$50 -> Send to orders topic -> split by commas, send to postgres
In kafka, you need an app to distribute messages to the orders topic, and an application that consumes it, splits it by commas, and sends it to the db

In pulsar, you can make a FunctionClass that splits the comma, later pulsar can get the JAR artifact  and data

Additionally, pulsar can take in a context


## 2 Main ways of developing pulsar functions
- [[Language native functions]]
- [[Language specific sdk function]]

[Language native functions]: <Language native functions.md> "Language native functions"
[Language specific sdk function]: <Language specific sdk function.md> "Language specific sdk function"
