
# Fanout exchange

Uses publisher - subscriber model
Messages published to the exchange are delivered to all bound queues, regardless of the messaging routing keys

Producer sends message to exchange
Unlike a direct exchange, queues are not automatically created when a message is sent. Consumers must explicitly declare and bind their queues to the exchange

Once the queues are bound, they receive all messages published to the exchange


### Usecases
- Broadcasting events to multiple services
- Live data streaming
- Logging systems


