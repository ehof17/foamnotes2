


### How to dump data
- Most useful sink are databases.
- Databases require schema

Pulsar comes with a schema registry on the topic level

A common problem with Kafka
- Teams need consensu

### Producer with Type enforcement

Specify the schema from ETF class
Sending the class instance itself
```java
Producer<ETF> producer = client.newProducer(JSONSchema.of(ETF.class)).topic(topic).create();
ETF etf = new ETF("2015-10-22");
producer.send(etf);

```

### Schema Info file
- AVRO schema from POJO
- JSON string representation of POJO, object in python, or struct in GO
