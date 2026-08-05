# RabbitMQ architecture
- Is a message broker architecture
- different components come together, where different components work together to enable async processing


Publisher sends message to rabbit RabbitMQ


Within rabbitmq, there are exchanges, which route messaages to queues

Then a subscriber processes the message


Publisher sends a message to the exchange, the exchange determines how to send the message using different routing mechanisms

Popular type of exhanges: 
[[Direct exchange]]
[[Fanout exchange]]
Topic exchange

[Direct exchange]: <Direct exchange.md> "Direct exchange"
